from time import sleep

from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from pages.sign_in_page import SignInPage


class MainPage(BasePage, LocatorsPage):
    def __init__(self, page):
        super().__init__(page)

    def set_cn_in_filter(self, text):
        sleep(2)
        self.page.keyboard.type(text)

    def click_on_sign_in_button(self):
        self.page.screenshot(path="debug.png")
        self.page.locator(self.SIGN_IN).wait_for(state="visible", timeout=30000)
        self.page.locator(self.SIGN_IN).click()

    def go_to_container_tracking_app(self):
        self.page.hover(self.MENU_TOOLS)

        # Ждем пока пункт появится
        container_tracking = self.page.locator(self.CONTAINER_TRACKING_MENU)
        container_tracking.wait_for(state="visible", timeout=10000)

        # Кликаем принудительно
        container_tracking.click(force=True)

        # Ждем загрузку приложения
        self.page.wait_for_selector(
            self.CONTAINER_TRACKING_APP,
            state="visible",
            timeout=15000
        )

    def go_to_ct_app_with_aut(self):
        self.click_on_sign_in_button()
        SignInPage(self.page).sign_in_form()
        self.go_to_container_tracking_app()