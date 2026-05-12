# Proyecto de automatización QA - Ignacio Ramírez

## Descripción

Proyecto de automatización de pruebas realizado con Python, Selenium WebDriver y Pytest

El objetivo del proyecto es automatizar distintas pruebas funcionales de una aplicación web

## Tecnologias usadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git

## Instalación de dependencias
A continuación se detalla la forma de instalar las distintas dependencias:
- Python: descargar el ejecutable desde https://www.python.org/downloads/
- Selenium WebDriver: ejecutar en terminal de VS Code "pip install selenium"
- Pytest: ejecutar en terminal de VS Code "pip install pytest"
- Pytest HTML: ejecutar en terminal de VS Code "pip install pytest-html"
- Git: descargar el ejecutable desde https://git-scm.com/

## Instalacion

git init
git commit -m "v1.0"
git branch -M main
git remote add origin https://github.com/iramirez-qa/pre-entrega.git
git push -u origin main

## Descripción de los elementos

### conftest.py
Archivo de configuración global de los test. Deja preestablecidos los siguientes parámetros:
- Navegador utilizado: Google Chrome
- El navegador siempre se abre en modo incógnito

### utils > LoginPage.py
Archivo en donde se define el paso a paso del login para luego reutilizarlo en los distintos tests a ejecutar:
1. Ingresa a la url "https://www.saucedemo.com/"
2. Ingresa el usuario "standard_user"
3. Ingresa la contraseña "secret_sauce"
4. Realiza click en login

### tests > test_login.py
Test en donde se realizan las siguientes acciones y verificaciones:
- Utiliza el driver definido en LoginPage.py para iniciar sesión
- Verifica el correcto logueo comprobando que la url contenga el string "/inventory.html"

### tests > test_inventory.py
Test en donde se realizan las siguientes acciones y verificaciones:
- Utiliza el driver definido en LoginPage.py para iniciar sesión
- Verifica el título de la página
- Verifica que haya productos visibles en el inventario
- Verifica que este visible el ícono de menu tipo "hamburguesa"
- Verifica que este visible el ícono de filtro

### tests > test_cart.py
Test en donde se realizan las siguientes acciones y verificaciones:
- Utiliza el driver definido en LoginPage.py para iniciar sesión
- Obtiene el nombre del primer producto visible en el inventario
- Añade el primer producto visible al carrito
- Verifica en un mismo test:
1. Que el contador del carrito muestre el valor "1"
2. Realiza click en el botón del carrito - Verifica la correcta redirección comprobando que la url contenga el string "/cart.html"
3. Verifica que el producto añadido al carrito sea el correcto, comparando el nombre del item con el nombre obtenido del primer producto visible en el inventario

## Descripción de comandos de ejecución
Durante la ejecución de las pruebas automatizadas se utilizaran los siguientes parámetros:
- "py": lanzador del ejecutable de python
- "-m pytest": ejecuta el módulo "pytest", el cual busca los archivos que comiencen su nombre con "test_" y ejecuta las funciones contenidas por los mismos
- "-v": muestra nombre y resultado completo de cada prueba
- "--html=name.html": realiza un reporte html (con el nombre indicado en el comando) con el detalle de las pruebas ejecutadas

## Comandos de ejecución a utilizar
A continuación se detallan los string a utilizar en la terminal para ejecutar los test y obtener el reporte de ejecución al finalizar los mismos:
- LOGIN: "py -m pytest -v tests/test_login.py --html=login.html"
- INVENTARIO:"py -m pytest -v tests/test_inventory.py --html=inventory.html"
- CARRITO: "py -m pytest -v tests/test_cart.py --html=cart.html"