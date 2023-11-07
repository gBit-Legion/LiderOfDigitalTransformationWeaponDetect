from sqlalchemy.orm import Session
from Database.database_connect import engine
from sqlalchemy.orm.query import Query
from Database.models import *
from Services.TableParser import TableParser
from Services.ArchiveFileExtractor import ZipFileExtractor
from Services.CameraVideoCapture import RTSPCamera

# Здесь нужно описать запросы к бд
session = Session(bind=engine)


def add_in_dataset(dataset_path):
    pass
