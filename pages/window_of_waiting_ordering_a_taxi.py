from locators.window_of_waiting_ordering_a_taxi_locators import WindowOfWaitingOrderingATaxiLocators
from pages.base import Base
import allure


class WindowOfWaitingOrderingATaxi(Base):

    @allure.step('Проверка отображения окна поиска машины')
    def check_displaying_window_of_waiting_ordering_a_taxi(self):
        return self.check_displaying(WindowOfWaitingOrderingATaxiLocators.TITLE_FINDING_CARS)

    @allure.step('Проверка отображения кнопки детали')
    def check_displaying_button_details(self):
        return self.check_displaying(WindowOfWaitingOrderingATaxiLocators.BUTTON_DETAILS)

    @allure.step('Проверка отображения кнопки отмена')
    def check_displaying_button_cancel(self):
        return self.check_displaying(WindowOfWaitingOrderingATaxiLocators.BUTTON_CANCEL)

    @allure.step('Проверка отображения таймера')
    def check_displaying_timer(self):
        return self.check_displaying(WindowOfWaitingOrderingATaxiLocators.COUNTDOWN_TIMER)

