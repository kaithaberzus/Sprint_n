from pages.base import Base
from locators.tariffe_picker_block_locators import TariffPickerBlockLocators
import allure


class BlockWithOrderingATaxi(Base):

    @allure.step('Получение цены тарифа Рабочий')
    def get_price_of_tariff_worker(self):
        return self.get_text_from_element(TariffPickerBlockLocators.PRICE_OF_ACTIVE_TARIFF)

    @allure.step('Навести курсор на иконку i')
    def move_to_i_in_tariff(self):
        self.move_to_element(TariffPickerBlockLocators.ICON_I_TARIFF)

    @allure.step('Проверка отображения не активного тарифа глянцевый')
    def check_displaying_non_active_tariff_glantsevi(self):
        return self.check_displaying(TariffPickerBlockLocators.NONE_ACTIVE_CARD_GLANTSEVI)

    @allure.step('Проверка отображения активного тарифа рабочий')
    def check_displaying_active_tariff_worker(self):
        return self.check_displaying(TariffPickerBlockLocators.ACTIVE_CARD_WORKER)

    @allure.step('Проверка отображения не активного тарифа сонный')
    def check_displaying_non_active_tariff_sonni(self):
        return self.check_displaying(TariffPickerBlockLocators.NONE_ACTIVE_CARD_SONNI)

    @allure.step('Проверка отображения не активного тарифа отпускной')
    def check_displaying_non_active_tariff_otpusknoi(self):
        return self.check_displaying(TariffPickerBlockLocators.NONE_ACTIVE_CARD_OTPUSKNOI)

    @allure.step('Проверка отображения не активного тарифа разговорчивый')
    def check_displaying_non_active_tariff_razgovorchivi(self):
        return self.check_displaying(TariffPickerBlockLocators.INFO_ABOUT_TARRIFE_RAZGOVOCHIVI)

    @allure.step('Проверка отображения не активного тарифа утешительный')
    def check_displaying_non_active_tariff_uteshitelni(self):
        return self.check_displaying(TariffPickerBlockLocators.INFO_ABOUT_TARRIFE_UTESHITELNI)

    @allure.step('Проверка отображения поля ввода номера телефона')
    def check_displaying_input_telephone(self):
        return self.check_displaying(TariffPickerBlockLocators.INPUT_TELEPHONE)

    @allure.step('Проверка отображения поля ввода комментария водителю')
    def check_displaying_input_comment(self):
        return self.check_displaying(TariffPickerBlockLocators.COMMENT_TO_DRIVER)

    @allure.step('Проверка отображения поля с выбором способа оплаты')
    def check_displaying_payment_method(self):
        return self.check_displaying(TariffPickerBlockLocators.INPUT_VAR_OF_PAY)

    @allure.step('Скролл до поля для комментария водителю')
    def scrolling_to_input_comment(self):
        self.scrolling(TariffPickerBlockLocators.COMMENT_TO_DRIVER)

    @allure.step('Скролл до бока с требованиями к заказу')
    def scrolling_to_block_req_to_the_order(self):
        self.scrolling(TariffPickerBlockLocators.REQUIREMENTS_TO_THE_ORDER)

    @allure.step('Проверка отображения блока с требованиями к заказу')
    def check_displaying_block_req_to_the_order(self):
        return self.check_displaying(TariffPickerBlockLocators.REQUIREMENTS_TO_THE_ORDER)

    @allure.step('Проверка отображения кнопки заказа такси')
    def check_displaying_button_order_taxi(self):
        return self.check_displaying(TariffPickerBlockLocators.BUTTON_INPUT_NUMBER_OF_ORDER)

    @allure.step('Клик по кнопке заказа такси')
    def click_to_the_button_order_taxi(self):
        self.click_to(TariffPickerBlockLocators.BUTTON_INPUT_NUMBER_OF_ORDER)

    @allure.step('Скролл до кнопки заказа такси')
    def scrolling_to_the_button_order_taxi(self):
        self.scrolling(TariffPickerBlockLocators.BUTTON_INPUT_NUMBER_OF_ORDER)

    @allure.step('Клик по блоку требования к заказу')
    def click_to_the_block_req_to_the_order(self):
        self.click_to(TariffPickerBlockLocators.REQUIREMENTS_TO_THE_ORDER)

    @allure.step('Выбор чекбокса столик для ноутбука')
    def choose_checkbox_table_for_laptop(self):
        self.click_to(TariffPickerBlockLocators.CHECKBOX_TABLE)

    @allure.step('Скролл до чекбокса стол для ноутбука')
    def scrolling_to_checkbox_table_for_laptop(self):
        self.scrolling(TariffPickerBlockLocators.CHECKBOX_TABLE)

    @allure.step('Клик по тарифу рабочий')
    def click_to_tariff(self, locator):
        self.click_to(locator)

    @allure.step('Получение заголовка описания')
    def get_text_from_title_about_tariff(self):
        return self.get_text_from_element(TariffPickerBlockLocators.TITLE_INFO_ABOUT_TARIFF)

    @allure.step('Получение описания тарифа')
    def get_text_from_descr_about_tariff(self):
        return self.get_text_from_element(TariffPickerBlockLocators.DESCRIPTION_ABOUT_TARIFF)

    @allure.step('')
    def scrolling_to_field_method_of_paying(self):
        self.scrolling(TariffPickerBlockLocators.INPUT_VAR_OF_PAY)

    @allure.step('')
    def scrolling_to_field_phone(self):
        self.scrolling(TariffPickerBlockLocators.INPUT_TELEPHONE)
