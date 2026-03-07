import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import *
from helpers import get_existed_user_data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()



@pytest.fixture(scope="function")
def authorized_driver(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_AND_SIGNUP_BUTTON)).click()
    email, password = get_existed_user_data()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(EMAIL_FIELD)).send_keys(email)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PASSWORD_FIELD)).send_keys(password)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON)).click()
    return driver