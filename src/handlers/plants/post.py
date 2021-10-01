from utils.database import db_session
from utils.models import Planta
from utils.response import BAD_REQUEST, OK
from nanoid import generate
import json


def handler(event, context):
    body = json.loads(event['body'])
    
    try:
        especie = body['especie']
        descricao = body['descricao']
        temperatura_maxima = body['temperatura_maxima']
        temperatura_minima = body['temperatura_minima']
        temperatura_ideal = body['temperatura_ideal']
        umidade_solo_ideal = body['umidade_solo_ideal']
        umidade_ar_ideal = body['umidade_ar_ideal']
        luminosidade_ideal = body['luminosidade_ideal']
        regas = body['regas']
        preco = body['preco']
    except:
        BAD_REQUEST('entrada errada')

    planta = Planta(
        id=generate(),
        especie=especie,
        descricao=descricao,
        temperatura_maxima=temperatura_maxima,
        temperatura_minima=temperatura_minima,
        temperatura_ideal=temperatura_ideal,
        umidade_solo_ideal=umidade_solo_ideal,
        umidade_ar_ideal=umidade_ar_ideal,
        luminosidade_ideal=luminosidade_ideal,
        regas=regas,
        preco=preco,
    )
    db_session.add(planta)
    db_session.commit()
    return OK('sucesso')