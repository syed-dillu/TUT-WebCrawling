from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
from openpyxl.styles import Alignment
import pandas as pd
import sys
import os


dir = os.getcwd()
sys.path.append(dir)

from utils.launch import Initiate, environ,url_tut
from elements import webElements
from excel_data.crawl_data import *
from excel_data.check_excel import write_excel
from utils.operate import click_element, sendkeys_element, get_screenshot

from helper import *

class File_Upload(Initiate):
    file_data = ''


    def crawl(self):


        self.driver.implicitly_wait(50)
        time.sleep(2)
        profile_email = self.driver.find_element(By.XPATH, webElements.profile_email_xpath)
        click_element(profile_email)

        Profile_click = self.driver.find_element(By.XPATH, webElements.Profile_xpath)
        click_element(Profile_click)
        profile_text = Profile_click.text
        print(profile_text)

        account_sett = self.driver.find_element(By.XPATH, webElements.account_setting_xpath)
        click_element(account_sett)
        account_text = account_sett.text
        print(account_text)

        time.sleep(2)

        file_upload_limit = self.driver.find_element(By.XPATH, webElements.file_upload_limit_xpath)
        file_upload_limit_txt = file_upload_limit.text
        print("limit",file_upload_limit_txt)
        
        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

        file_upload_element = self.driver.find_element(By.XPATH,webElements.file_upload_xpath)
        click_element(file_upload_element)

        time.sleep(1)

        download_sample_element = self.driver.find_element(By.XPATH,webElements.down_load_xpath)
        click_element(download_sample_element)

        time.sleep(1)

        file_results = ["No data found",f"Maximum {file_upload_limit_txt}","File uploaded successfully"]

        for i in range(len(crawl_file_upload)):

            file_upload_btn= self.driver.find_element(By.ID,webElements.file_upload_btn_xpath)
            time.sleep(1)
            file_upload_btn.send_keys(crawl_file_upload[i])
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(),name = f"Screenshot - File Upload",attachment_type=AttachmentType.PNG)
            time.sleep(1)

            if i >= 2 :

                try:
                    file_ok = self.driver.find_element(By.XPATH,webElements.file_upload_ok_btn)
                    click_element(file_ok)
                except Exception as e:
                    print(e)

                if i >=3:

                    time.sleep(2)
                    file_eye_element = self.driver.find_element(By.XPATH,webElements.file_upload_eye_xpath)
                    click_element(file_eye_element)
                    time.sleep(2)
                    allure.attach(self.driver.get_screenshot_as_png(),name = f"Screenshot - File Upload",attachment_type=AttachmentType.PNG)
                    time.sleep(1)

                    file_failure = self.driver.find_element(By.XPATH,webElements.file_failure_xpath)
                    file_failure_txt = file_failure.text

                    if file_failure_txt != '':

                        file_results.append(file_failure_txt)
                        self.driver.refresh()
                        time.sleep(1)


                time.sleep(1)
        print("file datas are",file_results)

        File_Upload.logout(self)


        self.file_data = [
            "Empty File",
            "Upload File More than the File upload limit",
            "File Upload with valid data of 10 ",
            "File Upload Without enter the URL ",
            "File Upload Without enter Trade Name ",
            "File Upload Without select Crawl Type ",
        ]
        results = []
        for i, (key, case) in enumerate(zip(self.file_data,file_results), start=1):

            if i == 1:
                results.append({
                "Test Case ID" :f'TC_000',
                'Test Scenerio': f'✔ Verify :\nFile upload limit',
                'Preconditions':f'User is logged in and purchase web crawling product',
                'Test Steps':f'1. Click on the my profile -> Account Settings \n3. Verify the file uploaded limit',
                'Actual output': f'[ {file_upload_limit_txt} ] ',
                'Expected output': f'✔ [ {file_upload_limit_txt} ] ',
                'Test Environment':environ,
                'Priority':'Medium',
            })
            
            results.append({
                "Test Case ID" :f'TC_00{i}',
                'Test Scenerio': f'✔ Verify :\n[ {key} ]',
                'Preconditions':f'User is logged in and purchase web crawling product',
                'Test Steps':f'1. Click on the file upload button\n2. [ {key} ] \n3. Verify the file uploaded status',
                'Actual output': f'[ {case} ]',
                'Expected output': f'✔ [ {case} ]',
                'Test Environment':environ,
                'Priority':'Medium',
            })

            write_excel(results,"File Upload")



    
if (__name__) == "__main__":

    file = File_Upload()
    file.browser()
    file.login()
    file.crawl()


    time.sleep(5)