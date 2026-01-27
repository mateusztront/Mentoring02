# Tutaj tworzenie silnika pod testy

from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool

from ..src.main import app
from ..src.models import User, get_session

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

@pytest.fixture()
def client():
    SQLModel.metadata.create_all(engine)

    def override_get_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    yield TestClient(app) # to co powyzej wykonuje sie przed testem, a to co ponizej po tescie
    
    app.dependency_overrides.clear()
    SQLModel.metadata.drop_all(engine)