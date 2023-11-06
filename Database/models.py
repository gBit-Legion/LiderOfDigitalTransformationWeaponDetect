from sqlmodel import Field, Session, SQLModel, create_engine

class CameraObject(SQLModel, table=True):
    id: int = Field()
