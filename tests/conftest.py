import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.searates.com/")
# @pytest.fixture
# def page():
#     with sync_playwright() as pw:
#         browser = pw.chromium.launch(headless=True)
#         context = browser.new_context(
#             viewport={"width": 1700, "height": 1080},
#             accept_downloads=True,
#             permissions = ["clipboard-read", "clipboard-write"]
#         )
#         page = context.new_page()
#         page.goto(BASE_URL)
#
#         yield page
#
#         context.close()
#         browser.close()

import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.container_tracking_page import ContainerTrackingPage

BASE_URL = "https://www.searates.com/"  # замени на свой URL

# ----------------------------
# Фикстура чистой страницы
# ----------------------------
@pytest.fixture(scope="function")
def page():
    """
    Каждый тест:
    - стартует новый браузер
    - создаёт новый контекст
    - создаёт новую страницу
    - закрывает браузер после теста
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=[
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-blink-features=AutomationControlled"
            ]
        )

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            viewport={"width": 1920, "height": 1080},
            permissions = ["clipboard-read", "clipboard-write"]
        )
        page = context.new_page()

        page.goto(BASE_URL, wait_until="load", timeout=60000)

        yield page  # тест получает объект page

        # закрытие ресурсов после теста
        context.close()
        browser.close()

# ----------------------------
# Фикстура Page Objects
# ----------------------------
@pytest.fixture
def pages(page):
    """
    Возвращает словарь с готовыми Page Objects для теста.
    Пример использования:
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()
        pages["ct"].update_button_click()
    """
    return {
        "main": MainPage(page),
        "signin": SignInPage(page),
        "ct": ContainerTrackingPage(page)
    }
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Делает скриншот при падении теста
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_")

            file_path = f"screenshots/{test_name}_{timestamp}.png"
            page.screenshot(path=file_path, full_page=True)

            print("📸")