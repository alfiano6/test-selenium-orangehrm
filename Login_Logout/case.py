import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from page import elem
from page import link
from data import input

class TestLL(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.quit()

    # Test Case 1 (LOG1) Valid Username and Password
    def log1(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys(input.username)
        password = driver.find_element(By.NAME, elem.password).send_keys(input.password)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.dashboard_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.top_header).text
        self.assertIn('Dashboard', response_data)

    # Test Case 2 (LOG2) Invalid Username
    def log2(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys(input.upcase_username)
        password = driver.find_element(By.NAME, elem.password).send_keys(input.password)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.dashboard_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.inv_cred).text
        self.assertIn(input.inv_cred, response_data) 

    # Test Case 3 (LOG3) Invalid Password
    def log3(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys(input.username)
        password = driver.find_element(By.NAME, elem.password).send_keys(input.wrong_password)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.inv_cred).text
        self.assertIn(input.inv_cred, response_data)

    # Test Case 4 (LOG4) Blank Field
    def log4(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys("")
        password = driver.find_element(By.NAME, elem.password).send_keys("")
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.required).text
        self.assertIn(input.required, response_data)

    # Test Case 5 (LOG5) Blank Username with Valid Password
    def log5(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys("")
        password = driver.find_element(By.NAME, elem.password).send_keys(input.password)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.required).text
        self.assertIn(input.required, response_data)

    # Test Case 6 (LOG6) Valid username with Blank Password
    def log6(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys(input.password)
        password = driver.find_element(By.NAME, elem.password).send_keys("")
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.required).text
        self.assertIn(input.required, response_data)

    # Test Case 7 (LOG7) Logout Successfully
    def log7(self):
        driver = self.browser
        driver.maximize_window()
        driver.get(link.base_url)
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username).send_keys(input.username)
        password = driver.find_element(By.NAME, elem.password).send_keys(input.password)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.btn_login).click()
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, elem.user_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, link.logout).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME, elem.login_page).text
        self.assertIn(input.login_title, response_data)