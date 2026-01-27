import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

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

@pytest.fixture(scope="function", autouse=True)
def setup_page(request):
    """
    Fixture для каждого теста:
    - открывает новый браузер и страницу перед тестом
    - закрывает браузер после теста
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        # Привязываем page к классу (request.cls) и к тесту (request.instance)
        if hasattr(request, "cls"):
            request.cls.page = page

        yield page  # тест получает page как аргумент

        # Закрываем контекст и браузер после теста
        context.close()
        browser.close()