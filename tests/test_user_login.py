
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from constant import *


class TestLogin:
    def test_login_success(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_AND_SIGNUP_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((EMAIL_FIELD)))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(EMAIL_FIELD)).send_keys(USER_EMAIL)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PASSWORD_FIELD)).send_keys(USER_PASSWORD)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((USER_NAME))).is_displayed()