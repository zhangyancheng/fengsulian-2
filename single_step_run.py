import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

class MyTest(unittest.TestCase):

    #定位器1
    login_username_loc = (By.ID, "usernam")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.CSS_SELECTOR, "input[class = 'btn_com btn_blue login_btn_submit sy_in']")
    #定位器2
    user_login_success_loc = (By.XPATH, "//div[1]/div[1]/div[1]/div/div[1]/div[1]/span")

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.fengsulian.com/login")

    def element_wait(self,css, secs=8):
        """
        显示等待，判断元素是否存在
        """
        by = css[0].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)
        if by == "id":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "name":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "class name":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "link text":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        elif by == "css selector":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(css), messages)
        else:
            #变量名不存在
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def login_username(self):
        """要传入多个值，用位置参数常用于元组"""
        self.element_wait(css=self.login_username_loc)
        self.driver.find_element(*self.login_username_loc).clear()
        self.driver.find_element(*self.login_username_loc).send_keys("15868147450")
    def login_password(self):
        self.element_wait(css=self.login_password_loc)
        self.driver.find_element(*self.login_password_loc).clear()
        self.driver.find_element(*self.login_password_loc).send_keys("12345678")
    def login_button(self):
        self.element_wait(css=self.login_button_loc)
        self.driver.find_element(*self.login_button_loc).click()
    def login_success(self):
        self.element_wait(css=self.user_login_success_loc)
        return self.driver.find_element(*self.user_login_success_loc).text

    def test_login1(self):
        self.login_username()
        self.login_password()
        self.login_button()
        self.assertEqual(self.login_success(),"FSL_62223599   ")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__mian__":
    unittest.main()
