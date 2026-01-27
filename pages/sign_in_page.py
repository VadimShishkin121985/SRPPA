import os
from time import sleep
import random

from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from dotenv import load_dotenv


load_dotenv()



class SignIn(BasePage, LocatorsPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.login = os.getenv("TEST_ACCOUNT_LOGIN")
        self.password = os.getenv("TEST_ACCOUNT_PASSWORD")

    def sign_in_form(self, max_attempts=5):

        for attempt in range(1, max_attempts + 1):
            print(f"🔑 Спроба авторизації {attempt}/{max_attempts}")

            self.page.fill(self.LOGIN_OR_EMAIL, self.login)
            self.page.fill(self.PASSWORD, self.password)

            # Випадкова затримка перед натисканням (імітація людини)
            sleep(random.uniform(1.5, 3.5))
            self.page.click(self.SIGN_IN_BUTTON)

            sleep(4)

            # Шукаємо помилку капчі
            if self.page.locator("text=Invalid captcha token").count() > 0:
                print(f"❌ Спроба {attempt}: Invalid captcha token")

                if attempt < max_attempts:
                    wait_time = random.uniform(2, 5)
                    print(f"🔄 Чекаємо {wait_time:.1f}с та перезавантажуємо...")
                    sleep(wait_time)
                    self.page.reload()
                    sleep(3)
                else:
                    raise Exception(f"Не вдалося авторизуватись після {max_attempts} спроб")
            else:
                print("✅ Авторизація успішна")
                return


