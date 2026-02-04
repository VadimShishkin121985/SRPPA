from time import sleep

from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from pages.sign_in_page import SignInPage
from playwright.sync_api import expect

class MainPage(BasePage, LocatorsPage):
    def __init__(self, page):
        super().__init__(page)

    def set_cn_in_filter(self, text):
        assert text is not None, "Tracking number is None"
        self.page.keyboard.type(str(text))

    def click_on_sign_in_button(self):
        self.page.screenshot(path="debug.png")
        self.page.locator(self.SIGN_IN).wait_for(state="visible", timeout=30000)
        self.page.locator(self.SIGN_IN).click()

    def go_to_container_tracking_app(self):
        """Переход в Container Tracking через меню Tools"""
        page = self.page

        # 1) Сброс возможных активных меню/оверлеев
        page.keyboard.press("Escape")
        page.mouse.move(1, 1)
        page.locator("body").click(position={"x": 5, "y": 5})

        # 2) Открываем Tools
        tools = page.locator(self.MENU_TOOLS)
        expect(tools).to_be_visible()
        tools.hover()

        # 3) Ждём появления пункта Container Tracking
        item = page.locator(self.CONTAINER_TRACKING_MENU)
        item.wait_for(state="visible", timeout=10000)
        item.scroll_into_view_if_needed()

        # 4) Кликаем безопасно (без force)
        self._safe_click(self.CONTAINER_TRACKING_MENU, timeout=30000)

        # 5) Ждём, что приложение загрузилось
        page.locator(self.CONTAINER_TRACKING_APP).wait_for(state="visible", timeout=15000)

    def go_to_ct_app_with_aut(self):
        self.click_on_sign_in_button()
        SignInPage(self.page).sign_in_form()
        self.go_to_container_tracking_app()