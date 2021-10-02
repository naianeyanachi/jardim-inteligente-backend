from utils.database import db_session
from utils.models import UsuarioPlanta
from utils.response import OK, NOT_FOUND
from utils.schemas import UsuarioPlantaSchema
import json

def handler(event, context):
    id_user_plant = event['pathParameters']['id_user_plant']
    user_plant = db_session.query(UsuarioPlanta).get(id_user_plant)
    if not user_plant:
        return NOT_FOUND('planta nao encontrado')
    user_plant = UsuarioPlantaSchema().dump(user_plant).data
    return OK(json.dumps(user_plant))