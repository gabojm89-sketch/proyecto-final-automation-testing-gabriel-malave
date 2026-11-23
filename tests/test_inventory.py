from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.reader import read_productos_json
from utils.logger import logger


def test_inventory(driver):
    try:
        logger.info("Inicializando la prueba de Inventario")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        logger.info("Ingresando a la pagina web")
        driver.get("https://www.saucedemo.com/")

        logger.info("Ingresando credenciales para iniciar sesion")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Sesion iniciada correctamente")

        productos = inventory_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")

        assert len(productos) > 0
        logger.info("Prueba de cantidad de productos validada")

        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Prueba de integridad de la informacion de los productos validada")

        assert inventory_page.menu_visible()
        logger.info("Prueba de visibilidad del menu en la pagina validada")

        assert inventory_page.filtro_visible()
        logger.info("Prueba de visibilidad del filtro en la pagina validada")
    except Exception:
        logger.exception("Error durante la prueba de Inventario")
        raise


def test_verificar_catalogo_completo_y_json(driver):
    try:
        logger.info("Iniciando prueba de catalogo completo contra JSON")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        productos = inventory_page.obtener_productos()
        assert len(productos) == 6, f"Se esperaban 6 productos en catalogo, se encontraron {len(productos)}"
        logger.info("Cantidad total de productos en inventario (6) validada")

        producto_json = read_productos_json()[0]
        assert inventory_page.obtener_nombre_primer_producto() == producto_json["nombre"]
        assert inventory_page.obtener_precio_primer_producto() == f"${producto_json['precio']}"
        logger.info("Primer producto del inventario coincide con el archivo JSON")
    except Exception:
        logger.exception("Error al validar el catalogo completo contra JSON")
        raise