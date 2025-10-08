from selenium.webdriver.common.by import By


class WindowOfCompleteOrderLocators:

    # Номер машины
    NUMBER_OF_A_CAR = By.XPATH, ".//div[@class='number']"

    # Картинка машины
    IMG_OF_A_CAR = By.XPATH, ".//img[@alt='Car']"

    # Время ожидания
    TIME_TO_WAIT = By.XPATH, ".//div[@class='order-header-title']"

    # Аватарка, рейтинг водителя и его имя
    AVATAR_NAME_AN_RATE_OF_DRIVER = By.XPATH, ".//div[@class='order-btn-group'][1]"

    # Кнопка детали
    BUTTON_DETAILS = By.XPATH, ".//div[@class='order-btn-group'][3]"

    # Кнопка отмена
    BUTTON_CANCEL = By.XPATH, ".//div[@class='order-btn-group'][2]"

    # Окно завершения заказа такси
    WINDOW_OF_COMLETE_ORDER = By.XPATH, ".//div[@class='order-body']"
