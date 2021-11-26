from utils.database import db_session
from utils.models import SolicitacoesRega

from utils.response import OK

def handler(event, context):
    id_water_solicitation = event['pathParameters']['id_water_solicitation']
    water_solicitation = [{
      'id': id_water_solicitation,
      'completo': True
    }]
    db_session.bulk_update_mappings(SolicitacoesRega, water_solicitation)
    db_session.commit()
    return OK('sucesso')