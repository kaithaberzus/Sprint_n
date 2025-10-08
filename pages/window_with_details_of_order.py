from locators.window_details_locators import WindowDetailsBlockLocators
from pages.base import Base
import allure


class WindowWithDetailsOfOrder(Base):

    @allure.step('Получение цены маршрута')
    def get_cost_of_a_trip(self):
        price = self.get_text_from_element(WindowDetailsBlockLocators.THE_COST_OF_THE_TRIP).split('- ')[1].replace('₽', '')

        return price