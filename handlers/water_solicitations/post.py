from utils.database import db_session
from utils.models import SolicitacoesRega
from nanoid import generate
import json

from utils.response import BAD_REQUEST, OK

def handler(event, context):
    id_user_plant = event['pathParameters']['id_user_plant']
    body = json.loads(event['body'])
    
    try:
        hora = body['hora']
    except:
        return BAD_REQUEST('entrada errada')

    water_solicitation = SolicitacoesRega(
        id=generate(),
        id_usuario_planta=id_user_plant,
        hora=hora,
        completo=False
    )
    db_session.add(water_solicitation)
    db_session.commit()
    return OK('sucesso')