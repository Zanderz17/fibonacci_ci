from fastapi.testclient import TestClient
from app import app
import time


client = TestClient(app)


def test_fibonacci_performance_average():
    number_of_requests = 10
    total_time = 0

    for _ in range(number_of_requests):
        start_time = time.time()
        response = client.get("/get_fibonacci/20")
        end_time = time.time()
        total_time += (end_time - start_time)
        assert response.status_code == 200
        assert response.json() is not None

    average_time = (total_time / number_of_requests) * 1000
    assert average_time <= 9.5, f"Average request time too long: {average_time}ms, exceeds 9.5ms"
