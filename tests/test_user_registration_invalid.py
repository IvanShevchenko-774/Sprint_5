
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import generate_unique_email_invalid, generate_unique_pass_invalid



class TestRegistrationInvalid:
    def test_register_with_invalid_email_format(self, driver):
        email = generate_unique_email_invalid()
        password = generate_unique_pass_invalid()
        
        driver.get(URL)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGIN_AND_SIGNUP_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(EMAIL_FIELD)).send_keys(email)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SUBMIT_PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(EMAIL_ERROR)).is_displayed()