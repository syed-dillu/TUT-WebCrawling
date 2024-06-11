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


class Web_ODD(Initiate):

    def crawl(self):
        
        self.run_odd_txt = ''
        self.history_odd_txt = ''
        self.history_logs_txt = ''

        self.website = "https://www.shoppersstop.com/"
        self.trade = random.choices(get_excel_trade())

        self.driver.implicitly_wait(50)

        time.sleep(2)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

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
            percent_trigger_element1 = self.driver.find_element(By.XPATH, webElements.percent_xpath)


            ActionChains(self.driver).move_to_element(risk_trigger_element).perform()
            time.sleep(1)

            self.percent_crawl = percent_trigger_element1.text
            self.risk_score = risk_trigger_element.text
            
            
            if risk_trigger_element.text == "0":

                time.sleep(6)
                self.driver.refresh()

            else:

                print(getLine())                
                time.sleep(2)

                case_id = self.driver.find_element(By.XPATH, webElements.link_xpath)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(case_id)).click()

                time.sleep(1)
                break


    def crawl_data(self):

        parent_percent_element = self.driver.find_element(By.XPATH, webElements.child1_percentage_xpath)
        self.parent_per_txt = parent_percent_element.text

        result_type_element = self.driver.find_element(By.XPATH, webElements.result_type_xpath)
        self.result_type_txt = result_type_element.text

        end_date_element = self.driver.find_element(By.XPATH, webElements.end_data_xpath)
        self.end_date_txt = end_date_element.text

        scroll_script = "window.scrollTo(0, 3000);"
        self.driver.execute_script(scroll_script)
    
        time.sleep(4)

        trade_element = self.driver.find_element(By.XPATH, webElements.trade_crawl_xpath)
        self.trade_Nm = trade_element.text.strip().replace('\n', ' : ')

        crawl_status_element = self.driver.find_element(By.XPATH, webElements.crawl_status_xpath)
        self.crawl_status = crawl_status_element.text.strip().replace('\n', ' : ')

        mcc_element = self.driver.find_element(By.XPATH,webElements.mcc_buss_xpath)
        self.crawl_mcc_data = mcc_element.text.strip().replace('\n', ' : ')

        mcc_risk_element = self.driver.find_element(By.XPATH,webElements.mcc_risk_xpath)
        self.crawl_risk = mcc_risk_element.text.strip().replace('\n', ' : ')

        """
            RISK INDICATOR
            Business Risk

        """

        mcc_trans_element = self.driver.find_element(By.XPATH, webElements.mcc_trans_xpath)
        self.crawl_mcc_trans = mcc_trans_element.text.strip().replace('\n', ' : ')


        phone_element = self.driver.find_element(By.XPATH, webElements.phone_track_xpath)
        self.crawl_phone = phone_element.text.strip().replace('\n', ' : ')

        email_element = self.driver.find_element(By.XPATH, webElements.email_track_xpath)
        self.crawl_email = email_element.text.strip().replace('\n', ' : ')


        element_xpath = webElements.scroll_element
        element = self.driver.find_element(By.XPATH, element_xpath)

        scroll_script = """
        arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
        """
        self.driver.execute_script(scroll_script, element)

        
        time.sleep(2)

        scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(scroll_script)

        web_category = self.driver.find_element(By.XPATH,webElements.web_category_xpath)
        self.web_category_crawl = web_category.text.strip().replace('\n', ' : ')
        time.sleep(3)

        """
        Contact info
        """
        contact_profiel = self.driver.find_element(By.XPATH, webElements.contact_profile_xpath)
        click_element(contact_profiel)

        contact_element = self.driver.find_element(By.XPATH,webElements.contact_url_xpath)
        self.contact_url_crawled = contact_element.text.strip().replace('\n', ' : ')
        print(getLine())
        
        phone_data_element = self.driver.find_element(By.XPATH,webElements.phone_data_xpath)
        self.phone_data_crawled = phone_data_element.text.strip().replace('\n', ' : ')

        email_data_element = self.driver.find_element(By.XPATH,webElements.email_data_xpath)
        self.email_data_crawl = email_data_element.text.strip().replace('\n', ' : ')
        time.sleep(2)

        """
        Banned info
        """
        banned_element = self.driver.find_element(By.XPATH, webElements.banned_xpath)
        click_element(banned_element)

        game_info_ = self.driver.find_element(By.XPATH,webElements.game_info_xpath)
        self.game_info_crawled = game_info_.text.strip().replace('\n', ' : ')
        print(getLine())
        
        prohibhited_info_ = self.driver.find_element(By.XPATH,webElements.prohibhited_info_xpath)
        self.prohibhited_info_crawled = prohibhited_info_.text.strip().replace('\n', ' : ')

        pharmeceutical_info = self.driver.find_element(By.XPATH,webElements.pharmeceutical_info_xpath)
        self.pharmeceutical_info_crawl = pharmeceutical_info.text.strip().replace('\n', ' : ')
        time.sleep(2)

        """
        Security Info
        """

        security_element = self.driver.find_element(By.XPATH, webElements.security_xpath)
        click_element(security_element)

        malware_xpath_ = self.driver.find_element(By.XPATH,webElements.malware_xpath)
        self.malware_xpath_crawled = malware_xpath_.text.strip().replace('\n', ' : ')
        print(getLine())
        
        spam_xpath_info_ = self.driver.find_element(By.XPATH,webElements.spam_xpath)
        self.spam_xpath_info_crawled = spam_xpath_info_.text.strip().replace('\n', ' : ')

        untrusted_xpath_ = self.driver.find_element(By.XPATH,webElements.untrusted_xpath)
        self.untrusted_xpath_crawl = untrusted_xpath_.text.strip().replace('\n', ' : ')


        time.sleep(2)
        print("Parent processing")

    
    def parent_data(self):

        run_odd = self.driver.find_element(By.XPATH, webElements.run_ODD_xpath)
        self.run_odd_txt = run_odd.text
        click_element(run_odd)
        time.sleep(2)

        history_odd = self.driver.find_element(By.XPATH, webElements.odd_history_xpath)
        self.history_odd_txt = history_odd.text
        click_element(history_odd)


        history_logs = self.driver.find_element(By.XPATH, webElements.history_logs_xpath)
        self.history_logs_txt = history_logs.text

        time.sleep(2)

        """
            Parent Data
        """

        parent_case = self.driver.find_element(By.XPATH, webElements.parent_case_xpath)
        parent_case_txt = parent_case.text

        parent_created = self.driver.find_element(By.XPATH, webElements.parent_created_xpath)
        parent_created_txt = parent_created.text

        parent_completed_per = self.driver.find_element(By.XPATH, webElements.parent_completed_per_xpath)
        parent_completed_txt = parent_completed_per.text

        parent_start_time = self.driver.find_element(By.XPATH, webElements.parent_start_time_xpath)
        parent_start_time_txt = parent_start_time.text

        click_element(parent_case)

        self.crawl_data()


        print("Parent processing")

        self.parentdata = [
            self.result_type_txt,
            parent_start_time_txt,
            self.end_date_txt,
            parent_case_txt,
            parent_created_txt,
            parent_completed_txt,
            self.trade_Nm,
            self.crawl_risk,
            self.crawl_status,
            self.parent_per_txt,            
            self.crawl_mcc_data,
            self.web_category_crawl,
            self.crawl_mcc_trans,
            self.crawl_phone,
            self.crawl_email,
            self.contact_url_crawled,
            self.phone_data_crawled,
            self.game_info_crawled,
            self.pharmeceutical_info_crawl,
            self.prohibhited_info_crawled,
            self.malware_xpath_crawled,
            self.spam_xpath_info_crawled,
            self.untrusted_xpath_crawl,
            self.run_odd_txt,
            self.history_odd_txt,


        ]

        print("parent",self.parentdata)


    def child_data(self):

        print("Child data processing")
        self.driver.refresh()
        time.sleep(2)

        history_odd = self.driver.find_element(By.XPATH, webElements.odd_history_xpath)
        self.history_odd_txt = history_odd.text
        click_element(history_odd)

        child1_case = self.driver.find_element(By.XPATH, webElements.child1_case_xpath)
        click_element(child1_case)
        time.sleep(3)


        for  i in range(100):
            child1_status = self.driver.find_element(By.XPATH, webElements.child1_crawl_status)
            child1_status_txt = child1_status.text
            print("child crawl",child1_status_txt)

            if child1_status_txt != "Completed":
                time.sleep(5)
                self.driver.refresh()
                
            else:
                self.crawl_data()
                self.driver.refresh()

                """
                    Child Data
                """
                history_odd = self.driver.find_element(By.XPATH, webElements.odd_history_xpath)
                history_odd_txt = history_odd.text
                click_element(history_odd)
                time.sleep(2)

                child1_case = self.driver.find_element(By.XPATH, webElements.child1_case_xpath)
                child1_case_txt = child1_case.text

                child1_created = self.driver.find_element(By.XPATH, webElements.child1_created_xpath)
                child1_created_txt = child1_created.text

                child1_start_time = self.driver.find_element(By.XPATH, webElements.child1_start_time_xpath)
                child1_start_time_txt = child1_start_time.text

                child1_completed_per = self.driver.find_element(By.XPATH, webElements.child1_completed_per_xpath)
                child1_completed_per_txt = child1_completed_per.text

                break

                
        self.childdata = [
        self.result_type_txt,
                    child1_start_time_txt,
            self.end_date_txt,
            child1_case_txt,
            child1_created_txt,
            child1_completed_per_txt,
            self.trade_Nm,
            self.crawl_risk,
            self.crawl_status,
            self.parent_per_txt,
            self.crawl_mcc_data,
            self.web_category_crawl,
            self.crawl_mcc_trans,
            self.crawl_phone,
            self.crawl_email,
            self.contact_url_crawled,
            self.phone_data_crawled,
            self.game_info_crawled,
            self.pharmeceutical_info_crawl,
            self.prohibhited_info_crawled,
            self.malware_xpath_crawled,
            self.spam_xpath_info_crawled,
            self.untrusted_xpath_crawl,
            self.run_odd_txt,
            self.history_odd_txt,
           

        ]

        print("child data",self.childdata)

            
    def print_excel(self):

        self.testcase = [
            "Crawling RESULT type",
            "Crawling START time",
            "Crawling END time",
            "Crawling CASE ID ",
            "Crawling CREATED BY",
            "Crawling COMPLETED Percentage",
            "TRADE Name",
            "MCC Risk",
            "Crawling STATUS",
            "Crawling COMPLETED Percentage",
            "MCC Data",
            "MCC Category",
            "MCC Transactionable",
            "Crawled PHONE Risk",
            "Crawled EMAIL Risk",
            "Crawled Contact URL",
            "Crawled PHONE NUM",
            "GAME Info",
            "PHARMECEUTICAL Info",
            "PROHIBITED Info",
            "MALWARE Info",
            "SPAM Info",
            "UNTRUSTED Downloads Info",
            "RUN ODD Txt",
            "HISTORY ODD Txt",
           

        ]



        results = []

        for case, parent, child in zip(self.testcase,self.parentdata, self.childdata):

            print(getLine())
            print(f'✔ Parent : {parent} : Child : {child}')

            if parent != child:
                result_status = "Failed"
            else:
                result_status = "Pass"

            print(getLine())

            results.append({
                'Test Scenario': 'Check Run ODD flow',
                'Test Case':f'✔ Validate {case}',
                'Actual Parent output': f'✔ Parent  :  {[ parent ]} ',
                'Actual Child output': f'✔ Child  :  {[ child ]}',
                'Expected output': f'✔ Parent and Child data should present',
                'Result': result_status
            })

        webform = pd.DataFrame(results)

        with pd.ExcelWriter(crawl_output,mode='a', if_sheet_exists='replace' ,  engine='openpyxl' ) as writer:
            webform.to_excel(writer,sheet_name='Web ODD Flow')


if (__name__) == "__main__":
    crawl = Web_ODD()
    crawl.browser()
    crawl.login()
    crawl.crawl()
    crawl.parent_data()
    crawl.child_data()
    crawl.print_excel()

