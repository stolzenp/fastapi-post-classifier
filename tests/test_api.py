from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_predict_valid_input():
    response = client.post("/predict", json={"text": "This is a test"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # values should be floats
    assert all(isinstance(prob, float) for prob in data.values())
    # probs should sum up to 1 (small tolerance)
    assert abs(sum(data.values()) - 1.0) < 1e-5


def test_predict_missing_text_field():
    response = client.post("/predict", json={"wrong_field": "This should fail"})
    assert response.status_code == 422  # misses required field 'text'


def test_predict_missing_text():
    response = client.post("/predict", json={})
    assert response.status_code == 422  # no field provided


def test_predict_empty_text():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all(isinstance(prob, float) for prob in data.values())
    assert abs(sum(data.values()) - 1.0) < 1e-5
