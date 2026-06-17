from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_inicio():
    response = client.get("/")

    assert response.status_code == 200
    assert "mensaje" in response.json()

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert "estado" in response.json()
    # assert "modelo_disponible" in response.json()
    assert "modelo" in response.json()

#pruebas para /predict 
def test_predict_valido():

    payload = {
        "antiguedad": 24,
        "cargo_mensual": 80.5,
        "reclamos": 1
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediccion" in data
    assert "probabilidad" in data
    assert "version_modelo" in data
# 
def test_predict_error_422():

    payload = {
        "antiguedad": 24,
        "cargo_mensual": 80.5
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 422
