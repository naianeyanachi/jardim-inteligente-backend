from utils.database import db_session
from utils.models import UsuarioPlanta
from nanoid import generate
import json

from utils.response import BAD_REQUEST, OK

def handler(event, context):
    id_usuario = event['pathParameters']['id_user']
    body = json.loads(event['body'])
    
    try:
        id_planta = body['id_planta']
        nome = body['nome']
        temperatura_maxima = body['temperatura_maxima']
        temperatura_minima = body['temperatura_minima']
        temperatura_ideal = body['temperatura_ideal']
        umidade_solo_ideal = body['umidade_solo_ideal']
        umidade_ar_ideal = body['umidade_ar_ideal']
        luminosidade_ideal = body['luminosidade_ideal']
        regas = body['regas']
    except:
        return BAD_REQUEST('entrada errada')

    user_plant = UsuarioPlanta(
        id=generate(),
        id_usuario=id_usuario,
        id_planta=id_planta,
        nome=nome,
        temperatura_maxima=temperatura_maxima,
        temperatura_minima=temperatura_minima,
        temperatura_ideal=temperatura_ideal,
        umidade_solo_ideal=umidade_solo_ideal,
        umidade_ar_ideal=umidade_ar_ideal,
        luminosidade_ideal=luminosidade_ideal,
        regas=regas
    )
    try:
        db_session.add(user_plant)
        db_session.commit()
    except:
        db_session.rollback()
        raise
    return OK('sucesso')