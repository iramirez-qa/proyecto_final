from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

# Verificar que el título de la página de inventario sea correcto
def test_inventory_title(driver_logged):
    title = driver_logged.title
    assert title == "Swag Labs", "El título de la página es incorrecto"

# Comprobar que existan productos visibles en la página
def test_visible_products(driver_logged):
    products = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(products) > 0, "No hay productos visibles en el inventario"

# Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID,"react-burger-menu-btn")
    filter = driver_logged.find_element(By.CLASS_NAME,"product_sort_container")
    assert menu.is_displayed(), "El botón de menú no se encuentra visible en el inventario"
    assert filter.is_displayed(), "El filtro no se encuentra visible en el inventario"