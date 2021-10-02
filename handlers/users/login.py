from utils.database import db_session
from utils.models import Usuario
import json

from utils.response import NOT_FOUND, OK
from utils.schemas import UsuarioSchema

def handler(event, context):
    body = json.loads(event['body'])
    nome = body['nome']
    senha = body['senha']
    user = db_session.query(Usuario).filter(Usuario.nome == nome).filter(Usuario.senha == senha).all()
    if not user:
        return NOT_FOUND('credenciais incorretas')
    user = UsuarioSchema().dump(user[0]).data
    return OK(json.dumps(user))