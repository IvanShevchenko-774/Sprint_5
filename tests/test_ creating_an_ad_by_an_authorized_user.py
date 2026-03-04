import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException


class TestAdCreation:
    def test_create_ad_authorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(By.CSS_SELECTOR, ".buttonPrimary").click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "email"))).send_keys('ivan1100@gmail.ru')
        driver.find_element(By.NAME, "password").send_keys('123123')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profileText")))
        driver.find_element(By.CSS_SELECTOR, ".buttonPrimary").click()
        title = f"Стигмата{random.randint(100, 999)}"
        driver.find_element(By.NAME, "name").send_keys(title)
        discription = f"Корень сельдерея{random.randint(100, 999)}"
        driver.find_element(By.CLASS_NAME, "textarea_inputStandart__IoNxq.spanGlobal").send_keys(discription)
        price = random.randint(100, 9099)
        driver.find_element(By.NAME, "price").send_keys(price)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@value='Новый']/following-sibling::div")))
        driver.find_element(By.XPATH, "//input[@value='Б/У']/following-sibling::div").click()
        driver.find_element(By.XPATH, "//input[@name='category']/parent::div/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']").click()
        driver.find_element(By.XPATH, "//span[text()='Книги']/parent::button").click()
        driver.find_element(By.XPATH, "//input[@name='city']/parent::div/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']").click()
        driver.find_element(By.XPATH, "//span[text()='Санкт-Петербург']/parent::button").click()
        driver.find_element(By.XPATH, "//button[contains(., 'Опубликовать')]").click()
        WebDriverWait(driver, 100).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "circleSmall")))
        driver.find_element(By.CLASS_NAME, "circleSmall").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Мои объявления')]")))
        while True:
            try:
                next_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".arrowButton--right:not([disabled]")))
                next_button.click()

            except TimeoutException:
                break
        ads = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".card")))
        last_ad_title = ads[-1].find_element(By.CSS_SELECTOR, ".h2").text
        assert last_ad_title == title
