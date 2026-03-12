
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from constant import *


class TestSing:
    def test_unauthorized_user_cannot_create_ad(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(CREATE_AD_BUTTON)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AUTH_MODAL_TITLE)).is_displayed()