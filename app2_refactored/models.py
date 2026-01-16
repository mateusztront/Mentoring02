from sqlmodel import Column, SQLModel, Field, Session, create_engine, PickleType
from typing import List
from sqlalchemy.ext.mutable import MutableList

class User(SQLModel, table=True):
    pesel: int = Field(primary_key=True)
    name: str = Field()
    address: str = Field()
    dieseses: List[str | None] = Field(sa_column=Column(MutableList.as_mutable(PickleType)),
                                    default=[])
    tel_number: int | None = Field(default=None) 

sqlite_url = "sqlite:///database.db"

engine = create_engine(sqlite_url, echo=True) # echo prints underlying sqls  

def get_session():
    with Session(engine) as session:
        yield session

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def create_dummy_users():
    dummy_users_1 = User(pesel=12345, name="John Doe", address="123 Main St", dieseses=["flu"], tel_number=5551234567)
    dummy_users_2 = User(pesel=67890, name="Jane Smith", address="456 Oak Ave", dieseses=["psoriasis", "egzema"], tel_number=5559876543)

    with Session(engine) as session:
        user1_exists = session.query(User).filter(User.pesel == 12345).first()
        user2_exists = session.query(User).filter(User.pesel == 67890).first()
        
        if not user1_exists:
            session.add(dummy_users_1)
        if not user2_exists:
            session.add(dummy_users_2)
        
        session.commit()
