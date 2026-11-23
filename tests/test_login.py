from pages.login_page import LoginPage
import pytest
from utils.reader import read_users_csv
from utils.logger import logger


@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver, data):
    try:
        logger.info(f"Iniciando prueba de login para usuario: {data['usuario']}")
        login_page = LoginPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina abierta correctamente")

        login_page.login(data["usuario"], data["password"])
        logger.info("Ingreso de credenciales completado")

        if data["tipo_usuario"] == "True":
            assert "/inventory.html" in driver.current_url
            logger.info("Login exitoso: redireccion a inventario verificada")
        elif data["tipo_usuario"] == "False":
            error = login_page.obtener_mensaje_error()
            assert error and "Epic sadface" in error
            logger.info(f"Prueba de mensaje de error valida: {error}")
        else:
            raise AssertionError(f"Valor de tipo_usuario no soportado en CSV: {data['tipo_usuario']}")
    except Exception:
        logger.exception("Error durante la prueba de login")
        raise


def test_login_campos_vacios(driver):
    try:
        logger.info("Iniciando prueba de login con campos vacios")
        login_page = LoginPage(driver)

        driver.get("https://www.saucedemo.com/")
        login_page.login("", "")

        error = login_page.obtener_mensaje_error()
        assert "Epic sadface: Username is required" in error
        logger.info("Validacion de campos vacios exitosa")
    except Exception:
        logger.exception("Error en prueba de login con campos vacios")
        raise


def test_login_usuario_bloqueado(driver):
    try:
        logger.info("Iniciando prueba de login con usuario bloqueado")
        login_page = LoginPage(driver)

        driver.get("https://www.saucedemo.com/")
        login_page.login("locked_out_user", "secret_sauce")

        error = login_page.obtener_mensaje_error()
        assert "Sorry, this user has been locked out" in error
        logger.info("Validacion de usuario bloqueado exitosa")
    except Exception:
        logger.exception("Error en prueba de login con usuario bloqueado")
        raise