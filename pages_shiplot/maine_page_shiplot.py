from time import sleep

from playwright.sync_api import expect

from pages.base_page import BasePage



class MainPage_Shiplot(BasePage):
    def __init__(self, page):
        super().__init__(page)

    MENU_SERVICES = "//a[@class='header__menu-link'][normalize-space()='Services']"
    MENU_TOOLS = "xpath=//li[@class='header__menu-item header__menu-item--tools']/a[1]"
    TOOLS_MENU_TAB = "#tools-dropDown"
    FREIGHT_CALCULATOR_EX = "//a[normalize-space()='Freight Calculator']"
    CARGO_TRACKING_EX = "//a[normalize-space()='Cargo tracking']"
    SHIPPING_SCHEDULES_EX = "//a[normalize-space()='Shipping schedules']"
    STAFFING_CALCULATOR_EX = "//a[normalize-space()='Stuffing Calculator']"
    LOGISTICS_MAP_EX = "//a[normalize-space()='Logistics Map']"
    DISTANCE_AND_TIME_EX = "//a[normalize-space()='Distance & time']"
    CO2_CALCULATOR_EX = "//a[normalize-space()='CO2 Calculator']"
    AI_ASSISTANT_EX = "//a[normalize-space()='AI Assistant']"
    ABOUT_HEADER_EX = "//a[@class='header__menu-link'][normalize-space()='About']"
    CONTACT_HEADER_EX = "//a[@class='header__menu-link'][normalize-space()='Contact']"
    SIGN_IN_EX = "//div[@id='navigator-root']"


    def go_to_services_page_ex(self):
        sleep(3)
        self.page.locator(self.MENU_SERVICES).click()
        expect(
            self.page.get_by_text(" a dedicated container for your cargo, offering maximum speed, "
                                  "security, and cost efficiency for larger shipments.")
        ).to_be_visible(timeout=30000)

    def hover_menu_tools_ex(self):
        sleep(2)
        page = self.page
        tools = page.locator(self.MENU_TOOLS)
        expect(tools).to_be_visible(timeout=10000)
        tools.hover()
        expect(self.page.locator(self.TOOLS_MENU_TAB).first).to_be_visible(timeout=100000)

    def go_to_freight_calculator_app_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.FREIGHT_CALCULATOR_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")

        expect(self.page.locator("h1")).to_contain_text("Logistics Explorer", timeout=30000)

    def go_to_cargo_tracking_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.CARGO_TRACKING_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")

        expect(self.page.locator("h3")).to_contain_text("Tracking starts here", timeout=30000)

    def go_to_shipping_schedules_page_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.SHIPPING_SCHEDULES_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("h2")).to_contain_text("Check vessel schedules online", timeout=30000)

    def go_to_staffing_calculator_page_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.STAFFING_CALCULATOR_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(".load-calculator-xSFglw").first).to_contain_text("Products", timeout=30000)

    def go_to_logistics_map_page_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.LOGISTICS_MAP_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("h3").first).to_contain_text("There are no cargoes yet", timeout=30000)

    def go_to_distance_and_time_page_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.DISTANCE_AND_TIME_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("._2d-nVx49nxs9UO9woqq19k").first).to_contain_text("transportation by", timeout=30000)

    def go_to_co2_calculator_page_ex(self):
        self.hover_menu_tools_ex()
        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.CO2_CALCULATOR_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(".k6IM0Y").first).to_contain_text("Carbon Emissions Calculator", timeout=30000)

    def go_to_ai_assistant_page_ex(self):
        self.hover_menu_tools_ex()

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.AI_ASSISTANT_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(".k6IM0Y").first).to_contain_text("Carbon Emissions Calculator", timeout=30000)

    def go_to_about_page_ex(self):

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.ABOUT_HEADER_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("h2").first).to_contain_text("Who We Are", timeout=30000)

    def go_to_contact_page_ex(self):

        with self.page.expect_popup() as new_page_info:
            self.page.locator(self.CONTACT_HEADER_EX).click()

        self.page = new_page_info.value
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("h2").first).to_contain_text("Contact Information", timeout=30000)

    def go_to_sign_in_ex(self):
        sleep(2)
        self.page.locator(self.SIGN_IN_EX).click()
        expect(self.page.locator("h4").first).to_contain_text("Welcome!", timeout=30000)

    def go_to_services_through_footer_ex(self):
        footer = self.page.locator("footer")
        footer.scroll_into_view_if_needed()
        expect(footer).to_be_visible()
        self.page.locator("//footer//a[normalize-space()='Services']").click()
        expect(
            self.page.get_by_text(" a dedicated container for your cargo, offering maximum speed, "
                                  "security, and cost efficiency for larger shipments.")
        ).to_be_visible(timeout=30000)

    def go_to_about_through_footer_ex(self):
        footer = self.page.locator("footer")
        footer.scroll_into_view_if_needed()
        expect(footer).to_be_visible()
        self.page.locator("//footer//a[normalize-space()='About']").click()
        expect(
            self.page.get_by_text(" At FreightCompany, we are more than just a logistics provider – "
                                  "we are problem solvers, innovators, and customer-focused professionals committed")
        ).to_be_visible(timeout=30000)

    def go_to_contact_through_footer_ex(self):
        footer = self.page.locator("footer")
        footer.scroll_into_view_if_needed()
        expect(footer).to_be_visible()
        self.page.locator("//footer//a[normalize-space()='Contact']").click()
        expect(self.page.locator("h2").first).to_contain_text("Contact Information", timeout=30000)