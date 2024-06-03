from fastapi.testclient import TestClient
from app import app
import requests
import time

client = TestClient(app)


def test_fibonacci_success():
    response = client.get("/get_fibonacci/5")
    assert response.status_code == 200
    assert response.json() == 5


def test_fibonacci_negative():
    response = client.get("/get_fibonacci/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "El número debe ser un entero no negativo."}


def test_fibonacci_one():
    response = client.get("/get_fibonacci/1")
    assert response.status_code == 200
    assert response.json() == 1


def test_fibonacci_twenty():
    response = client.get("/get_fibonacci/20")
    assert response.status_code == 200
    assert response.json() == 6765


def test_fibonacci_invalid_input():
    response = client.get("/get_fibonacci/abc")
    assert response.status_code == 422


def test_fibonacci_performance_average():
    url = "http://127.0.0.1:8000/get_fibonacci/20"
    number_of_requests = 20
    total_time = 0

    for _ in range(number_of_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        total_time += (end_time - start_time)
        assert response.status_code == 200
        assert response.json() is not None

    average_time = (total_time / number_of_requests) * 1000
    assert average_time <= 3.5, f"Average request time too long: {average_time}ms, exceeds 3.5ms"
