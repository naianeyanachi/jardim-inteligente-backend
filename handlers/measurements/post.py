from utils.database import db_session
from utils.models import Medicao
from nanoid import generate
import json

from utils.response import BAD_REQUEST, OK

def handler(event, context):
    id_user_plant = event['pathParameters']['id_user_plant']
    body = json.loads(event['body'])
    
    try:
        temperatura = body['temperatura']
        umidade_solo = body['umidade_solo']
        umidade_ar = body['umidade_ar']
        luminosidade = body['luminosidade']
    except:
        return BAD_REQUEST('entrada errada')

    measurement = Medicao(
        id=generate(),
        id_usuario_planta=id_user_plant,
        temperatura=temperatura,
        umidade_ar=umidade_ar,
        umidade_solo=umidade_solo,
        luminosidade=luminosidade
    )
    db_session.add(measurement)
    db_session.commit()
    return OK('sucesso')