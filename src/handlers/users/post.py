from utils.database import db_session
from utils.models import Usuario
from nanoid import generate
import json

from utils.response import BAD_REQUEST, OK

def handler(event, context):
    body = json.loads(event['body'])
    
    try:
        nome = body['nome']
        senha = body['senha']
    except:
        BAD_REQUEST('entrada errada')

    usuario = Usuario(id=generate(), nome=nome, senha=senha)
    db_session.add(usuario)
    db_session.commit()
    return OK('sucesso')