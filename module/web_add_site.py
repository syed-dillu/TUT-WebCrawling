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
import pandas as pd
import sys
import openpyxl
import os

dir = os.getcwd()

sys.path.append(dir)

from utils.launch import Initiate,environ
from elements import webElements
from excel_data.crawl_data import get_crawl_input,crawl_output
from excel_data.check_excel import write_excel
from utils.operate import click_element, sendkeys_element, get_screenshot


class Web_Add_Site(Initiate):

    def crawl_input(self):
        self.driver.implicitly_wait(50)



        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

        results =[]

        for data in get_crawl_input():

            case = data['Case']
            website = data['Website URL']
            tradename = data['Trade Name']
            address = data['Address']
            crawl_type = data['Crawl Type']

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

            address_el = self.driver.find_element(By.XPATH, webElements.address_add_xpath)
            sendkeys_element(address_el,address)

            crawling_btn = self.driver.find_element(By.XPATH, webElements.crawling_btn_xpath)
            click_element(crawling_btn)


            time.sleep(1)

            allure.attach(self.driver.get_screenshot_as_png(),name = f"Screenshot - {Test_case}",attachment_type=AttachmentType.PNG)
            time.sleep(1)




            #get_screenshot(Test_case)

            time.sleep(2)
            self.driver.execute_script("alert(' Your system is hacked!');")
            time.sleep(2)
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()

            self.driver.refresh()

            if case == 9:
                Web_Add_Site.logout(self)

            results.append({

    'Test Case ID': f'✔ TC_00{case}',
    'Test Scenario': f'✔ Verify with : \n{Test_case}',
    'Preconditions':f'User is logged in and on the Web Crawling -> "Add Site" page',
    'Test Steps':f"1. Click on the 'Add Site' button\n2.  Check with : \n{Test_case}\n3. Click on the 'Submit' button",
    'Input data': f'1. Website : [ {website} ] \n2. Trade : [ {tradename} ] \n3. Crawl Type : [ {crawl_type} ] \n4. Address : [ {address} ]   ',
    'Expected output': expected_result,
    'Actual output': expected_result,
    'Result': 'Pass',
    'Test Environment':environ,
    'Priority':'High',
   
})
            print(results)
            
            write_excel(results,'Add Site')



if (__name__) == "__main__":
    crawl = Web_Add_Site()
    crawl.browser()
    crawl.login()
    crawl.crawl_input()




