
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestRegistration:
    def test_register_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Нет аккаунта')]").click()
        driver.find_element(By.NAME, "email").send_keys('ivan1100@gmail.ru')
        driver.find_element(By.NAME, "password").send_keys('123123')
        driver.find_element(By.NAME, "submitPassword").send_keys('123123')
        driver.find_element(By.XPATH, "//button[text()='Создать аккаунт']").click()
        error_element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'input_span__') and text()='Ошибка']")))
        assert error_element.is_displayed()