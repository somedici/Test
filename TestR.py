import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def test_register():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://pushing-it.vercel.app/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user").send_keys("Tina" + Keys.ENTER)
    driver.find_element(By.ID, "pass").send_keys("tina123" + Keys.ENTER)

    radio_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "chakra-radio__control")))

    try:
        radio_container.click()
    except:

        driver.execute_script("arguments[0].click();", radio_container)

    time.sleep(3)

    select_file = Select(driver.find_element(By.ID, "day"))
    select_file.select_by_value("2")

    select_file = Select(driver.find_element(By.ID, "month"))
    select_file.select_by_value("4")

    select_file = Select(driver.find_element(By.ID, "year"))
    select_file.select_by_value("1992")

    driver.find_element(By.ID, "submitForm").send_keys(Keys.ENTER)

    time.sleep(5)
    driver.quit()

test_register()

