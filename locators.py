from selenium.webdriver.common.by import By


class Locators:

    NAME = (
        By.XPATH,
        "//label[contains(text(), 'Имя')]/following-sibling::input"
    )  # локатор поля Имя в форме регистрации
    EMAIL = (
        By.XPATH,
        "//label[contains(text(), 'Email')]/following-sibling::input"
    )  # локатор поля Email в форме регистрации
    PASSWORD = (
        By.XPATH,
        "//label[contains(text(), 'Пароль')]/following-sibling::input"
    )  # локатор поля Пароль в форме регистрации
    REGISTRATION_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']"
    )  # локатор кнопки Зарегистрироваться
    PASSWORD_ERROR_MESSAGE = (
        By.XPATH,
        "//p[@class='input__error text_type_main-default']"
    )  # локатор сообщения об ошибке пароля
    FIELD_EMAIL = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @name='name']"
    )  # локатор поля Email в форме авторизации
    FIELD_PASSWORD = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"
    )  # локатор поля Пароль в форме авторизации
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )  # локатор кнопки Войти на странице авторизации
    BUTTON_PLACE_AN_ORDER = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )  # локатор кнопки Оформить заказ на главной странице, для ожидания
    LOGIN_BUTTON_MAIN_PAGE = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )  # локатор кнопки Войти в аккаунт
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
    )  # локатор кнопки Личный Кабинет
    REG_FORM_AND_FGT_PSW_LOG_BTN = (
        By.CSS_SELECTOR,
        '.Auth_link__1fOlj'
    )  # локатор кнопок Войти на странице регистрации и странице восстановления пароля
    PROFILE = (
        By.XPATH,
        "//a[text()='Профиль']"
    )  # локатор кнопки Профиль
    CONSTRUCTOR = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"
    )  # локатор кнопки Конструктор
    LOGO = (
        By.CSS_SELECTOR,
        '.AppHeader_header__logo__2D0X2')
    # локатор лого Stellar Burgers
    LOG_OUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )  # локатор кнопки Выйти на странице Личного Кабинета
    BUNS = (
        By.XPATH,
        "//span[text()='Булки']"
    )  # локатор раздела Булки
    BUNS_PARENT = (
        By.XPATH,
        "//span[text()='Булки']/parent::div"
    )  # локатор родителя раздела Булки
    SAUCES = (
        By.XPATH,
        "//span[text()='Соусы']"
    )  # локатор раздела Соусы
    SAUCES_PARENT = (
        By.XPATH,
        "//span[text()='Соусы']/parent::div"
    )  # локатор родителя раздела Соусы
    FILLINGS = (
        By.XPATH,
        "//span[text()='Начинки']"
    )  # локатор раздела Начинки
    FILLINGS_PARENT = (
        By.XPATH,
        "//span[text()='Начинки']/parent::div"
    )  # локатор родителя раздела Начинки
    SECTION_CLASS = 'tab_tab_type_current__2BEPc'  # значение класса для проверки разделов «Булки», «Соусы», «Начинки».
