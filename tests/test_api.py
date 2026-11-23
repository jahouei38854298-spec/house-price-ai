import pytest

from fastapi.testclient import TestClient

from app.main import app



@pytest.fixture
def client():

    with TestClient(app) as test_client:

        yield test_client

    


def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "House Price Prediction API is running"
    }



def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["model_loaded"] is True




def test_predict_success(client):

    response = client.post(
        "/predict",
        json={
            "area": 120,
            "rooms": 3,
            "age": 5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["area"] == 120
    assert data["rooms"] == 3
    assert data["age"] == 5

    assert data["predicted_price"] == 3948.56





def test_predict_invalid_area(client):

    response = client.post(
        "/predict",
        json={
            "area": 50,
            "rooms": 3,
            "age": 5
        }
    )

    assert response.status_code == 422




def test_predict_invalid_rooms(client):

    response = client.post(
        "/predict",
        json={
            "area": 120,
            "rooms": 8,
            "age": 5
        }
    )

    assert response.status_code == 422






def test_predict_invalid_age(client):

    response = client.post(
        "/predict",
        json={
            "area": 120,
            "rooms": 3,
            "age": 20
        }
    )

    assert response.status_code == 422








@pytest.fixture(scope="function")
def sample_number():

    print("Fixture Started")

    yield 100

    print("Fixture Finished")

def test_sample_number(sample_number):
    assert sample_number == 100


def test_sample_number_again(sample_number):

    assert sample_number == 100



