from time import sleep
import os
import random
from dotenv import load_dotenv
from playwright.sync_api import expect

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

    def get_random_tracking_number(self) -> str:
        numbers_str = os.getenv("TEST_CT_NUMBER", "")
        numbers = [n.strip() for n in numbers_str.split(",") if n.strip()]

        if not numbers:
            raise RuntimeError(
                "TEST_CT_NUMBER is empty or not set. "
                "Expected comma-separated tracking numbers."
            )

        return random.choice(numbers)

    def _safe_click(self, locator: str, timeout: int = 30000):
        page = self.page
        els = page.locator(locator)

        expect(els.first).to_be_attached(timeout=timeout)

        # выбрать первый видимый
        chosen = None
        for i in range(els.count()):
            cand = els.nth(i)
            if cand.is_visible():
                chosen = cand
                break
        if chosen is None:
            raise TimeoutError(f"_safe_click: no visible element for locator: {locator}")

        chosen.scroll_into_view_if_needed()
        expect(chosen).to_be_enabled()

        try:
            chosen.click(trial=True, timeout=min(5000, timeout))
            chosen.click(timeout=timeout)
        except Exception:
            # 🔥 если перехватывают pointer events — кликаем событием по элементу
            chosen.dispatch_event("click")
