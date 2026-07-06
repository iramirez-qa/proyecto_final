from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.logger import logger
import pytest
import pytest_check as check

from page.login_page import LoginPage

@pytest.mark.smoke
def test_login_ok(driver):
    logger.info("Inicializando el driver para test_login_ok")
    login_page = LoginPage(driver)

    logger.info("Ingresando los datos de entrada para la prueba positiva")
    login_page.login("standard_user","secret_sauce")

    logger.info("Iniciando sesion...")

    #assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    check.is_in("/inventory.html", driver.current_url, "No se redirigió al inventario")
    logger.info("Sesion iniciada correctamente")

@pytest.mark.smoke
def test_login_invalid_password(driver):
    logger.info("Inicializando el driver para test_login_invalid_password")
    login_page = LoginPage(driver)

    logger.info("Ingresando los datos de entrada para la prueba negativa")
    login_page.login("standard_user","123456")

    logger.info("Intento fallido de inicio de sesion...")

    error = login_page.get_error_password_message()

    #assert "Epic sadface: Username and password do not match any user in this service" in error
    check.is_in("Epic sadface: Username and password do not match any user in this service", error, "Error Password Message")
    logger.info("Sesion no iniciada, contraseña incorrecta")