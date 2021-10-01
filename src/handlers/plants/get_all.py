from utils.database import db_session
from utils.models import Planta
from utils.response import OK, NOT_FOUND
from utils.schemas import PlantaSchema
import json

def handler(event, context):
    plants = db_session.query(Planta).all()
    if not plants:
        return NOT_FOUND('nenhuma planta :(')
    plants = PlantaSchema(many=True).dump(plants).data
    return OK(json.dumps(plants))