
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSing:
    def test_unauthorized_user_cannot_create_ad(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(By.CLASS_NAME, "buttonPrimary.inButtonText.undefined.inButtonText").click()
        name = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH , "/html/body/div/div/div[2]/div[5]/form/div[1]/h1")))
        assert name.is_displayed()