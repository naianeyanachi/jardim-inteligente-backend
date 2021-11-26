import datetime

from utils.response import OK


def handler(event, context):
    return OK(datetime.datetime.utcnow.isoformat())