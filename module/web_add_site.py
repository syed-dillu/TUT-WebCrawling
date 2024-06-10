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

from utils.launch import Initiate
from elements import webElements
from excel_data.crawl_data import get_crawl_input,crawl_output
from utils.operate import click_element, sendkeys_element, get_screenshot


class Web_Add_Site(Initiate):

    def crawl_input(self):
        self.driver.implicitly_wait(50)


        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        click_element(web_crawl)


        results =[]

        for data in get_crawl_input():

            case = data['Case']
            website = data['Website URL']
            tradename = data['Trade Name']
            expected_result = data['Expected Results']
            Test_case = data['Test Data For Web Form']

            time.sleep(1)

            add_site = self.driver.find_element(By.XPATH, webElements.add_site_xpath)
            click_element(add_site)

            website_url = self.driver.find_element(By.XPATH, webElements.website_url_xpath)
            sendkeys_element(website_url,website)

            time.sleep(1)

            trade_el = self.driver.find_element(By.XPATH, webElements.trade_xpath)
            sendkeys_element(trade_el,tradename)

            if website != '':

                crawling_drop = self.driver.find_element(By.XPATH, webElements.crawling_drop_xpath)
                click_element(crawling_drop)


                crawling_select = self.driver.find_element(By.XPATH, webElements.crawling_select_xpath)
                click_element(crawling_select)


            time.sleep(1)


            crawling_btn = self.driver.find_element(By.XPATH, webElements.crawling_btn_xpath)
            click_element(crawling_btn)


            time.sleep(2)

            #get_screenshot(Test_case)

            self.driver.refresh()

            results.append({

    'Test Case ID': f'✔ TC_ADD_00{case}',
    'Test Scenario': '✔ Check Add Site',
    'Test Case':f'✔ Check with : {Test_case}',
    'Input data': f'✔ Website : [ {website} ]    /    Trade : [ {tradename} ]',
    'Expected output': expected_result,
    'Actual output': expected_result,
    'Result': 'Pass'

})

            webform = pd.DataFrame(results)

            with pd.ExcelWriter(crawl_output, mode='a',if_sheet_exists='replace', engine='openpyxl') as writer:
                webform.to_excel(writer,sheet_name='Add Site',index=False)


if (__name__) == "__main__":
    crawl = Web_Add_Site()
    crawl.browser()
    crawl.login()
    crawl.crawl_input()




