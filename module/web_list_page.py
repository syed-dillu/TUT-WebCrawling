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
import random


dir = os.getcwd()
sys.path.append(dir)

from utils.launch import Initiate
from elements import webElements
from excel_data.crawl_data import *
from helper import *
from utils.operate import click_element, sendkeys_element




class Web_List_Page(Initiate):


    def crawl(self):
        self.list_data = ''
        self.website = random.choices(get_excel_url())
        self.trade = random.choices(get_excel_trade())

        
        self.driver.implicitly_wait(50)

        time.sleep(2)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        click_element(web_crawl)

        add_site = self.driver.find_element(By.XPATH, webElements.add_site_xpath)
        click_element(add_site)


        website_url = self.driver.find_element(By.XPATH, webElements.website_url_xpath)
        sendkeys_element(website_url,self.website)

        time.sleep(1)

        trade_el = self.driver.find_element(By.XPATH, webElements.trade_xpath)
        sendkeys_element(trade_el,self.trade)


        crawling_drop = self.driver.find_element(By.XPATH, webElements.crawling_drop_xpath)
        click_element(crawling_drop)


        crawling_select = self.driver.find_element(By.XPATH, webElements.crawling_select_xpath)
        click_element(crawling_select)


        time.sleep(2)

        allure.attach(self.driver.get_screenshot_as_png(), name=f'Screenshot : {"Crawled Data"}', attachment_type=AttachmentType.PNG)

        crawling_btn = self.driver.find_element(By.XPATH, webElements.crawling_btn_xpath)
        click_element(crawling_btn)


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

                crawl_status_element = self.driver.find_element(By.XPATH, webElements.list_crawl_status_xpath)
                crawl__status = crawl_status_element.text

                risk_status_element = self.driver.find_element(By.XPATH,webElements.list_risk_xpath)
                risk_status = risk_status_element.text

                break

        self.list_data = {

            "Case id" :self.case_ID,
            "Crawled Website" :web_url,
            "Trade Name" : trade_name,
            "Created date" : "Check the  CREATED DATE & TIME ",
            "Crawling Percentage" :percent_crawl,
            "Crawling Status" : crawl__status,
            "Risk status" : risk_status,
            "Risk score" :risk_score,

        }

        results = []

        for key, value in self.list_data.items():
            print(getLine())
            print(f'✔ {key} : {value}')

            if not value:
                result_status = "Failed"
            else:
                result_status = "Pass"

            print(getLine())

            results.append({
                'Test Scenario': 'Check web crawl list page',
                'Test Case':f'✔ Check =  [ {key} ]  =  Present or Not',
                'Input data': f'✔ Website :  {self.website}  /     Trade :  {self.trade} ',
                'Actual output': f'✔ {key}    :   [ {value} ]  =  Present',
                'Expected output': f'✔ [ {key} ]  should present',
                'Result': result_status
            })

        webform = pd.DataFrame(results)

        with pd.ExcelWriter(crawl_output,mode='a', if_sheet_exists='replace' ,  engine='openpyxl' ) as writer:
            webform.to_excel(writer,sheet_name='Web listing page')

if (__name__) == "__main__":
    crawl = Web_List_Page()
    crawl.browser()
    crawl.login()
    crawl.crawl()

