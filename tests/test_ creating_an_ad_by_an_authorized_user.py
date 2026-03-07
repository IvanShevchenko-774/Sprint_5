import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
from locators import *


class TestAdCreation:
    def test_create_ad_authorized(self, authorized_driver):
        WebDriverWait(authorized_driver, 100).until(expected_conditions.visibility_of_element_located(CREATE_AD_BUTTON))
        WebDriverWait(authorized_driver, 100).until(expected_conditions.element_to_be_clickable(CREATE_AD_BUTTON )).click()
        title = f"Стигмата{random.randint(100, 999)}"
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_TITLE_FIELD)).send_keys(title)
        discription = f"Корень сельдерея{random.randint(100, 999)}"
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_DESCRIPTION_FIELD)).send_keys(discription)
        price = random.randint(100, 9099)
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_PRICE_FIELD)).send_keys(price)
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_CONDITION_NEW))
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_CONDITION_BY)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_CATEGORY_ARROW)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_CATEGORY_BOOKS)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_CITY_ARROW)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_CITY_SPB)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_PUBLISH_BUTTON)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(USER_AVATAR)).click()
        WebDriverWait(authorized_driver, 10).until(expected_conditions.visibility_of_element_located((MY_ADS_TITLE)))
        while True:
            try:
                next_button = WebDriverWait(authorized_driver, 10).until(expected_conditions.element_to_be_clickable(AD_ARROW_BUTTON_RIGHT))
                next_button.click()

            except TimeoutException:
                break
        ads = WebDriverWait(authorized_driver, 10).until(expected_conditions.presence_of_all_elements_located(AD_CARDS))
        last_ad_title = ads[-1].find_element(*AD_CARD_TITLE).text
        assert last_ad_title == title
