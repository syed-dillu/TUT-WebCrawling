import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType

from dotenv import load_dotenv
import sys
import allure
import os
myDir = os.getcwd()
sys.path.append(myDir)
from helper import *

load_dotenv()
from elements.loginElements import *
from messages.loginMessage import *

url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

url_web = os.getenv("URL_WEB")
email_web = os.getenv("EMAIL_WEB")
password_web = os.getenv("PASSWORD_WEB")




class Initiate():
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    #driver = webdriver.Edge()
    # driver = webdriver.Safari()

    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    
    def browser(self):
        
        self.driver.implicitly_wait(20)
        print(getLine())

        self.driver.get(url)
        self.driver.maximize_window()
        web_url = self.driver.current_url

        actual_title=self.driver.title
        expected_title = "Tutelar | Risk and Fraud Assessment | Fintech"

        if actual_title == expected_title:
            print(f"✔ Title is correct :  {expected_title}")
            print(getLine())
            assert True

        else:

            allure.attach(self.driver.get_screenshot_as_png(),name="LoginScreen",attachment_type=AttachmentType.PNG)
            print(f"✔ Title is Incorrect :  {actual_title}")
            print(getLine())
            assert False

        if web_url == url:
            print(f"✔ URL is correct : {url}")
            print(getLine())

            assert True
        else:
            print(f"✔ InCorrect URL : {web_url}")
            print(getLine())

            assert False
        
        return 'browser opens successfully'

    def login(self):
        print(login_page)
        print(getLine())

        email_id = self.driver.find_element(By.NAME,login_email)
        email_id.send_keys(email)
        print(f'{email_enter}:{email}')
        print(getLine())

        pass_i = self.driver.find_element(By.NAME, login_pass)
        pass_i.send_keys(password)
        print(f'{password_enter}: *******')
        print(getLine())


        check_box = self.driver.find_element(By.ID, login_check_box)
        check_box.click()
        print(check_box_login)
        print(getLine())
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)

        button = self.driver.find_element(By.XPATH, login_button)
        button.click()
        print(login_button_click)
        print(getLine())
        
        print(login_success)

        # multiple_button = self.driver.find_element(By.XPATH, multiple_login)
        # multiple_button.click()
        print(getLine())
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Dashboard Page", attachment_type=AttachmentType.PNG)



        return 'loggedin successfully'   
    
if (__name__) == ("__main__"):

    s = Initiate()
    s.browser()
    s.login()
    time.sleep(10)

