from locators.block_of_started_window_locators import StartedWindowLocators
import allure
from pages.base import Base
from data import URL


class BlockWithStartedWindow(Base):

    @allure.step('Заполнение поля откуда')
    def fill_input_to(self, address):
        self.fill_input(StartedWindowLocators.INPUT_TO, address)

    @allure.step('Заполнение поля куда')
    def fill_input_from(self, address):
        self.fill_input(StartedWindowLocators.INPUT_FROM, address)

    @allure.step('Проверка отображения пункта б и а на карте')
    def check_displaying_points(self):
        return self.check_displaying(StartedWindowLocators.POINTS)

    @allure.step('')
    def open_main_page(self):
        self.open_url(URL, StartedWindowLocators.INPUT_FROM)
