from time import sleep

from pages.base_page import BasePage
from pages.locator_page import LocatorsPage


class MainPage(BasePage, LocatorsPage):
    def __init__(self, page):
        super().__init__(page)

    def set_cn_in_filter(self, text):
        sleep(2)
        self.page.keyboard.type(text)

    def click_on_sign_in_button(self):
        self.page.click(self.SIGN_IN)

    def go_to_container_tracking_app(self):
        self.page.hover(self.MENU_TOOLS)
        self.page.click(self.CONTAINER_TRACKING_MENU)
        self.page.wait_for_selector(self.CONTAINER_TRACKING_APP, state="visible")