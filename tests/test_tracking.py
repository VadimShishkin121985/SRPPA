import pytest
from time import sleep

from playwright.sync_api import expect

from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.container_tracking_page import ContainerTrackingPage

class Test_Tracking:

    def test_sign_in(self, pages):
        """
        Тест авторизации.
        """
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()

    def test_go_to_ct_app(self, pages):
        """
        Переход в Container Tracking.
        Логин выполняется в начале теста.
        """
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()
        pages["main"].go_to_container_tracking_app()

    def test_go_to_ct_from_filter(self, pages):
        """
        Переход в CT через фильтр.
        """
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()

        main_page = pages["main"]
        sleep(2)
        main_page.press_tab(3, True)
        main_page.set_cn_in_filter(main_page.get_random_tracking_number())
        main_page.press_tab(2, False)
        sleep(2)
        expect(pages["main"].page.locator(".app-root-unified_tracking")).to_be_visible(timeout=50000)


    def test_the_update_button_in_the_list(self, pages):
        """
        Нажатие кнопки обновления в списке.
        """
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].update_button_click()

    def test_saving_number(self, pages):
        """
        Сохранение номера в контейнерном приложении.
        """
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].fill_input_ct_number()
        pages["ct"].click_search_button_ct_app()
        pages["ct"].click_on_follow_button()

    def test_remove_a_card_inside_a_card(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_the_updated_card()
        pages["ct"].delete_the_card()

    def test_delete_the_card_from_the_list_265814035(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].delete_the_card()

    def test_view_rates(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_the_first_card()
        pages["ct"].click_on_the_rate()

    def test_download_template_(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].download_file()

    def test_upload_file(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].upload_test_file()

    def test_add_delete_tag(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_the_first_card()
        pages["ct"].add_first_tag()

    def test_copy_link(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_the_first_card()
        pages["ct"].copy_past_link()

    def test_map_setting(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].setting_map()

    def test_info_tab_in_the_card(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_the_first_card()
        pages["ct"].go_to_vessel_tab()
        pages["ct"].go_to_route_tab()

    def test_open_the_card_through_a_point_on_the_map(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].click_on_the_point()
        pages["ct"].hover_and_click_on_container_in_point()

    def test_checking_the_limit_for_unauthorized_user(self, pages):
        pages["main"].go_to_container_tracking_app()
        pages["ct"].fill_input_ct_number()
        pages["ct"].search_button_ct_app_limiter()

    def test_checking_limit_for_paid_user(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_subscription_info()
        pages["ct"].check_credit_counter()

    def test_extend_subscription(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].open_subscription_info()
        pages["ct"].purchase_additional_credits()

    def test_main_tabs(self, pages):
        pages["main"].go_to_ct_app_with_aut()
        pages["ct"].go_to_analytics_tab()
        pages["ct"].go_to_notifications_tab()
        pages["ct"].go_to_calendar_tab()
        pages["ct"].go_to_map_tab()
