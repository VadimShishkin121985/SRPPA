from time import sleep

import pytest

from pages.container_tracking_page import ContainerTracking
from pages.main_page import MainPage
from pages.sign_in_page import SignIn


@pytest.mark.usefixtures("setup_class_page")

class Test_Tracking:
    page = None

    @pytest.fixture(autouse=True)
    def _setup_page(self, page):
        self.page = page

    @property
    def main_page(self):
        if not hasattr(self, "_main_page"):
            self._main_page = MainPage(self.page)
        return self._main_page

    @property
    def sign_in_page(self):
        if not hasattr(self, "_sign_in_page"):
            self._sign_in_page = SignIn(self.page)
        return self._sign_in_page

    @property
    def container_tracking_page(self):
        if not hasattr(self, "_container_tracking_page"):
            self._container_tracking_page = ContainerTracking(self.page)
        return self._container_tracking_page

    def test_sign_in(self):
        self.main_page.click_on_sign_in_button()
        self.sign_in_page.sign_in_form()

    def test_go_to_ct_app(self):
        # используем self.page через fixture, не передаём в тест
        self.test_sign_in()  # теперь без аргумента
        self.main_page.go_to_container_tracking_app()

    def test_go_to_ct_from_filter_303169537(self):
        # используем self.page из fixture
        main_page = MainPage(self.page)

        from time import sleep
        sleep(2)

        main_page.press_tab(3, True)
        main_page.set_cn_in_filter(main_page.get_random_tracking_number())
        main_page.press_tab(2, False)

        sleep(2)
        # self.page вместо page
        assert self.page.wait_for_selector(".app-root-unified_tracking", state="visible", timeout=10000)

    def test_the_update_button_in_the_list_264863760(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.update_button_click()

    def test_saving_number_265191426(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.fill_input_ct_number()
        self.container_tracking_page.click_search_button_ct_app()
        self.container_tracking_page.click_on_follow_button()

    def test_remove_a_card_inside_a_card_266174465(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_the_updated_card()
        self.container_tracking_page.delete_the_card()

    def test_delete_the_card_from_the_list_265814035(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.delete_the_card()

    def test_view_rates(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_the_first_card()
        self.container_tracking_page.click_on_the_rate()

    def test_download_template_(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.download_file()

    def test_upload_file(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.upload_test_file()

    def test_add_delete_tag(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_the_first_card()
        self.container_tracking_page.add_first_tag()

    def test_copy_link(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_the_first_card()
        self.container_tracking_page.copy_past_link()

    def test_map_setting(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.setting_map()

    def test_info_tab_in_the_card(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_the_first_card()
        self.container_tracking_page.go_to_vessel_tab()
        self.container_tracking_page.go_to_route_tab()

    def test_open_the_card_through_a_point_on_the_map(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.click_on_the_point()
        self.container_tracking_page.hover_and_click_on_container_in_point()

    def test_checking_the_limit_for_unauthorized_user(self):
        self.main_page.go_to_container_tracking_app()
        self.container_tracking_page.fill_input_ct_number()
        self.container_tracking_page.search_button_ct_app_limiter()

    def test_checking_limit_for_paid_user(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_subscription_info()
        self.container_tracking_page.check_credit_counter()

    def test_extend_subscription(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.open_subscription_info()
        self.container_tracking_page.purchase_additional_credits()

    def test_main_tabs(self):
        self.test_go_to_ct_app(self.page)
        self.container_tracking_page.go_to_analytics_tab()
        self.container_tracking_page.go_to_notifications_tab()
        self.container_tracking_page.go_to_calendar_tab()
        self.container_tracking_page.go_to_map_tab()


















