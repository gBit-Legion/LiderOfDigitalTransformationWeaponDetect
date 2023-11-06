from sqlmodel import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/5432"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
