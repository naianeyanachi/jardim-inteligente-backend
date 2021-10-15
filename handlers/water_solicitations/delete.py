from utils.database import db_session
from utils.models import SolicitacoesRega
from utils.response import OK, NOT_FOUND
import json

def handler(event, context):
    id_water_solicitation = event['pathParameters']['id_water_solicitation']
    water_solicitation = db_session.query(SolicitacoesRega).get(id_water_solicitation)
    if not water_solicitation:
        return NOT_FOUND('solicitacao de rega nao encontrada')
    db_session.delete(water_solicitation)
    db_session.commit()
    return OK('sucesso')