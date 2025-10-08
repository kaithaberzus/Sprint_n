from selenium.webdriver.common.by import By


class WindowOfWaitingOrderingATaxiLocators:

    # Кнопка детали
    BUTTON_DETAILS = By.XPATH, ".//div[text()='Детали']"

    # Кнопка отмена
    BUTTON_CANCEL = By.XPATH, ".//div[text()='Отменить']"

    # Заголовок окна
    TITLE_FINDING_CARS = By.XPATH, ".//div[text()='Поиск машины']"

    # Таймер
    COUNTDOWN_TIMER = By.XPATH, ".//div[@class='order-header-time']"
