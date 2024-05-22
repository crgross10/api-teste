from fastapi.testclient import TestClient

from api_fast import app

def test_add_cliente():
    with TestClient(app) as client:
        response = client.post(
            "/clientes/",
            json={"id": 1, "nome": "Cristiano", "email": "cristianogross@outlook.com", "telefone": "99999999"},
        )
    assert response.status_code == 200
    assert response.json() == "Cliente adicionado!"

def test_get_cliente():
    with TestClient(app) as client:
        response = client.get("/cliente/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "nome": "Cristiano", "email": "cristianogross@outlook.com", "telefone": "99999999"}
