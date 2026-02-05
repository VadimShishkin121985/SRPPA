from time import sleep

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
        expect(self.page.locator("#request_a_quote")).to_be_visible(timeout=50000)


    def request_it_quote(self):
        # выбор тулзы
        expect(self.page.locator("input[aria-label='toolInfo.tool']")).to_be_visible()
        self.page.locator("input[aria-label='toolInfo.tool']").click()
        self.page.get_by_label("select-body").get_by_text("Container Tracking", exact=True).click()
        # выбор типа реквеста
        self.page.locator("input[aria-label='toolInfo.requestType']").click()
        self.page.get_by_label("select-body").get_by_text("API", exact=True).click()
        #количество реквестов
        self.page.fill("input.request-it-quote-coERK4[type='number'][placeholder='0']", "1000")
        self.page.locator("input.request-it-quote-coERK4[type='number'][placeholder='0']").nth(1).fill("1000")

        self.page.get_by_text("Container number", exact=True).click()


        self.page.fill(".request-it-quote-INW0I3", "test")

        self.page.get_by_role("button", name="Send").click()

        expect(self.page.get_by_role("button", name="Go to main page")).to_be_visible(timeout=50000)


        pass
