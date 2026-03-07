from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import platform

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# ✅ В версии 4.x просто вызываем install() — os_type больше не нужен
driver_path = ChromeDriverManager().install()

# 🔓 macOS: снимаем карантин, чтобы не было "zsh: killed"
if platform.system() == "Darwin":
    subprocess.run(["xattr", "-cr", driver_path], check=False, capture_output=True)

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print("✅ Успех! Заголовок:", driver.title)
driver.quit()