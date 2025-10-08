from pages.block_with_choosing_route import BlockWithChoosingRoute
import allure


class TestBlockWithChoosingARoute:

    @allure.title('Проверка смена активного таба и пересчет времени и стоимости маршрута при переключении вида маршрута Оптимальный/Быстрый')
    def test_change_active_tab_and_time_and_cost_recalc_after_switch_betw_routes_optim_and_faster(self, driver, fill_started_block):
        bwcr = BlockWithChoosingRoute(driver)

        time_faster = bwcr.get_text_of_time_in_route_faster
        cost_faster = bwcr.get_text_of_cost_the_route_faster

        bwcr.click_to_the_optimal_route()

        time_optimal =bwcr.get_text_of_time_in_route_optimal
        cost_optimal =bwcr.get_text_of_cost_the_route_optimal

        assert time_faster != time_optimal and cost_faster != cost_optimal

    @allure.title('Проверка, что все типы передвижения активный и Свой активен при выборе вида маршрута Свой')
    def test_all_types_of_movement_active_and_route_yours_active_after_switch_to_it(self, driver, fill_started_block):
        bwcr = BlockWithChoosingRoute(driver)

        bwcr.click_to_the_yours_route()

        assert (bwcr.check_displaying_active_yours_route and
                bwcr.check_displaying_active_method_of_transportation_by_bike and
                bwcr.check_displaying_active_method_of_transportation_by_car and
                bwcr.check_displaying_active_method_of_transportation_by_drive and
                bwcr.check_displaying_active_method_of_transportation_by_foot and
                bwcr.check_displaying_active_method_of_transportation_by_scooter and
                bwcr.check_displaying_active_method_of_transportation_by_taxi)


    @allure.title('Проверка отображения кнопки вызова такси при клике по виду маршрута Быстрый')
    def test_button_get_a_taxi_is_active_in_route_faster(self, driver, fill_started_block):
        bwcr = BlockWithChoosingRoute(driver)

        assert bwcr.check_displaying_button_get_a_taxi()

    @allure.title('Проверка активности кнопки забронировать при выборе типа передвижения драйв в виде маршрута Свой')
    def test_button_to_book_is_active_in_route_yours_type_of_movement_drive(self, driver, fill_started_block):
        bwcr = BlockWithChoosingRoute(driver)

        bwcr.click_to_the_yours_route()
        bwcr.click_to_the_method_of_transportation_drive()

        assert bwcr.check_displaying_button_get_drive()