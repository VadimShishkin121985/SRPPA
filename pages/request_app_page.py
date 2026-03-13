from time import sleep
import os
import re
from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from playwright.sync_api import expect




class RequestAQuote(LocatorsPage, BasePage):
    def __init__(self, page):
        super().__init__(page)

    def go_to_request_app(self):
        page = self.page

        # Закрываем оверлеи
        page.keyboard.press("Escape")
        page.click("body", position={"x": 5, "y": 5})

        # Открываем Services
        services = page.locator(self.MENU_SERVICES)
        expect(services).to_be_visible()
        services.hover()

        # Ждём, что services dropdown появился
        page.locator(self.SERVICES_DROPDOWN).wait_for(state="visible", timeout=10000)

        # 🔥 Если references активен и перекрывает — закрываем/снимаем
        ref_active = page.locator(self.REFERENCES_ACTIVE_SECTION)
        if ref_active.count() > 0:
            # Самый надёжный способ "снять" — выйти мышью и заново hover
            page.mouse.move(1, 1)
            page.keyboard.press("Escape")
            services.hover()
            page.locator(self.SERVICES_DROPDOWN).wait_for(state="visible", timeout=10000)

        # Клик по пункту
        self._safe_click(self.REQUEST_A_QUOTE_MENU, timeout=30000)

    def send_default_request(self):
        """Отправка стандартного запроса и сохранение номера request"""

        # HS Code
        self.page.click(self.HS_CODE_REQUEST)
        self.page.keyboard.type("090611")
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

        # Send
        self.page.locator(".PfDxg", has_text="Send").first.click()

        # Ждём заголовок
        request_title = self.page.locator("h2", has_text="Request")
        expect(request_title).to_be_visible(timeout=50000)

        request_text = request_title.inner_text().strip()

        match = re.search(r"\d+", request_text)
        if not match:
            raise AssertionError(f"Request number not found in text: {request_text}")

        request_number = match.group()

        os.makedirs("reports", exist_ok=True)
        with open("reports/created_requests.txt", "a", encoding="utf-8") as f:
            f.write(f"{request_number}\n")

        print(f"Request created: {request_number}")

        return request_number


    def request_it_quote(self):
        """Создание IT Quote с сохранением номера реквеста в отдельный файл"""

        # выбор тулзы
        expect(self.page.locator("input[aria-label='toolInfo.tool']")).to_be_visible()
        self.page.locator("input[aria-label='toolInfo.tool']").click()
        self.page.get_by_label("select-body").get_by_text("Container Tracking", exact=True).click()

        # выбор типа реквеста
        self.page.locator("input[aria-label='toolInfo.requestType']").click()
        self.page.get_by_label("select-body").get_by_text("API", exact=True).click()

        # количество реквестов
        self.page.fill("input.request-it-quote-coERK4[type='number'][placeholder='0']", "1000")
        self.page.locator("input.request-it-quote-coERK4[type='number'][placeholder='0']").nth(1).fill("1000")

        # параметр запроса
        self.page.get_by_text("Container number", exact=True).click()
        self.page.fill(".request-it-quote-INW0I3", "test")

        # отправка
        self.page.get_by_role("button", name="Send").click()

        # ждём успех
        expect(self.page.get_by_role("button", name="Go to main page")).to_be_visible(timeout=50000)

        # ждём заголовок с номером IT request
        request_title = self.page.locator("h1.request-it-quote-gQVYW8")
        expect(request_title).to_be_visible(timeout=50000)

        request_text = request_title.inner_text().strip()
        # например: "Request № 432679"

        match = re.search(r"\d+", request_text)
        if not match:
            raise AssertionError(f"Не удалось найти IT request number в тексте: {request_text}")

        request_number = match.group()

        # создаём папку reports если её нет
        os.makedirs("reports", exist_ok=True)

        # сохраняем в отдельный файл
        with open("reports/created_it_requests.txt", "a", encoding="utf-8") as f:
            f.write(f"{request_number}\n")

        print(f"Request IT created: {request_number}")

        return request_number
