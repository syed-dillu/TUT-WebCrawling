
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import sys
import os
import random

dir = os.getcwd()
sys.path.append(dir)

from utils.launch import Initiate,environ
from elements import webElements
from excel_data.crawl_data import *
from excel_data.check_excel import write_excel

from helper import *


class Web_List_Page(Initiate):

    def crawl(self):
        
        self.list_data = ''
        self.website = random.choices(get_excel_url())
        self.trade = random.choices(get_excel_trade())

        self.driver.implicitly_wait(50)

        time.sleep(2)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

        time.sleep(2)


        for i in range(100):
            time.sleep(3)

            risk_trigger_element = self.driver.find_element(By.XPATH, webElements.risk_xpath)
            percent_trigger_element = self.driver.find_element(By.XPATH, webElements.percent_xpath)

            ActionChains(self.driver).move_to_element(risk_trigger_element).perform()
            time.sleep(1)

            percent_crawl = percent_trigger_element.text
            risk_score = risk_trigger_element.text
            
            
            if risk_trigger_element.text == "0":

                time.sleep(6)
                self.driver.refresh()

            else:

                print(getLine())                
                time.sleep(2)

                case_id = self.driver.find_element(By.XPATH, webElements.link_xpath)
                self.case_ID = case_id.text

                web_element = self.driver.find_element(By.XPATH, webElements.list_weburl_xpath)
                web_url = ''

                trade_element = self.driver.find_element(By.XPATH, webElements.list_trade_xpath)
                trade_name = trade_element.text

                list_crawlstart = self.driver.find_element(By.XPATH, webElements.list_crawlstart_xpath)
                ActionChains(self.driver).move_to_element(risk_trigger_element).perform()

                crawl_start = list_crawlstart.text


                crawl_status_element = self.driver.find_element(By.XPATH, webElements.list_crawl_status_xpath)
                crawl__status = crawl_status_element.text

                crawl_time_element = self.driver.find_element(By.CSS_SELECTOR, webElements.list_time_taken)
                crawl_time = crawl_time_element.text

                risk_status_element = self.driver.find_element(By.XPATH,webElements.list_risk_xpath)
                risk_status = risk_status_element.text

                allure.attach(self.driver.get_screenshot_as_png(),name = "Screenshot - Crawling list page",attachment_type=AttachmentType.PNG)
                time.sleep(1)

                Web_List_Page.logout(self)

                break

        self.list_data = {

            "Case id" :self.case_ID,
            "Crawled Website" :web_url,
            "Trade Name" : trade_name,
            "Created date" : crawl_start,
            "Crawling Percentage" :percent_crawl,
            "Crawling Time taken": crawl_time,
            "Crawling Status" : crawl__status,
            "Risk status" : risk_status,
            "Risk score" :risk_score,


        }

        

        results = []

        for i, (key, value) in enumerate(self.list_data.items(), start=1):
            print(getLine())
            print(f'✔ {key} : {value}')

            if not value:
                result_status = "Failed"
            else:
                result_status = "Pass"

            print(getLine())

            results.append({
                "Test Case ID" :f'TC_00{i}',
                'Test Scenerio': f'✔ Verify :\n[ {key} ] Present or Not',
                'Preconditions':f'User is logged in and on the Web Crawling Listing page',
                'Test Steps':f'1. Click on the Web Crawling button\n2. In listing page verify :\n[ {key} ]',
                'Actual output': f'✔ {key}  :\n[ {value} ]  Present',
                'Expected output': f'✔ [ {key} ] \nshould present',
                'Result': result_status,
                'Test Environment':environ,
                'Priority':'Medium',
            })

            write_excel(results,'Web Listing Page')




if (__name__) == "__main__":
    crawl = Web_List_Page()
    crawl.browser()
    crawl.login()
    crawl.crawl()

