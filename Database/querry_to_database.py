from sqlalchemy.orm import Session, sessionmaker
from Database.database_connect import engine
from sqlalchemy.orm.query import Query
from Database.models import *
from Services.TableParser import TableParser
from Services.random_addres_generator import address_generator
from models import CameraObject


def add_in_dataset(file_path):
    Session = sessionmaker(engine)
    session = Session()
    list_id = []
    tp = TableParser(file_path)
    url_list = tp.parse_xlsx_file()
    for url in url_list:
        address, lat, lon = address_generator()
        add_to_database = CameraObject.add(url=url, latitude=lat, lontitude=lon, physical_address=address)
        record = session.query(CameraObject).filter_by(url=url).first()
        list_id.append({record.id: record.url})
        session.add(add_to_database)

    session.commit()
    session.close()
    return list_id


def id_to_url(id_list):
    Session = sessionmaker(engine)
    session = Session()

    for id in id_list:
        record = session.query(CameraObject).filter_by(id=id).first()
        list.append(record.url)
    return list
