import json
import datetime
from datetime import timedelta
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def validate_date(date_str):
    """
    Valida si la fecha es válida y no está en el pasado
    """
    try:
        # Convertir el string de fecha ISO a objeto datetime
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.date.today()
        
        # Verificar si la fecha es futura
        if date_obj < today:
            return {
                'isValid': False,
                'message': 'La fecha no puede estar en el pasado'
            }
        return {
            'isValid': True,
            'date': date_obj
        }
    except ValueError:
        return {
            'isValid': False,
            'message': 'Formato de fecha inválido'
        }

def format_date_for_response(date_obj):
    """
    Formatea la fecha para la respuesta al usuario
    """
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
    
    return response

def lambda_handler(event, context):
    """
    Función principal del Lambda handler
    """
    try:
        logger.debug('Event: %s', json.dumps(event))
        
        # Obtener información del intent y slots
        intent = event['sessionState']['intent']
        intent_name = intent['name']
        slots = intent.get('slots', {})
        
        # Si es un DialogCodeHook, procesar la fecha
        if event['invocationSource'] == 'DialogCodeHook':
            # Obtener el valor del slot de fecha
            fecha_slot = slots.get('fecha', {})
            if not fecha_slot or not fecha_slot.get('value'):
                return create_lex_response(
                    intent_name,
                    slots,
                    '¿Para qué fecha deseas agendar? Puedes decir "hoy", "mañana", "próximo sábado", etc.',
                    'ElicitSlot',
                    'fecha'
                )
            
            date_str = fecha_slot['value'].get('interpretedValue')
            validation_result = validate_date(date_str)
            
            if not validation_result['isValid']:
                return create_lex_response(
                    intent_name,
                    slots,
                    validation_result['message'],
                    'ElicitSlot',
                    'fecha'
                )
            
            formatted_date = format_date_for_response(validation_result['date'])
            return create_lex_response(
                intent_name,
                slots,
                f'He registrado tu cita para el {formatted_date}. ¿Es esto correcto?',
                'ConfirmIntent'
            )
            
        # Si no es DialogCodeHook, cerrar el intent
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
