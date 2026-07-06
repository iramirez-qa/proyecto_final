from page.login_page import LoginPage
from utils.data_reader import read_users_csv
from utils.logger import logger
import pytest
import pytest_check as check

@pytest.mark.parametrize("user",read_users_csv())

@pytest.mark.smoke
def test_login(driver,user):
    logger.info("Inicializando el driver para test_login")
    login_page = LoginPage(driver)

    logger.info("Ingresando los datos de entrada para la prueba")
    login_page.login(user["username"],user["password"])
    if user["valid"] == "true":
        #assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        check.is_in("/inventory.html", driver.current_url, "No se redirigió al inventario")
    else:
        error = login_page.get_error_message()
        #assert "Epic sadface" in error
        check.is_in("Epic sadface", error)