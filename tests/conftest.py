import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.searates.com/")
@pytest.fixture
def page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1700, "height": 1080},
            accept_downloads=True,
            permissions = ["clipboard-read", "clipboard-write"]
        )
        page = context.new_page()
        page.goto(BASE_URL)

        yield page

        context.close()
        browser.close()