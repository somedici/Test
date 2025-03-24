import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://pushing-it.vercel.app/")

    wait = WebDriverWait(driver, 15)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "registertoggle")))
    login_button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "registertoggle")))

    time.sleep(5)

    web_element = driver.find_element(By.ID, "user")
    web_element.send_keys("Tina" + Keys.ENTER)

    web_element = driver.find_element(By.ID, "pass")
    web_element.send_keys("tina123" + Keys.ENTER)

    time.sleep (5)

    driver.quit()

