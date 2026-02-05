import random
import string
from time import sleep
from pages.base_page import BasePage
from pages.locator_page import LocatorsPage
from playwright.sync_api import expect
import os
import shutil


class ContainerTrackingPage(BasePage, LocatorsPage):
    # def __init__(self, page):
    #     super().__init__(page)

    # def update_button_click(self):
    #     update_button = self.page.locator("button:has-text('update')").first
    #
    #     expect(update_button).to_be_visible()
    #
    #     card_id = update_button.get_attribute("data-test-id")
    #     assert card_id, "Не удалось получить data-test-id у кнопки update"
    #
    #     update_button.click()
    #
    #     expect(update_button).not_to_have_text("update", timeout=15000)
    def update_button_click(self):
        update_button = self.page.locator("[data-test-id='card-status-update-button']").first
        expect(update_button).to_be_visible(timeout=10000)

        card = update_button.locator("xpath=ancestor::div[.//div[@data-test-id='card-number']]")
        card_number = card.locator("[data-test-id='card-number']").first.inner_text()
        print(f"Updating card: {card_number}")

        update_button.click()

        status = card.locator(
            "[data-test-id^='card-status-']:not([data-test-id='card-status-update-button'])"
        ).first
        expect(status).to_be_visible(timeout=20000)

    def fill_input_ct_number(self):
        self.number = self.get_random_tracking_number()
        self.page.fill(self.INPUT_CT_APP, self.number)
        actual_value = self.page.get_attribute(self.INPUT_CT_APP, "value")
        assert actual_value == self.number, (
            f"value='{self.number}', bat  '{actual_value}'"
        )

    def click_search_button_ct_app(self):
        self.page.click(self.SEARCH_BUTTON_CT)
        expect(self.page.locator(self.ROUTE_BUTTON)).to_be_visible(timeout=500000)

    def click_on_follow_button(self):
        self.page.click(self.FOLLOW_BUTTON)
        expect(self.page.locator(self.FOLLOW_BUTTON)).to_have_count(0)

    def open_the_updated_card(self):
        self.page.click(self.OPEN_CARD)
        expect(self.page.locator(self.ROUTE_BUTTON)).to_be_visible(timeout=500000)
        expect(self.page.locator(self.FOLLOW_BUTTON)).not_to_be_visible(timeout=500000)

    def delete_the_card(self):
        self.page.click(self.DELETE_CARD_BUTTON)
        self.page.click(self.CONFIRM_DELETE_CARD_BUTTON)
        expect(self.page.locator(self.CT_LIST_CARD)).to_be_visible(timeout=500000)

    def open_the_first_card(self):
        self.page.click(self.FIRST_CARD)
        expect(self.page.locator(self.RATE_SWIPER)).to_be_visible(timeout=500000)

    def click_on_the_rate(self):
        sleep(3)
        if self.page.locator(self.BOOK_NOW_IN_SWIPER).count() > 0:
            with self.page.context.expect_page() as new_page_info:
                self.page.locator(self.BOOK_NOW_IN_SWIPER).first.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state("domcontentloaded")
            expect(new_page.locator(self.MAP_PREBOOK_PAGE)).to_be_visible(timeout=500000)
        else:
            with self.page.context.expect_page() as new_page_info:
                self.page.locator(self.REQUEST_QUOTA_IN_SWIPER).first.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state("domcontentloaded")
            expect(new_page.locator(self.RQ_CARGO_DETAILS_LOCATOR)).to_be_visible(timeout=500000)

        return new_page

    def download_file(self):
        # ✅ кроссплатформенно: папка downloads рядом с проектом (где запускается pytest)
        downloads_dir = os.path.abspath(os.path.join(os.getcwd(), "downloads"))
        os.makedirs(downloads_dir, exist_ok=True)

        # ✅ чистим папку если накопилось >= 200 файлов
        if os.path.exists(downloads_dir) and len(os.listdir(downloads_dir)) >= 200:
            shutil.rmtree(downloads_dir)
            os.makedirs(downloads_dir, exist_ok=True)

        # ✅ ждём download
        with self.page.expect_download() as download_info:
            self.page.click(self.UPLOAD_FILE_MENU_CT)
            self.page.click(self.EMPTY_TEMPLATE)

        download = download_info.value

        base_name = download.suggested_filename or "download.bin"
        name, ext = os.path.splitext(base_name)

        # ✅ если файл уже существует → добавляем суффикс
        save_path = os.path.join(downloads_dir, base_name)
        counter = 1
        while os.path.exists(save_path):
            save_path = os.path.join(downloads_dir, f"{name}_{counter}{ext}")
            counter += 1

        # ❌ sleep(10) не нужен — save_as сам дождётся артефакта
        download.save_as(save_path)

        assert os.path.exists(save_path), f"Файл не найден: {save_path}"
        assert os.path.getsize(save_path) > 0, f"Файл пустой: {save_path}"

        print(f"✅ Download saved: {save_path}")

    def upload_test_file(self):
        file_path = "/Users/Vadim/PycharmProjects/SRPPA/data/containers.xlsx"

        # Клик по меню, если нужно открыть форму загрузки
        self.page.click(self.UPLOAD_FILE_MENU_CT)

        # Загружаем файл напрямую в скрытый input
        self.page.set_input_files(
            "input[type='file'][accept='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']",
            file_path
        )

        # Ассерт: кнопка с текстом файла существует (видимость не важна)
        file_name = os.path.basename(file_path)
        uploaded_file_button = self.page.locator(f"button:has-text('{file_name}')")
        assert uploaded_file_button.count() > 0, f"Кнопка с файлом {file_name} не найдена"

        self.page.click(self.NEXT_BUTTON_UPLOAD_FILE)
        expect (self.page.locator(self.SUCCESFULLY_UPLOAD_FILE)).to_be_visible(timeout=500000)

    def random_latin_string(self, length: int = 15) -> str:
        return ''.join(random.choices(string.ascii_letters, k=length))

    def add_first_tag(self):
        add_btn = self.page.locator(self.ADD_FIRST_TAG_BUTTON)

        # 1. Убедиться, что кнопка существует
        #expect(add_btn).to_be_attached()
        #expect(add_btn).to_be_visible()

        # 2. Осознанный force-клик (overlay постоянный)
        add_btn.click(force=True)

        # 3. Работаем уже ВНУТРИ модалки
        modal = self.page.locator(".unified-tracking-gIokNt")
        expect(modal).to_be_visible()

        # 4. Удаляем все существующие теги
        crosses = modal.locator(self.DELETE_TAG_CROSS)
        while True:
            count_before = crosses.count()
            if count_before == 0:
                break
            crosses.first.click()
            expect(crosses).to_have_count(count_before - 1)

        # 5. Добавляем новый тег
        tag_input = modal.locator(self.TAG_INPUT)
        expect(tag_input).to_be_visible()
        tag_input.fill(self.random_latin_string())

        modal.locator(self.SAVE_BUTTON_TAG).click()

        # 6. Проверка результата
        expect(self.page.locator(self.EDIT_TAG_BUTTON)).to_be_visible()

    def copy_past_link(self):
        self.page.click(self.COPY_BUTTON)
        clipboard_text = self.page.evaluate("navigator.clipboard.readText()")
        assert clipboard_text, "Буфер обміну порожній"
        new_page = self.page.context.new_page()
        new_page.goto(clipboard_text)
        new_page.wait_for_load_state("domcontentloaded")
        expect(new_page.locator(self.ROUTE_BUTTON)).to_be_visible(timeout=10000)
        
        return new_page

    def setting_map(self):
        self.page.locator(".leaflet-control-layers-toggle").click(force=True)
        radios = self.page.locator(".leaflet-control-layers-selector")
        count = radios.count()
        print(f"Found {count} map layers")

        prev_value = None

        for i in range(count):
            radios.nth(i).click()
            self.page.wait_for_timeout(1000)

            current_value = self.page.evaluate(
                "window.localStorage.getItem('tracking-system-app')"
            )
            print(f"Map layer {i + 1}: localStorage value = {current_value}")

            if prev_value:
                assert current_value != prev_value, (
                    f"❌ Карта не изменилась при выборе слоя #{i + 1}: "
                    f"localStorage остался тем же"
                )

            prev_value = current_value

    def go_to_vessel_tab(self):
        self.page.click(self.VESSEL_TAB)
        sleep(2)
        expect(self.page.locator(self.VOYAGE_IN_VESSEL_TAB).first).to_be_visible(timeout=10000)

    def go_to_route_tab(self):
        self.page.click(self.ROUTE_BUTTON)
        sleep(2)
        expect(self.page.locator(self.ROUTE_BUTTON)).to_be_visible(timeout=10000)

    def click_on_the_point(self):
        sleep(2)
        self.page.hover(self.POINT_ON_MAP)
        self.page.click(self.POINT_ON_MAP)

    def hover_and_click_on_container_in_point(self):
        self.page.hover(self.CONTAINER_NUMBER_POINT)
        self.page.click(self.CONTAINER_NUMBER_POINT)
        expect(self.page.locator(self.ROUTE_BUTTON)).to_be_visible(timeout=500000)

    def search_button_ct_app_limiter(self):
        self.page.click(self.SEARCH_BUTTON_CT)

        limit_msg = self.page.locator(self.DAILY_LIMIT_MESSAGE)
        route_btn = self.page.locator(self.ROUTE_BUTTON)

        try:
            expect(limit_msg).to_be_visible(timeout=2000)
            return
        except:
            pass

        expect(route_btn).to_be_visible(timeout=5000)


    def open_subscription_info(self):
        self.page.click(self.PAID_BUTTON_SUBSCRIPTION)
        expect(self.page.locator(self.PAID_PLAN)).to_be_visible(timeout=500000)

    def check_credit_counter(self):
        counter_before = self.page.locator(self.CREDITS_USED).inner_text()
        print(f"📊 Кредитів ДО пошуку: {counter_before}")

        # Виконуємо пошук
        self.fill_input_ct_number()
        self.click_search_button_ct_app()
        self.page.reload()

        # Чекаємо оновлення лічильника (можливо потрібна затримка)
        sleep(2)

        # Відкриваємо інфо про підписку
        self.open_subscription_info()


    def purchase_additional_credits(self):
        # Очікуємо відкриття нової сторінки після кліку
        with self.page.context.expect_page() as new_page_info:
            self.page.click(self.PURCHASE_CREDITS)

        # Отримуємо нову сторінку
        new_page = new_page_info.value

        # Чекаємо завантаження нової сторінки
        new_page.wait_for_load_state("domcontentloaded")

        # Перевіряємо що на новій сторінці є потрібний локатор
        expect(new_page.locator(self.PRO_PLAN)).to_be_visible(timeout=10000)

        return new_page

    def go_to_analytics_tab(self):
        with self.page.expect_response(lambda r: r.status == 200):
            self.page.click(self.ANALYTICS_TAB_BOTTON)
            expect(self.page.locator(self.CONTENT_ANALYTICS_TAB).first).to_be_visible(timeout=500000)


    def go_to_notifications_tab(self):
        with self.page.expect_response(lambda r: r.status == 200):
            self.page.click(self.NOTIFICATION_TAB_BOTTON)
            expect(self.page.locator(self.CONTENT_NOTIFICATION_TAB).first).to_be_visible(timeout=500000)

    def go_to_calendar_tab(self):
        with self.page.expect_response(lambda r: r.status == 200):
            self.page.click(self.CALENDAR_TAB_BOTTON)
            expect(self.page.locator(self.CONTENT_CALENDAR_TAB).first).to_be_visible(timeout=500000)

    def go_to_map_tab(self):
        with self.page.expect_response(lambda r: r.status == 200):
            self.page.click(self.MAP_TAB_BOTTON)
            expect(self.page.locator(self.POINT_ON_MAP).first).to_be_visible(timeout=500000)



















