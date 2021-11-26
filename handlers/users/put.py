from utils.database import db_session
from utils.models import Usuario

from utils.response import OK

def handler(event, context):
    id_user = event['pathParameters']['id_user']
    premium = True
    if 'queryStringParameters' in event and event["queryStringParameters"] and 'premium' in event["queryStringParameters"]:
        premium = event["queryStringParameters"]['premium'] == 'true'
    user = [{
      'id': id_user,
      'premium': premium
    }]
    db_session.bulk_update_mappings(Usuario, user)
    db_session.commit()
    return OK('sucesso')