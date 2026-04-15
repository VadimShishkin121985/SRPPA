import pytest
from time import sleep

from playwright.sync_api import expect


class Test_Shiplot:

    def test_go_to_menu_services_page_ex(self, pages):
        pages["main_shiplot"].go_to_services_page_ex()

    def test_go_to_freight_calculator_app_ex(self, pages):
        pages["main_shiplot"].go_to_freight_calculator_app_ex()

    def test_go_to_cargo_tracking_ex(self, pages):
        pages["main_shiplot"].go_to_cargo_tracking_ex()

    def test_go_to_shipping_schedules_ex(self, pages):
        pages["main_shiplot"].go_to_shipping_schedules_page_ex()

    def test_go_to_staffing_calculator_ex(self, pages):
        pages["main_shiplot"].go_to_staffing_calculator_page_ex()

    def test_go_to_logistics_map_ex(self, pages):
        pages["main_shiplot"].go_to_logistics_map_page_ex()

    def test_go_to_distance_and_time_ex(self, pages):
        pages["main_shiplot"].go_to_distance_and_time_page_ex()

    def test_go_to_co2_calculator_ex(self, pages):
        pages["main_shiplot"].go_to_co2_calculator_page_ex()

    def test_go_to_ai_assistant_ex(self, pages):
        pages["main_shiplot"].go_to_ai_assistant_page_ex()

    def test_go_to_about_page_from_menu_ex(self, pages):
        pages["main_shiplot"].go_to_about_page_ex()

    def test_go_to_contact_page_from_menu_ex(self, pages):
        pages["main_shiplot"].go_to_contact_page_ex()

    def test_go_to_sign_in_ex(self, pages):
        pages["main_shiplot"].go_to_sign_in_ex()

    def test_go_to_services_page_through_footer_ex(self, pages):
        pages["main_shiplot"].go_to_services_through_footer_ex()

    def test_go_to_about_page_through_footer_ex(self, pages):
        pages["main_shiplot"].go_to_about_through_footer_ex()

    def test_go_to_contact_page_through_footer_ex(self, pages):
        pages["main_shiplot"].go_to_contact_through_footer_ex()
