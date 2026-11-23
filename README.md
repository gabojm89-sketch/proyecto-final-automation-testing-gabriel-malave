# Automatización QA - SauceDemo y API

Este proyecto contiene la suite de pruebas automatizadas de interfaz de usuario (UI) y API para la plataforma de comercio electrónico **SauceDemo**, desarrollada en Python con Pytest, Selenium WebDriver y Page Object Model (POM) para el curso de Automation Testing.

## Propósito del Proyecto

El objetivo es validar de forma automatizada los flujos principales de la aplicación SauceDemo y los endpoints de API, asegurando que las funcionalidades críticas operen correctamente:
- Autenticación y control de acceso (login exitoso, escenarios negativos, campos vacíos y usuario bloqueado).
- Visualización y navegación del catálogo de productos (interfaz y validación contra datos JSON).
- Interacción con el carrito de compras (agregar productos, contadores y detalle de ítems).
- Validación de operaciones de API (`GET`, `POST`, `DELETE` y respuesta `404`).

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Framework de Pruebas:** Pytest y `pytest-check`
- **Automatización Web:** Selenium WebDriver (Page Object Model)
- **Pruebas de API:** `requests`
- **Generación de reportes:** `pytest-html`
- **Control de versiones:** Git y GitHub

## Estructura del Proyecto

```text
proyecto-final-automation-testing-gabriel-malave/
├── data/                # Archivos de datos de prueba (CSV / JSON)
├── features/            # Escenarios / especificaciones
├── logs/                # Logs de ejecución
├── pages/               # Page Object Model (POM)
├── reports/
│   ├── screenshots/     # Capturas de pantalla ante fallos
│   └── report.html      # Reporte HTML autocontenido
├── tests/
│   ├── test_login.py    # Casos de prueba de autenticación (1 - 4)
│   ├── test_inventory.py# Casos de prueba de catálogo / inventario (5 - 9)
│   ├── test_cart.py     # Casos de prueba del carrito de compras (10 - 11)
│   └── test_api.py      # Casos de prueba de API (12 - 13)
├── utils/               # Utilidades y funciones auxiliares
├── conftest.py          # Configuración global de fixtures de Pytest
├── pytest.ini           # Configuración global de Pytest
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto