import random
import string
from time import sleep
from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from playwright.sync_api import expect
import os
import shutil


class RequestAQuote(BasePage, LocatorsPage):
    def __init__(self, page):
        super().__init__(page)

    def go_to_request_app(self):
        self.page.hover(self.MENU_SERVICES)
        self.page.click(self.REQUEST_A_QUOTE_MENU)
        self.page.wait_for_selector(self.REQUEST_APP, state="visible")
        pass

    def send_default_request(self):
        self.page.click(self.HS_CODE_REQUEST)
        self.page.type(self.HS_CODE_REQUEST, "090611")
        self.page.locator(".cg_b7", has_text="090611").nth(0).click()
        #заполняем поле веса
        self.page.locator("#cargoWeight").click()
        self.page.type("#cargoWeight", "5")
        #заполняем поле от
        self.page.locator("#autocomplete_from").click()
        self.page.type("#autocomplete_from", "65000")
        self.page.locator(".w3zuf").first.click()
        self.page.locator(".WOajJ").first.click()
        #Заполняем поле ТУ
        self.page.locator("#autocomplete_to").click()
        self.page.type("#autocomplete_to", "mumbai")
        self.page.locator(".w3zuf").first.click()
        self.page.locator(".WbWAn", has_text="Mumbai, India").nth(0).click()
        #Zip Code From
        self.page.locator("#zipCodeFrom").click()
        self.page.type("#zipCodeFrom", "65000")
        #Zip Code To
        self.page.locator("#zipCodeTo").click()
        self.page.type("#zipCodeTo", "400001")
        #* Ready to load
        self.page.locator(".KLr4P").click()
        self.page.locator(".Calendar__day.-today[aria-disabled='false']").click()
        self.page.locator(".Calendar__day.-weekend[aria-disabled='false']").first.click()
        #Additional information
        self.page.locator(".textarea__element").click()
        self.page.type(".textarea__element", "Test Test Test Test Test")
        # Send button
        self.page.locator(".PfDxg", has_text="Send").nth(0).click()
        expect(self.page.locator(".cJg5n")).to_be_visible(timeout=50000)

        sleep(10)