import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_register():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://pushing-it.vercel.app/")

    time.sleep(3)

    web_element = driver.find_element(By.ID, "user")
    web_element.send_keys("Tina" + Keys.ENTER)

    web_element = driver.find_element(By.ID, "pass")
    web_element.send_keys("tina123" + Keys.ENTER)

    web_element = driver.find_element(By.ID, "radio-:r5:")
    web_element.click()

    female_button = driver.find_element(By.ID, "radio-:r5:")
    driver.execute_script("arguments[0].click();", female_button)

    time.sleep(3)

    driver.quit()
