import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page import elem
from page import link
from data import input

def success(driver):
    driver.get(link.base_url)
    time.sleep(3)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys(input.username)
    driver.find_element(By.NAME, elem.password).send_keys(input.password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)