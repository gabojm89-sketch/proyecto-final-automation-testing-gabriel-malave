from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_productos_json
from utils.logger import logger


def test_cart(driver):
    try:
        logger.info("Inicializando la prueba de carrito")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        logger.info("Ingresando a la pagina web de prueba")
        driver.get("https://www.saucedemo.com/")

        logger.info("Iniciando sesion con credenciales validas")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Sesion iniciada correctamente")

        logger.info("Leyendo el primer producto del JSON")
        productos = read_productos_json()
        producto = productos[0]
        print(producto)

        logger.info("Agregando producto del JSON al carrito")
        inventory_page.agregar_producto(producto["nombre"])

        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Prueba de contador de carrito validada")

        logger.info("Ir a la pagina del carrito")
        inventory_page.ir_al_carrito()

        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        logger.info("Prueba del nombre del producto en carrito contra JSON validada")

        assert cart_page.obtener_precio_producto() == producto["precio"]
        logger.info("Prueba del precio del producto en carrito contra JSON validada")
    except Exception:
        logger.exception("Error durante la prueba de carrito")
        raise


def test_agregar_multiples_productos_carrito(driver):
    try:
        logger.info("Iniciando prueba de multiples productos en carrito")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        productos = read_productos_json()
        assert len(productos) >= 2, "Se requieren al menos 2 productos en el JSON"

        inventory_page.agregar_producto(productos[0]["nombre"])
        inventory_page.agregar_producto(productos[1]["nombre"])

        assert inventory_page.obtener_contador_carrito() == "2"
        logger.info("Contador de carrito validado con 2 productos")
    except Exception:
        logger.exception("Error al agregar multiples productos al carrito")
        raise