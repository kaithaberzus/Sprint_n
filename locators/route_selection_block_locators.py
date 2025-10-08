from selenium.webdriver.common.by import By


class RouteSelectionBlockLocators:

    # Блок с выбором маршрута
    BLOCK_WITH_ROUTE_SELECTION = By.CLASS_NAME, "workflow-subcontainer"

    # Текст авто бесплатно
    TEXT_FOR_FREE = By.XPATH, ".//div[@class='text' and text()='Авто бесплатно']"

    # Текст В пути 0 мин.
    TEXT_TIME_IN_ROUTE_SAME_ADDRESS = By.XPATH, ".//div[@class='duration' and text()='В пути 0 мин.']"

    # Вид маршрута твой в активном состоянии
    MODE_ACTIVE_YOURS = By.XPATH, ".//div[@class='mode active' and text()='Свой']"

    # Вид маршрута твой в не активном состоянии
    MODE_NONE_ACTIVE_YOURS = By.XPATH, ".//div[@class='mode' and text()='Свой']"

    # Вид маршрута оптимальный в активном состоянии
    MODE_ACTIVE_OPTIMAL = By.XPATH, ".//div[@class='mode active' and text()='Оптимальный']"

    # Вид маршрута оптимальный в не активном состоянии
    MODE_NONE_ACTIVE_OPTIMAL = By.XPATH, ".//div[@class='mode' and text()='Оптимальный']"

    # Цена выбранного маршрута
    TEXT_COST_IN_ROUTE = By.XPATH, ".//div[@class='text']"

    # Время в пути выбранного маршрута
    TEXT_TIME_IN_ROUTE = By.XPATH, ".//div[@class='duration']"

    #  Цена маршрута свой
    TEXT_YOURS = By.XPATH, ".//div[@class='text' and text()='Авто ~ 40 руб.']"

    # Время в пути маршрута свой
    TEXT_TIME_IN_ROUTE_YOURS = By.XPATH, ".//div[@class='duration' and text()='В пути 4 мин.']"

    # Вид маршрута быстрый в активном состоянии
    MODE_ACTIVE_FAST = By.XPATH, ".//div[@class='mode active' and text()='Быстрый']"

    # Вид маршрута быстрый в не активном состоянии
    MODE_NONE_ACTIVE_FAST = By.XPATH, ".//div[@class='mode' and text()='Быстрый']"

    # Тип передвижения пешком в активном состоянии в виде маршрута твой
    ACTIVE_OPTIONS_BY_FOOT_IN_YOURS = By.XPATH, ".//div[@class='types-container']/div[@class='type'][2]"

    # Тип передвижения такси в активном состоянии в маршруте вида быстрый
    ACTIVE_TAXI_IN_FAST = By.XPATH, ".//div[@class='types-container']/div[@class='type active disabled']"

    # Тип передвижения такси в активном состоянии в виде маршрута твой
    ACTIVE_OPTIONS_TAXI_IN_YOURS = By.XPATH, ".//div[@class='types-container']/div[@class='type active']"

    # Тип передвижение на машине в активном состоянии в виде маршрута твой
    ACTIVE_OPTIONS_CAR_IN_YOURS = By.XPATH, ".//div[@class='types-container']/div[@class='type'][1]"

    # Тип передвижение на мотоцикле в активном состоянии в виде маршрута твой
    ACTIVE_OPTIONS_BIKE_IN_YOURS = By.XPATH, ".//div[@class='types-container']/div[@class='type'][3]"

    # Тип передвижение на самокате в активном состоянии в виде маршрута твой
    ACTIVE_OPTIONS_SCOOTER_IN_YOURS = By.XPATH, ".//div[@class='types-container']/div[@class='type'][4]"

    # Тип передвижение драйв в активном состоянии в виде маршрута твой
    ACTIVE_OPTIONS_DRIVE_IN_YOURS = By.XPATH, ".//div[@class='types-container']/div[@class='type drive']"

    # Кнопка забронировать
    BUTTON_TO_BOOK = By.XPATH, ".//button[text()='Забронировать']"

    # Кнопка вызвать такси
    BUTTON_GET_TAXI = By.XPATH, ".//button[text()='Вызвать такси']"
