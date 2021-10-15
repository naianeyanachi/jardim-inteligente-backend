from utils.database import db_session
from utils.models import Medicao
from utils.response import OK, NOT_FOUND
from utils.schemas import MedicaoSchema
import json

def handler(event, context):
    id_user_plant = event['pathParameters']['id_user_plant']
    # completo = False
    # if 'completo' in event["queryStringParameters"]:
    #     completo = event["queryStringParameters"]['completo'] == 'true'
    measurements = db_session.query(Medicao).filter(Medicao.id_usuario_planta == id_user_plant).order_by(Medicao.created_at.desc()).all()
    if not measurements:
        return NOT_FOUND('medicoes nao encontradas')
    measurements = MedicaoSchema(many=True).dump(measurements).data
    return OK(json.dumps(measurements))