from selenium.webdriver.common.by import By


class TariffPickerBlockLocators:

    # Активный тариф рабочий
    ACTIVE_CARD_WORKER = By.XPATH, ".//div[@class='tcard active']/div[@class='tcard-title' and text()='Рабочий']"

    # Не активный тариф сонный
    NONE_ACTIVE_CARD_SONNI = By.XPATH, ".//div[@class='tcard']/div[@class='tcard-title' and text()='Сонный']"

    # Не активный тариф отпускной
    NONE_ACTIVE_CARD_OTPUSKNOI = By.XPATH, ".//div[@class='tcard']/div[@class='tcard-title' and text()='Отпускной']"

    # Не активный тариф разговорчивый
    NONE_ACTIVE_CARD_RAZGOVORCHIVI = By.XPATH, ".//div[@class='tcard']/div[@class='tcard-title' and text()='Разговорчивый']"

    # Не активный тариф утешительный
    NONE_ACTIVE_CARD_UTESHITELNI = By.XPATH, ".//div[@class='tcard']/div[@class='tcard-title' and text()='Утешительный']"

    # Не активный тариф глянцевый
    NONE_ACTIVE_CARD_GLANTSEVI = By.XPATH, ".//div[@class='tcard']/div[@class='tcard-title' and text()='Глянцевый']"

    # Информация о тарифе отпускной
    INFO_ABOUT_TARRIFE_OTPUSKNOI = By.XPATH, ".//div[@class='i-title' and text()='Отпускной']/div[@class='i-dPrefix' and text()='Если пришла пора отдохнуть']"

    # Информация о тарифе рабочий
    INFO_ABOUT_TARRIFE_WORKER = By.XPATH, ".//div[@class='i-title' and text()='Рабочий']/div[@class='i-dPrefix' and text()='Для деловых особ, которых отвлекают']"

    # Информация о тарифе сонный
    INFO_ABOUT_TARRIFE_SONNI = By.XPATH, ".//div[@class='i-title' and text()='Сонный']/div[@class='i-dPrefix' and text()='Для тех, кто не выспался']"

    # Информация о тарифе разговорчивый
    INFO_ABOUT_TARRIFE_RAZGOVOCHIVI = By.XPATH, ".//div[@class='i-title' and text()='Разговорчивый']/div[@class='i-dPrefix' and text()='Если мысли не выходят из головы']"

    # Информация о тарифе утешительный
    INFO_ABOUT_TARRIFE_UTESHITELNI = By.XPATH, ".//div[@class='i-title' and text()='Утешительный']/div[@class='i-dPrefix' and text()='Если хочется свернуться калачиком']"

    # Информация о тарифе глянцевый
    INFO_ABOUT_TARRIFE_GLANTSEVI = By.XPATH, ".//div[@class='i-title' and text()='Глянцевый']/div[@class='i-dPrefix' and text()='Если нужно блистать']"

    # Поле ввода телефона
    INPUT_TELEPHONE = By.XPATH, ".//div[@class='np-button']"

    # Поле вводы способа оплаты
    INPUT_VAR_OF_PAY = By.XPATH, ".//div[@class='pp-button filled']"

    # Поле ввода комментария водителю
    COMMENT_TO_DRIVER = By.XPATH, ".//div[@class='input-container']/input[@id='comment']"

    # Раздел с выбором требований к заказу
    REQUIREMENTS_TO_THE_ORDER = By.XPATH, ".//div[@class='reqs']"

    # Чекбокс столик для ноутбука
    CHECKBOX_TABLE = By.XPATH, ".//*[@class='slider round']"

    # Кнопка вызова такси
    BUTTON_INPUT_NUMBER_OF_ORDER = By.XPATH, ".//button/span[text()='Ввести номер и заказать']"

    # Стоимость активного тарифа
    PRICE_OF_ACTIVE_TARIFF = By.XPATH, ".//div[@class='tcard active']//div[@class='tcard-price']"

    # Иконка i
    ICON_I_TARIFF = By.XPATH, ".//div[@class='tcard active']/button[@class = 'i-button tcard-i active']"

    # Название тарифа в инфо
    TITLE_INFO_ABOUT_TARIFF = By.XPATH, ".//div[@class='tcard active']//div[@class='i-title']"

    # Описание тарифа в инфо
    DESCRIPTION_ABOUT_TARIFF = By.XPATH, ".//div[@class='tcard active']//div[@class='i-dPrefix']"
