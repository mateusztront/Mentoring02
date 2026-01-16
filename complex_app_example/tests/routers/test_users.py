from app.models import User

def test_get_me(client, db):
    user = User(
        email="admin@test.com",
        role="admin"
    )
    db.add(user)
    db.commit()

    response = client.get("/users/me")

    assert response.status_code == 200
    data = response.json()

    assert data["email"] == "admin@test.com"
    assert data["role"] == "admin"
