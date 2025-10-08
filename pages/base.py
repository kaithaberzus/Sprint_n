from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.webdriver import ActionChains, Keys
import time


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.stop_time = 10
        self.wait = WebDriverWait(self.driver, self.stop_time)

    @allure.step('Открытие ссылки')
    def open_url(self, url, locator):
        self.driver.get(url)
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            pass

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            pass
        return self.driver.find_element(*locator)

    @allure.step('Клик')
    def click_to(self, locator):
        self.find_element(locator).click()

    @allure.step('Заполнение поля')
    def fill_input(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Скролл')
    def scrolling(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Проверка отображение элемента')
    def check_displaying(self, locator):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            pass
        return self.find_element(locator).is_displayed()

    @allure.step('Наведение курсора на объект')
    def move_to_element(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    @allure.step('Выполнение функции после окончания таймера')
    def waiting_const_time(self, func, callback):
        time.sleep(func / 1000)
        callback()
