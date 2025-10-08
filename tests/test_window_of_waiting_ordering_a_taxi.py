from pages.window_of_waiting_ordering_a_taxi import WindowOfWaitingOrderingATaxi
import allure


class TestWindowOfWaitingOrderingATaxi:

    @allure.title('Проверка отображения кнопки детали, отмена и таймера при вызове такси')
    def test_check_displaying_window_of_search_a_driver_with_buttons_details_cancel_and_timer(self, driver, fill_started_block, get_taxi):
        wowoat = WindowOfWaitingOrderingATaxi(driver)

        assert (wowoat.check_displaying_timer and
                wowoat.check_displaying_button_cancel and
                wowoat.check_displaying_button_details and
                wowoat.check_displaying_window_of_waiting_ordering_a_taxi)