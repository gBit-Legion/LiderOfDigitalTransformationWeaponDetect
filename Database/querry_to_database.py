from fastapi_sqlalchemy.middleware import DBSession
from sqlalchemy.orm import Session
from Database.database_connect import engine
from sqlalchemy.orm.query import Query
from Database.models import *


# Здесь нужно описать запросы к бд
session_maker = Session(bind=engine)
session = DBSession


def add_in_dataset(list_from_camera_parse):

    add_to_database = CameraObject(url=1)
