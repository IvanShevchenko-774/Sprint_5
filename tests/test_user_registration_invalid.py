
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def generate_unique_email():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"ui_test_{int(time.time())}_{suffix}@matroshka"

def generate_unique_pass():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"pass_{int(time.time())}_{suffix}"

class TestRegistrationInvalid:   
    def test_register_with_invalid_email_format(self, driver):
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
        error_element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'input_span__') and text()='Ошибка']")))
        assert error_element.is_displayed()