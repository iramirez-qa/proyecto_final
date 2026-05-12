from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def get_product_name(driver_logged):
    return driver_logged.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

def test_cart(driver_logged):

    #Obtengo nombre del producto
    product_name = get_product_name(driver_logged)

    # Añadir el producto al carrito haciendo clic en el botón correspondiente
    driver_logged.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # Verificar que el contador del carrito se incremente correctamente
    cart_counter = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_counter.text == "1", "El producto no se agrego correctamente"
    
    # Navegar al carrito de compras
    driver_logged.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "/cart.html" in driver_logged.current_url, "No se redirigió al carrito"

    # Comprobar que el producto añadido aparezca correctamente en el carrito
    cart_item = driver_logged.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item == product_name, "El producto en el carrito no coincide con el agregado"