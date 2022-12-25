from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB.entity import ClientData, Transaction, base
from Utility.app_configs import Configs as cfg
from dotenv import load_dotenv

load_dotenv()

db = create_engine(cfg().dbUrl)
Session = sessionmaker(db)
session = Session()

# Helps In Table Migration
base.metadata.create_all(db)


# Create
def create_client_data():
    doctor_strange = ClientData(title="Doctor Strange", director="Scott Derrickson", year="2016")
    session.add(doctor_strange)
    session.commit()


# Read
def get_client_data():
    films = session.query(ClientData)
    for film in films:
        print(film.title)
