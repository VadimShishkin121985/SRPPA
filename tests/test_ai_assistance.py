import pytest
from time import sleep

from playwright.sync_api import expect


class Test_AI_Assistance:

    def test_go_to_ai_app(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()

    def test_ct_default(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_ct_default_question()

    def test_dt_default(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_dt_default_question()

    def test_le_default(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_le_default_question()

    def test_co2_default(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_co2_default_question()

    def test_ss_default(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_ss_default_question()

    def test_fi_default(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_fi_default_question()

    def test_new_chat(self, pages):
        pages["main"].go_to_virtual_office()
        pages["virtual_office"].go_to_ai_app()
        pages["ai_assistant"].check_fi_default_question()
        pages["ai_assistant"].go_to_new_chat()


