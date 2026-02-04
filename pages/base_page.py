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

        # 0) попытка снять активные hover/меню (часто именно они мешают)
        page.keyboard.press("Escape")
        page.mouse.move(1, 1)
        page.locator("body").click(position={"x": 5, "y": 5})

        el = page.locator(locator).first

        el.wait_for(state="visible", timeout=timeout)
        el.scroll_into_view_if_needed()
        expect(el).to_be_enabled()

        # 1) проверка кликабельности
        try:
            el.click(trial=True, timeout=min(5000, timeout))
        except Exception:
            # 2) если кто-то перехватывает клики — ещё раз “сброс” и повтор
            page.keyboard.press("Escape")
            page.mouse.move(1, 1)
            page.locator("body").click(position={"x": 5, "y": 5})
            el.scroll_into_view_if_needed()
            el.click(trial=True, timeout=min(5000, timeout))

        # 3) реальный клик
        el.click(timeout=timeout)
