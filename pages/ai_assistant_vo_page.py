from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from playwright.sync_api import expect




class AIAssistant(LocatorsPage, BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_ct_default_question(self):
        btn = self.page.locator(self.CT_QUICK_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(
            self.page.get_by_text("Please provide a valid container number for tracking. "
                                  "Container numbers are typically 10-11 characters like MSCU1234567. "
                                  "You can track containers at")
        ).to_be_visible(timeout=30000)

    def check_dt_default_question(self):
        btn = self.page.locator(self.DT_QUICK_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(
            self.page.get_by_text("Please provide the origin and destination (cities/ports),"
                                  " e.g. 'distance from New York to London'.")
        ).to_be_visible(timeout=30000)


    def check_le_default_question(self):
        btn = self.page.locator(self.LE_QUICK_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(
            self.page.get_by_text("Please provide the origin and destination (cities/ports),"
                                  " e.g. 'freight rate from Shanghai to Hamburg'.")
        ).to_be_visible(timeout=30000)

    def check_co2_default_question(self):
        btn = self.page.locator(self.CO2_QUICK_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(
            self.page.get_by_text("To calculate CO2 emissions, I need the origin and destination coordinates,"
                                  " transport mode, and either container type or cargo weight."
                                  " Please provide these details.")
        ).to_be_visible(timeout=30000)

    def check_ss_default_question(self):
        btn = self.page.locator(self.SS_QUICK_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(
            self.page.get_by_text("The schedule for a vessel can be checked on SeaRates by going to the "
                                  "TOOLS tab and selecting the Ship Schedules tool, where you can choose the "
                                  "location of departure and arrival, as well as the departure date, "
                                  "and other parameters for your request.")
        ).to_be_visible(timeout=30000)

    def check_fi_default_question(self):
        btn = self.page.locator(self.FI_QUICK_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(
            self.page.get_by_text("To show freight index data, I need the origin and destination ports/cities."
                                  " Please specify the route for market analysis.")
        ).to_be_visible(timeout=30000)

    def go_to_new_chat(self):
        btn = self.page.locator(self.NEW_CHAT_BUTTON)
        expect(btn).to_be_visible(timeout=30000)
        btn.click()
        expect(self.page.locator(self.FI_QUICK_BUTTON)).to_be_visible(timeout=30000)


