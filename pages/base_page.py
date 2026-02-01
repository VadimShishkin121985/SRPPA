from time import sleep
import os
import random
from dotenv import load_dotenv
from playwright.sync_api import expect
from playwright.sync_api import expect, TimeoutError as PWTimeoutError

load_dotenv()


class BasePage:
    def __init__(self, page):
        self.page = page

    def press_tab(self, times=1, shift=False):
        """
        :param times: количество нажатий Tab / Shift+Tab
        :param shift: True — Shift+Tab, False — Tab
        """
        key = "Shift+Tab" if shift else "Tab"
        for _ in range(times):
            self.page.keyboard.press(key)
            sleep(1)
        self.page.keyboard.press("Enter")

    def get_random_tracking_number(eslf):
        numbers_str = os.getenv("TEST_CT_NUMBER", "")
        numbers = [n.strip() for n in numbers_str.split(",") if n.strip()]
        return random.choice(numbers) if numbers else None


    def _safe_click(self, locator: str, timeout: int = 30000):
        el = self.page.locator(locator)
        el.wait_for(state="visible", timeout=timeout)
        el.scroll_into_view_if_needed()
        expect(el).to_be_enabled()

        try:
            el.click(trial=True, timeout=5000)
        except PWTimeoutError:
            # чаще всего это overlay / active section intercept
            self.page.keyboard.press("Escape")
            self.page.click("body", position={"x": 5, "y": 5})
            el.wait_for(state="visible", timeout=timeout)
            el.scroll_into_view_if_needed()
            el.click(trial=True, timeout=5000)

        el.click(timeout=timeout)
