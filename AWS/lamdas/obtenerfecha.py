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

def create_lex_response(intent_name, slots, message, dialog_action_type='Close', slot_to_elicit=None, state='Fulfilled', session_attributes=None):
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
            },
            'sessionAttributes': session_attributes or {}
        },
        'messages': [{
            'contentType': 'PlainText',
            'content': message
        }]
    }
    
    if slot_to_elicit:
        response['sessionState']['dialogAction']['slotToElicit'] = slot_to_elicit
    
        # Agregamos el invocationLabel si se proporciona

    
    logger.debug(f"Respuesta de Lex: {json.dumps(response)}")
    return response

def lambda_handler(event, context):
    try:
        logger.debug('Evento recibido: %s', json.dumps(event))
        intent = event['sessionState']['intent']
        intent_name = intent['name']
        slots = intent.get('slots', {})
        
        if event['invocationSource'] == 'DialogCodeHook':
            fecha_slot = slots.get('fecha', {})
            hora_slot = slots.get('hora', {})
            confirmation_slot = slots.get('confirmation', {})
            
            # Si no hay fecha, solicitarla
            if not fecha_slot or not fecha_slot.get('value'):
                return create_lex_response(
                    intent_name, slots,
                    '¿Para qué fecha deseas agendar?',
                    'ElicitSlot', 'fecha'
                )
            
            # Validar fecha
            date_str = fecha_slot['value'].get('interpretedValue')
            validation_result = validate_date(date_str)
            if not validation_result['isValid']:
                return create_lex_response(
                    intent_name, slots,
                    validation_result['message'],
                    'ElicitSlot', 'fecha'
                )
            
            # Si fecha es válida, pero no hay confirmación, pedir confirmación
            if not confirmation_slot or not confirmation_slot.get('value'):
                formatted_date = format_date_for_response(validation_result['date'])
                return create_lex_response(
                    intent_name, slots,
                    f'¿Confirmas que quieres agendar para el {formatted_date}? Por favor responde sí o no.',
                    'ElicitSlot', 
                    'confirmation',
                    session_attributes={'isDateConfirmation': 'true'}
                )
            
            # Procesar confirmación de fecha
            confirmacion = confirmation_slot['value'].get('interpretedValue', '').lower()
            if confirmacion == 'no':
                slots['fecha'] = None
                slots['confirmation'] = None
                return create_lex_response(
                    intent_name, slots,
                    'De acuerdo, por favor ingresa una nueva fecha.',
                    'ElicitSlot', 'fecha'
                )
            elif confirmacion in ['si', 'sí']:
                # Si fecha confirmada pero no hay hora, pedir hora
                if not hora_slot or not hora_slot.get('value'):
                    formatted_date = format_date_for_response(validation_result['date'])
                    return create_lex_response(
                        intent_name, slots,
                        f'¿A qué hora te gustaría tu cita el {formatted_date}?',
                        'ElicitSlot', 'hora',
                        session_attributes={'isHourElicitation': 'true'}
                    )
                
                # Si hay hora, confirmar la cita completa
                formatted_date = format_date_for_response(validation_result['date'])
                hora = hora_slot['value'].get('interpretedValue')
                return create_lex_response(
                    intent_name, slots,
                    f'¡Perfecto! Tu cita ha sido agendada para el {formatted_date} a las {hora}.',
                    'Close', state='Fulfilled'
                )
        
        return create_lex_response(
            intent_name, slots,
            '¡Tu cita ha sido agendada exitosamente!'
        )
        
    except Exception as e:
        logger.error(f'Error: {str(e)}')
        return create_lex_response(
            event['sessionState']['intent']['name'],
            {}, 'Lo siento, hubo un error procesando tu solicitud.',
            state='Failed'
        )
