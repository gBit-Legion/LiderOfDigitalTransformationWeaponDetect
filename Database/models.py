from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CameraObject(Base):
    __tablename__ = "camera_db"

    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    latitude = Column(String(255))
    longitude = Column(String(255))
    physical_address = (String(255))


class DatasetDB(Base):
    __tablename__ = "dataset_db"

    id = Column(Integer, primary_key=True)
    full_file_path = Column(String(255))
    labels_path = Column(String(255))


class EmployeeDB(Base):
    __tablename__ = "employee_db"
    id = Column(Integer, primary_key=True)
    FIO = Column(String(255))
    day_password = Column(String(255))
