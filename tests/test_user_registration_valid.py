

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import generate_unique_email, generate_unique_pass
from constant import *



class TestRegistration:
    def test_register_new_user(self, driver):
        email = generate_unique_email()
        password = generate_unique_pass()
        driver.get(URL)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_AND_SIGNUP_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(EMAIL_FIELD))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(EMAIL_FIELD)).send_keys(email)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SUBMIT_PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME)).is_displayed()