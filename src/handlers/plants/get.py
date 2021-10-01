from utils.database import db_session
from utils.models import Planta
from utils.response import OK, NOT_FOUND
from utils.schemas import PlantaSchema
import json

def handler(event, context):
    id_plant = event['pathParameters']['id_plant']
    plant = db_session.query(Planta).get(id_plant)
    if not plant:
        return NOT_FOUND('planta nao encontrado')
    plant = PlantaSchema().dump(plant).data
    return OK(json.dumps(plant))