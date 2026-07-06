from behave import given,when,then
import requests

headers = {
    "x-api-key" : "free_user_3G66M3gy9PIE3lygVlbpqI7XJ0f"
}

@given("La API de Reqres esta disponible")
def step_impl(context):
    context.base_url = "https://reqres.in/api"

# Escenario 1
@when("realizar un login valido")
def step_impl(context):
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslickat"
    }

    context.response = requests.post(
        f"{context.base_url}/login",
        headers=headers,
        json=body
    )

@then("el status code debe ser {status_code:d}")
def step_impl(context,status_code):
    print(f"status:{context.response.status_code}")
    assert context.response.status_code == status_code

# Escenario 2
@when("realizar un login sin contraseña")
def step_impl(context):
    body = {
        "email": "eve.holt@reqres.in",
    }

    context.response = requests.post(
        f"{context.base_url}/login",
        headers=headers,
        json=body
    )

@then("el mensaje de error debe ser '{mensaje}'")
def step_impl(context, mensaje):
    body = context.response.json()

    assert body["error"] == mensaje