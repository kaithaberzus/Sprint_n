from pages.block_with_started_window import BlockWithStartedWindow
from pages.block_with_choosing_route import BlockWithChoosingRoute
import allure
from data import Addresses


class TestBlockWithStartedWindow:

    @allure.title('Проверка отображения маршрута при введение разных адресов в поля откуда и куда')
    def test_check_displaying_point_a_and_point_b_after_enter_two_diff_addresses(self, driver):
        bwsw = BlockWithStartedWindow(driver)
        adr = Addresses()

        bwsw.open_main_page()
        bwsw.fill_input_to(adr.ADDRESS_HAM_VAL)
        bwsw.fill_input_from(adr.ADDRESS_ZUB_VAL)

        assert bwsw.check_displaying_points

    @allure.title('Проверка отображения в пути 0 мин. и бесплатно при введении одинаковых адресов в поля откуда и куда')
    def test_check_displaying_in_description_0_min_in_route_and_for_free_after_enter_the_same_address(self, driver):
        bwsw = BlockWithStartedWindow(driver)
        bwcar = BlockWithChoosingRoute(driver)
        adr = Addresses()

        bwsw.open_main_page()
        bwsw.fill_input_to(adr.ADDRESS_HAM_VAL)
        bwsw.fill_input_from(adr.ADDRESS_HAM_VAL)

        assert (bwcar.check_displayed_price_of_trip_zero_if_input_same_addresses and
                bwcar.check_displaying_time_in_trip_zero_if_input_same_addresses)