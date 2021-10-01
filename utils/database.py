from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_user = "jardim"
db_pass = "qCBe398azmCyh6T"
db_host = "jardim-inteligente.cg3vj23v6toi.us-east-1.rds.amazonaws.com"
db_port = "5432"
db_name = "jardim_inteligente"

engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

Session = sessionmaker(bind=engine)

db_session = Session()