from pages.base import Base
from locators.window_of_complete_order_locators import WindowOfCompleteOrderLocators
import allure


class TheWindowOfTheCompletedTaxiOrder(Base):

    @allure.step('Проверка отображения окна с ожиданием машины')
    def check_displaying_window_with_completed_taxi_order(self):
        return self.check_displaying(WindowOfCompleteOrderLocators.WINDOW_OF_COMLETE_ORDER)

    @allure.step('Проверка отображения кнопки детали')
    def check_displaying_button_details(self):
        return self.check_displaying(WindowOfCompleteOrderLocators.BUTTON_DETAILS)

    @allure.step('Проверка отображения кнопки отмена')
    def check_displaying_button_cancel(self):
        return self.check_displaying(WindowOfCompleteOrderLocators.BUTTON_CANCEL)

    @allure.step('Проверка отображения аватара, рейтинга и имени водителя')
    def check_displaying_avatar_name_and_rating_of_driver(self):
        return self.check_displaying(WindowOfCompleteOrderLocators.AVATAR_NAME_AN_RATE_OF_DRIVER)

    @allure.step('Проверка отображения иконки машины и ее номера')
    def check_displaying_icon_car(self):
        return self.check_displaying(WindowOfCompleteOrderLocators.IMG_OF_A_CAR)

    @allure.step('Клик по кнопке отмена')
    def click_to_the_cancel_button(self):
        self.click_to(WindowOfCompleteOrderLocators.BUTTON_CANCEL)

    @allure.step('Клик по кнопке детали')
    def click_to_the_button_details(self):
        self.click_to(WindowOfCompleteOrderLocators.BUTTON_DETAILS)
