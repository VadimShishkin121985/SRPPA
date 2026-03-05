from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from playwright.sync_api import expect




class VirtualOffice(LocatorsPage, BasePage):
    def __init__(self, page):
        super().__init__(page)

    def go_to_ai_app(self):
        self.page.locator(self.AI_ASSISTANT).first.click()
        expect(self.page.locator(self.NEW_CHAT)).to_be_visible(timeout=30000)