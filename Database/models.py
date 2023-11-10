from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CameraObject(Base):
    __tablename__ = "camera_db"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255))
    latitude = Column(String(255))
    longitude = Column(String(255))
    physical_address = (String(255))