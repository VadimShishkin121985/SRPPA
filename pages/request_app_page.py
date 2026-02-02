import random
import string
from time import sleep
from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from playwright.sync_api import expect

from pages.main_page import MainPage


class RequestAQuote(LocatorsPage, BasePage):
    def __init__(self, page):
        super().__init__(page)

    def go_to_request_app(self):
        """Переход в Request A Quote через меню Services"""
        page = self.page

        # 1) Сброс возможных активных меню
        page.keyboard.press("Escape")
        page.click("body", position={"x": 5, "y": 5})

        # 2) Наводимся на Services
        services = page.locator(self.MENU_SERVICES)
        expect(services).to_be_visible()
        services.hover()

        # 3) Ждём появления пункта (это и есть признак открытого dropdown)
        request_item = page.locator(self.REQUEST_A_QUOTE_MENU)
        request_item.wait_for(state="visible", timeout=10000)
        request_item.scroll_into_view_if_needed()

        # 4) Кликаем безопасно (без force)
        self._safe_click(self.REQUEST_A_QUOTE_MENU)

        # 5) Ждём, что приложение реально открылось
        page.locator(self.REQUEST_APP).wait_for(state="visible", timeout=15000)

    def send_default_request(self):
        """Отправка стандартного запроса с заполнением всех полей"""

        # HS Code
        self.page.click(self.HS_CODE_REQUEST)
        self.page.keyboard.type("090611")  # вместо fill
        self.page.locator(".cg_b7", has_text="090611").first.click()

        # Вес
        self.page.fill("#cargoWeight", "5")

        # Откуда
        self.page.fill("#autocomplete_from", "65000")
        self.page.locator(".w3zuf").first.click()
        self.page.locator(".WOajJ").first.click()

        # Куда
        self.page.fill("#autocomplete_to", "mumbai")
        self.page.locator(".w3zuf").first.click()
        self.page.locator(".WbWAn", has_text="Mumbai, India").first.click()

        # Zip Code
        self.page.fill("#zipCodeFrom", "65000")
        self.page.fill("#zipCodeTo", "400001")

        # Ready to load
        self.page.locator(".KLr4P").click()

        # Даты
        expect(self.page.locator(".Calendar__day.-today[aria-disabled='false']")).to_be_visible()
        self.page.locator(".Calendar__day.-today[aria-disabled='false']").click()
        self.page.locator(".Calendar__day.-weekend[aria-disabled='false']").first.click()

        # Additional information
        self.page.fill(".textarea__element", "Test")

        # Отправка запроса
        self.page.locator(".PfDxg", has_text="Send").first.click()

        # Ждём подтверждения
        expect(self.page.locator(".cJg5n")).to_be_visible(timeout=50000)