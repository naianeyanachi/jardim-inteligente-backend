from utils.database import db_session
from utils.models import UsuarioPlanta
from utils.response import OK, NOT_FOUND
from utils.schemas import UsuarioPlantaSchema
import json

def handler(event, context):
    id_user = event['pathParameters']['id_user']
    plants = db_session.query(UsuarioPlanta).filter(UsuarioPlanta.id_usuario == id_user).all()
    if not plants:
        return NOT_FOUND('nenhuma planta :(')
    plants = UsuarioPlantaSchema(many=True).dump(plants).data
    return OK(json.dumps(plants))