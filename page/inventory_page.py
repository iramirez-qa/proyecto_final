from selenium.webdriver.common.by import By

class InventoryPage:
    inventory_items = (By.CLASS_NAME, "inventory_item")
    menu_button = (By.ID, "react-burger-menu-btn")
    filtro = (By.CLASS_NAME, "product_sort_container")
    add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
    contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
    link_carrito = (By.CLASS_NAME, "shopping_cart_link")
    nombres_productos = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def obtener_titulo(self):
        return self.driver.title

    def obtener_productos(self):
        return self.driver.find_elements(*self.inventory_items)

    def menu_visible(self):
        return self.driver.find_element(*self.menu_button).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self.filtro).is_displayed()
    
    def agregar_producto_por_nombre(self, nombre_producto):
        tarjetas_productos = self.driver.find_elements(*self.inventory_items)
        
        for tarjeta in tarjetas_productos:
            nombre_actual = tarjeta.find_element(*self.nombres_productos).text
            if nombre_actual.strip() == nombre_producto.strip():
                boton_agregar = tarjeta.find_element(*self.add_to_cart_buttons)
                boton_agregar.click()
                break

    def agregar_producto_al_carrito(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.contador_carrito).text
    
    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.nombres_productos)[0].text
    
    def ir_al_carrito(self):
        self.driver.find_element(*self.link_carrito).click()
