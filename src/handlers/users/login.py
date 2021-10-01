from utils.database import db_session
from utils.models import Usuario
from nanoid import generate
import json

from utils.response import NOT_FOUND, OK

def handler(event, context):
    body = json.loads(event['body'])
    nome = body['nome']
    senha = body['senha']
    user = db_session.query(Usuario).filter(Usuario.nome == nome).filter(Usuario.senha == senha).all()
    if not user:
        return NOT_FOUND('credenciais incorretas')
    return OK('sucesso')