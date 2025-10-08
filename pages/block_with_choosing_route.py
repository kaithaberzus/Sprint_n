from locators.route_selection_block_locators import RouteSelectionBlockLocators
from pages.base import Base
import allure


class BlockWithChoosingRoute(Base):

    @allure.step('Проверка отображения время в пути 0 минут в блоке с маршрутами')
    def check_displaying_time_in_trip_zero_if_input_same_addresses(self):
        return self.check_displaying(RouteSelectionBlockLocators.TEXT_TIME_IN_ROUTE_SAME_ADDRESS)

    @allure.step('Проверка отображения 0 руб. в блоке с маршрутами')
    def check_displayed_price_of_trip_zero_if_input_same_addresses(self):
        return self.check_displaying(RouteSelectionBlockLocators.TEXT_FOR_FREE)

    @allure.step('Клик по маршруту Оптимальный')
    def click_to_the_optimal_route(self):
        self.click_to(RouteSelectionBlockLocators.MODE_NONE_ACTIVE_OPTIMAL)

    @allure.step('Клик по маршруту Свой')
    def click_to_the_yours_route(self):
        self.click_to(RouteSelectionBlockLocators.MODE_NONE_ACTIVE_YOURS)

    @allure.step('Проверка отображения активного маршрута Свой')
    def check_displaying_active_yours_route(self):
        return self.check_displaying(RouteSelectionBlockLocators.MODE_ACTIVE_YOURS)

    @allure.step('Проверка отображения активного метода передвижения пешком')
    def check_displaying_active_method_of_transportation_by_foot(self):
        return self.check_displaying(RouteSelectionBlockLocators.ACTIVE_OPTIONS_BY_FOOT_IN_YOURS)

    @allure.step('Проверка отображения активного метода передвижения на машине')
    def check_displaying_active_method_of_transportation_by_car(self):
        return self.check_displaying(RouteSelectionBlockLocators.ACTIVE_OPTIONS_CAR_IN_YOURS)

    @allure.step('Проверка отображения активного метода передвижения на такси')
    def check_displaying_active_method_of_transportation_by_taxi(self):
        return self.check_displaying(RouteSelectionBlockLocators.ACTIVE_OPTIONS_TAXI_IN_YOURS)

    @allure.step('Проверка отображения активного метода передвижения на мотоцикле')
    def check_displaying_active_method_of_transportation_by_bike(self):
        return self.check_displaying(RouteSelectionBlockLocators.ACTIVE_OPTIONS_BIKE_IN_YOURS)

    @allure.step('Проверка отображения активного метода передвижения на самокате')
    def check_displaying_active_method_of_transportation_by_scooter(self):
        return self.check_displaying(RouteSelectionBlockLocators.ACTIVE_OPTIONS_SCOOTER_IN_YOURS)

    @allure.step('Проверка отображения активного метода передвижения драйв')
    def check_displaying_active_method_of_transportation_by_drive(self):
        return self.check_displaying(RouteSelectionBlockLocators.ACTIVE_OPTIONS_DRIVE_IN_YOURS)

    @allure.step('Клик по методу передвижения драйв')
    def click_to_the_method_of_transportation_drive(self):
        self.click_to(RouteSelectionBlockLocators.ACTIVE_OPTIONS_DRIVE_IN_YOURS)

    @allure.step('Клик по кнопке вызова такси')
    def click_to_the_button_call_a_taxi(self):
        self.click_to(RouteSelectionBlockLocators.BUTTON_GET_TAXI)

    @allure.step('')
    def get_text_of_time_in_route_faster(self):
        time = self.get_text_from_element(RouteSelectionBlockLocators.TEXT_TIME_IN_ROUTE)
        ready_time = time.split('~')[1]

        return ready_time

    @allure.step('')
    def get_text_of_cost_the_route_faster(self):
        cost = self.get_text_from_element(RouteSelectionBlockLocators.TEXT_COST_IN_ROUTE)
        ready_cost = cost.split('пути')[1]

        return ready_cost

    @allure.step('')
    def get_text_of_time_in_route_optimal(self):
        time = self.get_text_from_element(RouteSelectionBlockLocators.TEXT_TIME_IN_ROUTE)
        ready_time = time.split('~')[1]

        return ready_time

    @allure.step('')
    def get_text_of_cost_the_route_optimal(self):
        cost = self.get_text_from_element(RouteSelectionBlockLocators.TEXT_COST_IN_ROUTE)
        ready_cost = cost.split('пути')[1]

        return ready_cost

    @allure.step('')
    def check_displaying_button_get_a_taxi(self):
        return self.check_displaying(RouteSelectionBlockLocators.BUTTON_GET_TAXI)

    @allure.step('')
    def check_displaying_button_get_drive(self):
        return self.check_displaying(RouteSelectionBlockLocators.BUTTON_TO_BOOK)
