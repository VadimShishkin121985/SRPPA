from time import sleep

import pytest

from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from pages.main_page import MainPage
from pages.request_app_page import RequestAQuote
from pages.sign_in_page import SignIn
from tests.test_tracking import Test_Tracking


class Test_Request(Test_Tracking):
    page = None

    @pytest.fixture(autouse=True)
    def _setup_page(self, page):
        self.page = page

    @property
    def request_app_page(self):
        if not hasattr(self, "_request_app_page"):
            self._request_app_page = RequestAQuote(self.page)
        return self._request_app_page


    def test_go_to_request_app(self, page):
        self.test_sign_in(self.page)
        self.request_app_page.go_to_request_app()

    def test_send_default_request(self, page):
        self.test_go_to_request_app(page)
        self.request_app_page.send_default_request()

        pass
