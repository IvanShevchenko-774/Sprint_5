from selenium.webdriver.common.by import By

# Базовый URL
URL = 'https://qa-desk.stand.praktikum-services.ru'

LOGIN_AND_SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
EMAIL_FIELD = (By.NAME, "email")
PASSWORD_FIELD = (By.NAME, "password")
SUBMIT_PASSWORD_FIELD = (By.NAME, "submitPassword")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
USER_NAME = (By.XPATH, "//h3[contains(@class, 'profileText') and contains(@class, 'name') and contains(text(), 'User.')]")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
EMAIL_ERROR = (By.XPATH, "//span[contains(@class, 'input_span__') and text()='Ошибка']")
CREATE_AD_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and text()='Разместить объявление']")
AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(@class, 'h1')]")
LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btnSmall.spanGlobal[type='button']")
AD_ARROW_BUTTON_RIGHT = (By.CSS_SELECTOR, ".arrowButton--right:not([disabled])")
AD_CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button")
AD_CATEGORY_BOOKS = (By.XPATH, "//button[.//span[contains(text(), 'Книги')]]")
AD_CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button")
AD_CITY_SPB = (By.XPATH, "//button[.//span[contains(text(), 'Санкт-Петербург')]]")
AD_CONDITION_NEW = (By.XPATH, "//input[@value='Новый']/following-sibling::div")
AD_CONDITION_BY = (By.XPATH, "//input[@value='Б/У']/following-sibling::div")
MY_ADS_TITLE = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
AD_CARDS = (By.CSS_SELECTOR, ".card")
AD_CARD_TITLE = (By.CSS_SELECTOR, ".h2")
USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
AD_ARROW_BUTTON_RIGHT = (By.CSS_SELECTOR, ".arrowButton--right:not([disabled])")
AD_PUBLISH_BUTTON = (By.XPATH, "//button[contains(., 'Опубликовать')]")
AD_TITLE_FIELD = (By.NAME, "name")
AD_DESCRIPTION_FIELD = (By.CLASS_NAME, "textarea_inputStandart__IoNxq.spanGlobal")
AD_PRICE_FIELD = (By.NAME, "price")

