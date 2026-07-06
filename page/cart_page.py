from selenium.webdriver.common.by import By

class CartPage:
    # Selectores como variables de clase limpias
    cart_items = (By.CLASS_NAME, "cart_item")
    cart_items_name = (By.CLASS_NAME, "inventory_item_name")
    cart_items_price = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def obtener_productos_carrito(self):
        items = self.driver.find_elements(*self.cart_items)
        productos = []

        for item in items:
            nombre_item = item.find_element(*self.cart_items_name).text
            precio_item = item.find_element(*self.cart_items_price).text

            productos.append(
                {
                    "name": nombre_item.strip(),
                    "precio": precio_item.strip()
                }
            )

        return productos