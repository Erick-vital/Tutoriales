import json
import datetime
from datetime import timedelta
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def validate_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.date.today()
        if date_obj < today:
            logger.debug(f"Fecha inválida: {date_str} está en el pasado.")
            return {
                'isValid': False,
                'message': 'La fecha no puede estar en el pasado'
            }
        logger.debug(f"Fecha válida: {date_str}")
        return {
            'isValid': True,
            'date': date_obj
        }
    except ValueError:
        logger.debug(f"Formato de fecha inválido: {date_str}")
        return {
            'isValid': False,
            'message': 'Formato de fecha inválido'
        }

def format_date_for_response(date_obj):
    dias = {
        0: 'Lunes', 1: 'Martes', 2: 'Miércoles',
        3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'
    }
    meses = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
        5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
        9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    
    dia_semana = dias[date_obj.weekday()]
    dia = date_obj.day
    mes = meses[date_obj.month]
    año = date_obj.year
    
    return f"{dia_semana} {dia} de {mes} del {año}"

def create_lex_response(intent_name, slots, message, dialog_action_type='Close', slot_to_elicit=None, state='Fulfilled'):
    logger.debug(f"Creando respuesta con dialogActionType: {dialog_action_type}, slotToElicit: {slot_to_elicit}")
    response = {
        'sessionState': {
            'dialogAction': {
                'type': dialog_action_type
            },
            'intent': {
                'name': intent_name,
                'slots': slots,
                'state': state
            }
        },
        'messages': [{
            'contentType': 'PlainText',
            'content': message
        }]
    }
    
    if slot_to_elicit:
        response['sessionState']['dialogAction']['slotToElicit'] = slot_to_elicit
    
    logger.debug(f"Respuesta de Lex: {json.dumps(response)}")
    return response

def lambda_handler(event, context):
    try:
        logger.debug('Evento recibido: %s', json.dumps(event))
        
        # Obtener información del intent y slots
        intent = event['sessionState']['intent']
        intent_name = intent['name']
        slots = intent.get('slots', {})
        
        logger.debug(f"Intent: {intent_name}, Slots: {json.dumps(slots)}")
        
        # Si es un DialogCodeHook, procesar la fecha
        if event['invocationSource'] == 'DialogCodeHook':
            logger.debug("InvocationSource es DialogCodeHook")
            
            # Obtener el valor del slot de fecha y confirmación
            fecha_slot = slots.get('fecha', {})
            confirmacion_slot = slots.get('confirmation', {})
            
            logger.debug(f"Slot fecha: {json.dumps(fecha_slot)}, Slot confirmation: {json.dumps(confirmacion_slot)}")
            
            # Si no hay fecha, solicitarla
            if not fecha_slot or not fecha_slot.get('value'):
                logger.debug("No se proporcionó fecha, solicitando al usuario.")
                return create_lex_response(
                    intent_name,
                    slots,
                    '¿Para qué fecha deseas agendar? Puedes decir "hoy", "mañana", "próximo sábado", etc.',
                    'ElicitSlot',
                    'fecha'
                )
            
            date_str = fecha_slot['value'].get('interpretedValue')
            logger.debug(f"Fecha proporcionada: {date_str}")
            validation_result = validate_date(date_str)
            
            # Si la fecha no es válida, solicitar nueva fecha
            if not validation_result['isValid']:
                logger.debug(f"Fecha no válida: {validation_result['message']}")
                return create_lex_response(
                    intent_name,
                    slots,
                    validation_result['message'],
                    'ElicitSlot',
                    'fecha'
                )
            
            # Si la fecha es válida pero no hay confirmación, solicitarla
            if not confirmacion_slot or not confirmacion_slot.get('value'):
                formatted_date = format_date_for_response(validation_result['date'])
                logger.debug(f"Solicitando confirmación para la fecha: {formatted_date}")
                return create_lex_response(
                    intent_name,
                    slots,
                    f'¿Confirmas que quieres agendar para el {formatted_date}? Por favor responde sí o no.',
                    'ElicitSlot',
                    'confirmation'
                )
            
            # Procesar la confirmación
            confirmacion = confirmacion_slot['value'].get('interpretedValue', '').lower()
            logger.debug(f"Confirmación proporcionada: {confirmacion}")
            if confirmacion == 'no':
                # Si el usuario dice no, limpiar la fecha y volver a preguntar
                slots['fecha'] = None
                slots['confirmation'] = None
                logger.debug("El usuario no confirmó, solicitando nueva fecha.")
                return create_lex_response(
                    intent_name,
                    slots,
                    'De acuerdo, ¿para qué fecha prefieres agendar?',
                    'ElicitSlot',
                    'fecha'
                )
            elif confirmacion == 'si' or confirmacion == 'sí':
                # Si el usuario confirma, proceder con el cierre
                formatted_date = format_date_for_response(validation_result['date'])
                logger.debug(f"El usuario confirmó, agendando cita para: {formatted_date}")
                return create_lex_response(
                    intent_name,
                    slots,
                    f'¡Perfecto! Tu cita ha sido agendada para el {formatted_date}.',
                    'Close',
                    state='Fulfilled'
                )
        
        # Si no es DialogCodeHook, cerrar el intent
        logger.debug("InvocationSource no es DialogCodeHook, cerrando el intent.")
        return create_lex_response(
            intent_name,
            slots,
            '¡Tu cita ha sido agendada exitosamente!'
        )
        
    except Exception as e:
        logger.error(f'Error: {str(e)}')
        return create_lex_response(
            event['sessionState']['intent']['name'],
            {},
            'Lo siento, hubo un error procesando tu solicitud.',
            state='Failed'
        )
