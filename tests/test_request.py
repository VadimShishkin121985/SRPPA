import pytest

from pages.main_page import MainPage
from pages.request_app_page import RequestAQuote
from pages.sign_in_page import SignInPage



class Test_Request:

    def test_go_to_request_app(self, pages):
        """Переход в Request A Quote"""
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()
        pages["request"].go_to_request_app()

    def test_send_default_request(self, pages):
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()
        pages["request"].go_to_request_app()
        pages["request"].send_default_request()
        # Можно добавить assert, если есть уникальный элемент после отправки
        # например:
        # assert self.page.locator(".cJg5n").is_visible()

    def test_send_default_request_it_quote(self, pages):
        pages["main"].click_on_sign_in_button()
        pages["signin"].sign_in_form()
        pages["main"].go_to_request_it_quota()
        pages["request"].request_it_quote()