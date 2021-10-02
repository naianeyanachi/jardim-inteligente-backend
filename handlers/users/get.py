from utils.database import db_session
from utils.models import Usuario
from utils.response import OK, NOT_FOUND
from utils.schemas import UsuarioSchema
import json

def handler(event, context):
    id_user = event['pathParameters']['id_user']
    user = db_session.query(Usuario).get(id_user)
    if not user:
        return NOT_FOUND('usuario nao encontrado')
    user = UsuarioSchema().dump(user).data
    return OK(json.dumps(user))