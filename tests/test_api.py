import requests
import pytest_check as check
from utils.logger import logger
import pytest

headers = {
    "x-api-key": "free_user_3G66M3gy9PIE3lygVlbpqI7XJ0f"
}

@pytest.mark.api
@pytest.mark.smoke
def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    #assert response.status_code == 200
    check.equal(response.status_code,200)

@pytest.mark.api
def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    #assert response.status_code == 400
    #assert body["error"] == "Missing password"
    check.equal(response.status_code,400)
    check.equal(body["error"],"Missing password")


@pytest.mark.api
def test_create_user():
    body = {
        "name": "Ignacio",
        "email": "ignacio.ramirez@emailtest.com",
        "password": "1335555777777"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers,json=body)

    data = response.json()

    print(data)

    #assert response.status_code == 201
    check.equal(response.status_code,201)
    #assert data["name"] == body["name"]
    #assert data["email"] == body["email"]
    #print(response.elapsed.total_seconds())
    #assert response.elapsed.total_seconds() < 1
    check.equal(data["name"], body["name"], "El nombre no coincide")
    check.equal(data["email"], body["email"], "El email no coincide")
    print(response.elapsed.total_seconds())
    check.less(response.elapsed.total_seconds(), 1, "El tiempo de respuesta es igual o mayor a 1 segundo")

@pytest.mark.api
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    #assert response.status_code == 204
    check.equal(response.status_code,204)

@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    #assert response.status_code == 200
    check.equal(response.status_code,200)
    print(response.elapsed.total_seconds())
    #assert response.elapsed.total_seconds() < 1
    check.less(response.elapsed.total_seconds(), 1, "El tiempo de respuesta es igual o mayor a 1 segundo")