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
from utils.operate import click_element, sendkeys_element
from elements import webElements
from excel_data.crawl_data import *
from helper import *


class Web_Crawl_Results(Initiate):

    def crawl(self):
        
        self.website = random.choices(get_excel_url())
        self.trade = random.choices(get_excel_trade())
        
        self.driver.implicitly_wait(50)

        time.sleep(2)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        click_element(web_crawl)

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

    def crawl_result(self):

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

                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(case_id)).click()


                scroll_script = "window.scrollTo(0, 3000);"
                self.driver.execute_script(scroll_script)
            

                time.sleep(4)

                trade_element = self.driver.find_element(By.XPATH, webElements.trade_crawl_xpath)
                trade_Nm = trade_element.text.strip().replace('\n', ' : ')


                crawl_status_element = self.driver.find_element(By.XPATH, webElements.crawl_status_xpath)
                crawl_status = crawl_status_element.text.strip().replace('\n', ' : ')


                risk_status_element = self.driver.find_element(By.XPATH, webElements.risk_status_xpath)
                risk__status = risk_status_element.text.strip().replace('\n', ' : ')


                mcc_element = self.driver.find_element(By.XPATH,webElements.mcc_buss_xpath)
                crawl_mcc_data = mcc_element.text.strip().replace('\n', ' : ')

                mcc_risk_element = self.driver.find_element(By.XPATH,webElements.mcc_risk_xpath)
                crawl_risk = mcc_risk_element.text.strip().replace('\n', ' : ')


                mcc_trans_element = self.driver.find_element(By.XPATH, webElements.mcc_trans_xpath)
                crawl_mcc_trans = mcc_trans_element.text.strip().replace('\n', ' : ')


                phone_element = self.driver.find_element(By.XPATH, webElements.phone_track_xpath)
                crawl_phone = phone_element.text.strip().replace('\n', ' : ')

                email_element = self.driver.find_element(By.XPATH, webElements.email_track_xpath)
                crawl_email = email_element.text.strip().replace('\n', ' : ')


                element_xpath = webElements.scroll_element
                element = self.driver.find_element(By.XPATH, element_xpath)

                scroll_script = """
                arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
                """
                self.driver.execute_script(scroll_script, element)

             
                time.sleep(2)

                scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
                self.driver.execute_script(scroll_script)


                time.sleep(3)


                contact_profiel = self.driver.find_element(By.XPATH, webElements.contact_profile_xpath)
                click_element(contact_profiel)


                allure.attach(self.driver.get_screenshot_as_png(), name=f'Screenshot : {"Contact Data"}', attachment_type=AttachmentType.PNG)
                
                contact_element = self.driver.find_element(By.XPATH,webElements.contact_url_xpath)
                contact_url_crawled = contact_element.text.strip().replace('\n', ' : ')
                print(getLine())
                
                phone_data_element = self.driver.find_element(By.XPATH,webElements.phone_data_xpath)
                phone_data_crawled = phone_data_element.text.strip().replace('\n', ' : ')

                eamil_data_element = self.driver.find_element(By.XPATH, webElements.email_data_xpath)
                email_data_crawl = eamil_data_element.text.strip().replace('\n', ' : ')
 
                break

        
                
        self.client_crawl = {
            "Crawled Website" :self.website,
            "Trade Name" : self.trade,
            "Case id" : self.case_ID,
            "Risk Triggered" : risk_score,
            "Crawling Percentage" :percent_crawl,
            "Crawling Status" : crawl_status,
            "Risk status" :risk__status,
            "MCC Business" : crawl_mcc_data,
            "MCC Risk" :crawl_risk,
            "Website belongs MCC" :crawl_mcc_trans,
            "Crawled Trade Name" : trade_Nm,
            "Contact url" : contact_url_crawled,
            "Phone status" :crawl_phone,
            "Email status" :crawl_email,
            "Crawled Phone" : phone_data_crawled,
            "Crawled Email" : email_data_crawl
        }
        print(getLine())
        print("✔ Client Crawled Data •··················•·····················•")
        print(getLine())

        results = []


        for key, value in self.client_crawl.items():
            print(getLine())
            print(f'✔ {key} : {value}')
            print(getLine())
            if not value:
                result_status = "Failed"
            else:
                result_status = "Pass"



            results.append({

                'Test Scenario': '✔ Check crawl results',
                'Test Case':f'✔ Check  =  [ {key} ]  =  present or not',
                'Input data': f'✔ Website : {self.website}   /   Trade : {self.trade} ',
                'Actual output': f'✔  {key}   :  [ {value} ]  =  present ',
                'Expected output' : f'✔ [ {key} ] =  should present ',
                'Result': result_status

            })
            
            webform = pd.DataFrame(results)

            with pd.ExcelWriter(crawl_output, mode='a', if_sheet_exists='replace', engine='openpyxl')as writer:
                webform.to_excel(writer,sheet_name='Crawl Results')


if (__name__) == "__main__":
    crawl = Web_Crawl_Results()
    crawl.browser()
    crawl.login()
    crawl.crawl()
    crawl.crawl_result()

