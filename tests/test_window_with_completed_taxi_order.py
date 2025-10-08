import pytest
from pages.the_window_of_the_completed_taxi_order import TheWindowOfTheCompletedTaxiOrder
import allure


class TestWindowWithCompletedTaxiOrder:

    @allure.title('Проверка отоюражения окна завершения заказа такси, кнопок детали, отмена, иконки машины и инфо о водителе при завершении ожидания поиска машины')
    def test_check_displaying_window_of_completed_ordering_with_buttons_details_cancel_and_info_about_car_and_driver(self, driver, fill_started_block, get_taxi):
        twotcto = TheWindowOfTheCompletedTaxiOrder(driver)

        twotcto.waiting_const_time(35000, twotcto.check_displaying_window_with_completed_taxi_order )

        assert (twotcto.check_displaying_button_details and
                twotcto.check_displaying_button_cancel and
                twotcto.check_displaying_icon_car and
                twotcto.check_displaying_avatar_name_and_rating_of_driver and
                twotcto.check_displaying_window_with_completed_taxi_order)

    @pytest.mark.xfail
    @allure.title('Проверка закрытия окна завершения заказа такси при нажатии на кнопку отмена')
    def test_window_with_completed_taxi_ordering_is_closed_after_click_to_cancel_button(self, driver, fill_started_block, get_taxi):
        twotcto = TheWindowOfTheCompletedTaxiOrder(driver)

        twotcto.waiting_const_time(25000, twotcto.click_to_the_cancel_button)

        assert not twotcto.check_displaying_window_with_completed_taxi_order
