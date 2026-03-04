
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_login_success(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
        driver.find_element(By.NAME, "email").send_keys('ivan1100@gmail.ru')
        driver.find_element(By.NAME, "password").send_keys('123123')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        user = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profileText")))
        assert user.is_displayed()