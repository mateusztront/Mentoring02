from app2_refactored.src.models import User
from .conftest import client, engine
from sqlmodel import Session

def test_get_users_missing_user(client):
    response = client.get('/users/9999')
    assert response.status_code == 404
    assert response.json() == {'detail': {'error': 'User not found'}}

def test_get_users_user_exist(client):
    with Session(engine) as session:
        user = User(pesel = "123456", name="Test", address="Addr")
        session.add(user)
        session.commit()

    response = client.get("/users/123456")
    assert response.status_code == 200
    assert response.json()["name"] == "Test"
    assert response.json()["address"] == "Addr"
    assert response.json()["diseases"] == []
    assert response.json()["tel_number"] == None