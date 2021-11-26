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
        return BAD_REQUEST('entrada errada')
    try:
        usuario = Usuario(id=generate(), nome=nome, senha=senha, premium=False)
        db_session.add(usuario)
        db_session.commit()
    except:
        db_session.rollback()
        raise
    return OK('sucesso')