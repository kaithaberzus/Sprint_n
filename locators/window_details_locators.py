from selenium.webdriver.common.by import By


class WindowDetailsBlockLocators:

    # Стоимость поездки
    THE_COST_OF_THE_TRIP = By.XPATH, ".//div[@class='o-d-sh' and text()='Стоимость - ']"

    # Заголовок Еще про поездку
    TITLE_MORE_ABOUT_THE_TRIP = By.XPATH, ".//div[@class='o-d-h' and text()='Еще про поездку']"
