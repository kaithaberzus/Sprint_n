from pages.window_with_details_of_order import WindowWithDetailsOfOrder
from pages.the_window_of_the_completed_taxi_order import TheWindowOfTheCompletedTaxiOrder
import allure


class TestWindowWithDetailsOfOrder:

    @allure.title('Проверка совпадения стоимости поездки в блоке заказа такси у тарифа и в окне завершения заказа такси в деталях')
    def test_price_in_tariff_info_matches_with_price_in_order_info(self, driver, fill_started_block, get_taxi):
        twotcto = TheWindowOfTheCompletedTaxiOrder(driver)
        wwdoo = WindowWithDetailsOfOrder(driver)

        twotcto.waiting_const_time(30000, twotcto.click_to_the_button_details)
        cost = wwdoo.get_cost_of_a_trip()

        assert get_taxi == cost