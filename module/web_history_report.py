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

from utils.launch import Initiate,environ
from elements import webElements
from excel_data.crawl_data import *
from excel_data.check_excel import write_excel
from helper import *
from utils.operate import click_element, sendkeys_element


class Web_History_Page(Initiate):

    def crawl(self):

        self.list_data = ''
        self.website = random.choices(get_excel_url())
        self.trade = random.choices(get_excel_trade())

        self.driver.implicitly_wait(50)

        time.sleep(2)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

        # add_site = self.driver.find_element(By.XPATH, webElements.add_site_xpath)
        # click_element(add_site)

        # website_url = self.driver.find_element(By.XPATH, webElements.website_url_xpath)
        # sendkeys_element(website_url,self.website)

        # time.sleep(1)

        # trade_el = self.driver.find_element(By.XPATH, webElements.trade_xpath)
        # sendkeys_element(trade_el,self.trade)

        # crawling_drop = self.driver.find_element(By.XPATH, webElements.crawling_drop_xpath)
        # click_element(crawling_drop)

        # crawling_select = self.driver.find_element(By.XPATH, webElements.crawling_select_xpath)
        # click_element(crawling_select)

        # time.sleep(2)

        # allure.attach(self.driver.get_screenshot_as_png(), name=f'Screenshot : {"Crawled Data"}', attachment_type=AttachmentType.PNG)

        # crawling_btn = self.driver.find_element(By.XPATH, webElements.crawling_btn_xpath)
        # click_element(crawling_btn)

        time.sleep(2)

        for i in range(100):
            time.sleep(3)

            risk_trigger_element = self.driver.find_element(By.XPATH, webElements.risk_xpath)
            percent_trigger_element = self.driver.find_element(By.XPATH, webElements.percent_xpath)

            ActionChains(self.driver).move_to_element(risk_trigger_element).perform()
            time.sleep(1)

            percent_crawl = percent_trigger_element.text
            risk_score = risk_trigger_element.text
            print("the risk score is", risk_score)
            
            
            if risk_trigger_element.text == "0":

                time.sleep(6)
                self.driver.refresh()

            else:

                print(getLine())                
                time.sleep(2)

                case_id = self.driver.find_element(By.XPATH, webElements.link_xpath)
                case_ID = case_id.text

                web_element = self.driver.find_element(By.XPATH, webElements.list_weburl_xpath)
                web_url = web_element.text

                trade_element = self.driver.find_element(By.XPATH, webElements.list_trade_xpath)
                trade_name = trade_element.text

                list_crawlstart = self.driver.find_element(By.XPATH, webElements.list_crawlstart_xpath)
                ActionChains(self.driver).move_to_element(risk_trigger_element).perform()

                crawl_start = list_crawlstart.text

                crawl_status_element = self.driver.find_element(By.XPATH, webElements.list_crawl_status_xpath)
                crawl__status = crawl_status_element.text

                risk_status_element = self.driver.find_element(By.XPATH,webElements.list_risk_xpath)
                risk_status = risk_status_element.text
                print("the risk status is", risk_status)

                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(),name = f"Screenshot - Web Listing Page",attachment_type=AttachmentType.PNG)
                time.sleep(1)



                break

        self.list_data = [
                case_ID,
                web_url,
                trade_name,
                crawl_start,
                crawl__status,
                risk_status,
                risk_score
    ]
        
    def history_report(self):
        
        self.report_list_data = ''

        self.driver.implicitly_wait(50)

        time.sleep(2)

        reports_element = self.driver.find_element(By.XPATH, webElements.reports_xpath)
        click_element(reports_element)

        his_reports_element = self.driver.find_element(By.LINK_TEXT, webElements.his_reports_xpath)
        click_element(his_reports_element)

        crawl_his_element = self.driver.find_element(By.XPATH, webElements.crawl_his_xpath)
        click_element(crawl_his_element)

        time.sleep(1)

        view_report_element = self.driver.find_element(By.XPATH, webElements.view_report_xpath)
        click_element(view_report_element)

        reports_link = self.driver.find_element(By.XPATH, webElements.reports_link_xpath)
        case_ID = reports_link.text

        reports_list_weburl = self.driver.find_element(By.XPATH, webElements.reports_list_weburl_xpath)
        web_url = reports_list_weburl.text

        reports_list_createddata = self.driver.find_element(By.XPATH, webElements.reports_list_createddata_xpath)
        created_date = reports_list_createddata.text

        reports_list_crawlstart = self.driver.find_element(By.XPATH, webElements.reports_list_crawlstart_xpath)
        ActionChains(self.driver).move_to_element(reports_list_crawlstart).perform()

        crawlt_start = reports_list_crawlstart.text

        reports_list_trade = self.driver.find_element(By.XPATH, webElements.reports_list_trade_xpath)
        trade_name = reports_list_trade.text

        reports_list_crawl_status = self.driver.find_element(By.XPATH,webElements.reports_list_crawl_status_xpath)
        ActionChains(self.driver).move_to_element(reports_list_crawl_status).perform()
        time.sleep(1)
        crawl__status = reports_list_crawl_status.text


        reports_list_risk = self.driver.find_element(By.XPATH, webElements.reports_list_risk_xpath)
        risk_status = reports_list_risk.text


        reports_list_riskscore = self.driver.find_element(By.XPATH, webElements.reports_list_riskscore_xpath)
        risk_score = reports_list_riskscore.text

        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(),name = f"Screenshot - Crawling Histroy Report",attachment_type=AttachmentType.PNG)
        time.sleep(1)

        Web_History_Page.logout(self)



        self.report_list_data = [
            case_ID,
            web_url,
            trade_name,
            crawlt_start,
            crawl__status,
            risk_status,
            risk_score
        ]

    def validate_report(self):

        self.actual_output = [
            "Case id",
            "Crawled Website",
            "Trade Name",
            "Crawl start date",
            "Crawling Status",
            "Risk level",
            "Risk score"
        ]

        results = []

        for i, (actual,web_list,report_list) in enumerate(zip(self.actual_output,self.list_data,self.report_list_data),start=1):
            print(getLine())
            print(f'✔ Web List : [{web_list}, Report List : {report_list}')

            if web_list != report_list:
                result_status = "Failed"
            else:
                result_status = "Pass"

            print(getLine())

            results.append({
                "Test Case ID" :f'TC_00{i}',
                'Test Scenario': f'Verify [ {actual} ] Should be same in both Crawling Listing page & history report page ',
                'Preconditions':f'User is logged in and on the Web Crawling Listing page and history report page',
                'Test Steps':f'1. Click on the Web Crawling Listing \n2. Check [ {actual} ] present in crawling listing page \n3. Click on the History Report -> Crawling History  \n4. Check [ {actual} ] present in crawling history report',
                'Expected output': f'✔  [ {actual} ]  \nShould be same',
                'Actual Web List output': f'✔  [{web_list}] ',
                'Actual History List output': f'✔ [{report_list}]',
                'Result': result_status,
                'Test Environment':environ,
                'Priority':'Medium',
            })
            write_excel(results,'Validate Listing Data')





if (__name__) == "__main__":
    crawl = Web_History_Page()
    crawl.browser()
    crawl.login()
    crawl.crawl()
    crawl.history_report()
    crawl.validate_report()



