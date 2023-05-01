import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from page import link
from data import input
from data import addJob 
from data import hal
import login

class ADM(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.close()

    # Test Case 1 (ADM1) Add Job Title Sucessfully
    def ADM1(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Add Job
        driver.find_element(By.XPATH, elem.btn_add_job).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.add_job_title).send_keys(addJob.jobTitle)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_desc).send_keys(addJob.jobDesc1)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_save).click()
        time.sleep(5)

        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/h6").text
        self.assertIn(response_data, 'Job Titles')

    # Test Case 2 (ADM2) Add Job Title Failed
    def ADM2(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Add Job
        driver.find_element(By.XPATH, elem.btn_add_job).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.add_job_title).send_keys(addJob.jobTitle)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_desc).send_keys(addJob.jobDesc2)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_save).click()
        time.sleep(2)

        if driver.find_element(By.XPATH, elem.btn_save).is_enabled():
            print("Can't save, button disabled")
        else:
            print("Button Enable")
        time.sleep(5)

    # Test Case 3 (ADM3) Add Job Title Failed
    def ADM3(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Add Job
        driver.find_element(By.XPATH, elem.btn_add_job).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.add_job_title).send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_desc).send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_save).click()
        time.sleep(2)

        response_url = driver.current_url
        self.assertEqual(response_url, link.addjob_url)
        response_data = driver.find_element(By.XPATH, hal.required).text
        self.assertIn(addJob.required, response_data)

    # Test Case 4 (ADM4) Edit Job Title Sucessfully
    def ADM4(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Edit Job
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.add_job_title).clear()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_title).send_keys(addJob.jobEdit)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_desc).send_keys(addJob.jobDesc3)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_save).click()
        time.sleep(5)

        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/h6").text
        self.assertIn(response_data, 'Job Titles')

    # Test Case 5 (ADM5) Edit Job Title Failed
    def ADM5(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Edit Job
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.add_job_title).send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_desc).send_keys(addJob.jobDesc2)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_save).click()
        time.sleep(2)

        if driver.find_element(By.XPATH, elem.btn_save).is_enabled():
            print("Can't save, button disabled")
        else:
            print("Button Enable")
        time.sleep(5)

    # Test Case 6 (ADM6) Cancel Add Job Title
    def ADM6(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Cancel Add Job
        driver.find_element(By.XPATH, elem.btn_add_job).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.add_job_title).send_keys(addJob.jobTitle1)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.add_job_desc).send_keys(addJob.jobDesc4)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_cancel).click()
        time.sleep(5)

        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/h6").text
        self.assertIn(response_data, 'Job Titles')

    # Test Case 7 (ADM7) Delete Job Title
    def ADM7(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Cancel delete Job
        driver.find_element(By.XPATH, elem.btn_delete).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_fix_delete).click()
        time.sleep(2)

        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/h6").text
        self.assertIn(response_data, 'Job Titles')
    
    # Test Case 8 (ADM8) Cancel Delete Job Title
    def ADM8(self):
        # LOGIN
        driver = self.browser
        login.success(driver)

        # ADMIN MENU
        driver.find_element(By.XPATH, elem.admin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_drop).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.job_title).click()
        time.sleep(1)

        # Cancel delete Job
        driver.find_element(By.XPATH, elem.btn_delete).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_cancel_delete).click()
        time.sleep(2)

        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/h6").text
        self.assertIn(response_data, 'Job Titles')

if __name__ == "__main__":
    unittest.main()