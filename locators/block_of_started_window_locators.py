from selenium.webdriver.common.by import By


class StartedWindowLocators:

    # Поле ввода адреса откуда
    INPUT_TO = By.ID, "to"

    # Поле ввода адреса куда
    INPUT_FROM = By.ID, "from"

    # Маршрут на карте
    POINTS = By.XPATH, ".//ymaps[contains(@class, 'ymaps-2-1-79-route-pin__text')]/ymaps[@id]"
