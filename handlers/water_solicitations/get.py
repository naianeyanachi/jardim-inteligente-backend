from utils.database import db_session
from utils.models import SolicitacoesRega
from utils.response import OK, NOT_FOUND
from utils.schemas import SolicitacoesRegaSchema
import json

def handler(event, context):
    id_user_plant = event['pathParameters']['id_user_plant']
    completo = False
    if 'completo' in event["queryStringParameters"]:
        completo = event["queryStringParameters"]['completo'] == 'true'
    water_solicitation = db_session.query(SolicitacoesRega).filter(SolicitacoesRega.id_usuario_planta == id_user_plant).filter(SolicitacoesRega.completo == completo).all()
    if not water_solicitation:
        return NOT_FOUND('solicitacao nao encontrada')
    water_solicitation = SolicitacoesRegaSchema(many=True).dump(water_solicitation).data
    return OK(json.dumps(water_solicitation))