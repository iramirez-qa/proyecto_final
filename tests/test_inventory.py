from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import logger
import pytest
import pytest_check as check

# Verificar que el título de la página de inventario sea correcto
@pytest.mark.smoke
def test_inventory_title(driver_logged):
    logger.info("Verificando titulo de página")
    title = driver_logged.title
    #assert title == "Swag Labs", "El título de la página es incorrecto"
    check.equal(title, "Swag Labs", "El título de la página es incorrecto")

# Comprobar que existan productos visibles en la página
@pytest.mark.smoke
def test_visible_products(driver_logged):
    logger.info("Verificando productos visibles")
    products = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    #assert len(products) > 0, "No hay productos visibles en el inventario"
    check.greater(len(products), 0, "No hay productos visibles en el inventario")

# Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
@pytest.mark.smoke
def test_ui_elements(driver_logged):
    logger.info("Verificando presencia de botón de menú ")
    menu = driver_logged.find_element(By.ID,"react-burger-menu-btn")
    filter = driver_logged.find_element(By.CLASS_NAME,"product_sort_container")
    #assert menu.is_displayed(), "El botón de menú no se encuentra visible en el inventario"
    #assert filter.is_displayed(), "El filtro no se encuentra visible en el inventario"
    check.is_true(menu.is_displayed(), "El botón de menú no se encuentra visible en el inventario")
    check.is_true(filter.is_displayed(), "El filtro no se encuentra visible en el inventario")