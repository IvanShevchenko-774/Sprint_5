
import random
import string
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def generate_unique_email():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"ui_test_{int(time.time())}_{suffix}@example.com"

def generate_unique_pass():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"pass_{int(time.time())}_{suffix}"


class TestRegistration:
    def test_register_new_user(self, driver):
        email = generate_unique_email()
        password = generate_unique_pass()
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Нет аккаунта')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "submitPassword").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Создать аккаунт']").click()
        user = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profileText")))
        assert user.is_displayed()