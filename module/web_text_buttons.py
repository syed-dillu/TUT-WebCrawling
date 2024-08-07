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

from utils.launch import Initiate, environ
from elements import webElements
from excel_data.crawl_data import *
from excel_data.check_excel import write_excel

from helper import *



class Web_UI_Elements(Initiate):

    results = []

    def validation(self,element,text):

        response = []
        buttons = []

        buttons.append(text)
        print(buttons)

        if not text:
            response.append(f"[ ]")

        try:

            self.wait.until(EC.element_to_be_clickable(element))

            element.click()

            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(),name = f"Screenshot - {text}",attachment_type=AttachmentType.PNG)

            response.append(f"[ {text} ]  -  Button responding")

        except Exception as e:

            response.append(f"[ {text} ]  -  Button not responding")
        


        for i, j in zip(response, buttons):

            getLine()
            print(f'✔ [{j}, Buttons : {i}')



            if "Button not responding" in i or "[ ]" in i :
                result_status = "Failed"
            else:
                result_status = "Pass"

            if ("test" in j):
                continue
   
            self.results.append({
                "Test Case ID" :f'TC_001',
                'Test Scenario': f' ✔ Verify :\n[ {j} ] button',
                'Preconditions':f'User is logged in and on the Web Crawling page',
                'Test Steps':f'1. Click on the Web Crawling button\n2. Check : [ {j} ] \nbutton responding or not ',
                'Actual Output': f' ✔  {i}  ',
                'Expected Output':f' ✔ [ {j} ]  \nbutton should respond ',
                'Result': result_status,
                'Test Environment':environ,
                'Priority':'Medium',

            })

            write_excel(self.results,'Web Elements')

    def crawl(self):



        self.driver.implicitly_wait(50)

        time.sleep(2)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

        web_side_element = self.driver.find_element(By.XPATH, webElements.web_history_xpath)
        web_side = web_side_element.text

        web_title = self.driver.find_element(By.XPATH, webElements.web_title_xpath)
        web_title_text = web_title.text
        self.validation(web_title,web_title_text)


        filter_element = self.driver.find_element(By.XPATH, webElements.filter_btn_xpath)
        filter_text = filter_element.text

        self.validation(filter_element,filter_text)

        web_filter_close = self.driver.find_element(By.XPATH, webElements.web_filter_close_icon)
        filter_close_icon = "Filter close icon"
        self.validation(web_filter_close,filter_close_icon)

        time.sleep(1)

        add_element = self.driver.find_element(By.XPATH,webElements.add_btn_xpath)
        add_btn = add_element.text
        self.validation(add_element,add_btn)

        time.sleep(1)

        web_form_close = self.driver.find_element(By.XPATH, webElements.web_form_close)
        add_close_icon = "Add close icom"
        self.validation(web_form_close,add_close_icon)

        time.sleep(2)

        file_upload_element = self.driver.find_element(By.XPATH,webElements.file_upload_xpath)
        file_text = file_upload_element.text
        self.validation(file_upload_element,file_text)
        time.sleep(1)

        download_sample_element = self.driver.find_element(By.XPATH,webElements.down_load_xpath)
        downsample_text = download_sample_element.text
        self.validation(download_sample_element,downsample_text)

        time.sleep(1)

        file_upload_btn= self.driver.find_element(By.ID,webElements.file_upload_btn_xpath)
        time.sleep(1)
        file_upload_btn.send_keys(crawl_file_upload[0])
        time.sleep(1)
        self.driver.back()

        time.sleep(1)

        download_icon = self.driver.find_element(By.XPATH, webElements.download_icon_display)
        download_check = "Download icon"
        self.validation(download_icon,download_check)

        more_option = self.driver.find_element(By.XPATH, webElements.more_option_btn)
        more_text = more_option.text
        self.validation(more_option,more_text)

        time.sleep(3)

        more_appr = self.driver.find_element(By.XPATH, webElements.more_appr_xpath)
        more_approve_text = more_appr.text

        more_rejt = self.driver.find_element(By.XPATH,webElements.more_rejt_xpath)
        more_reject = more_rejt.text

        more_rejt_block = self.driver.find_element(By.XPATH, webElements.more_rejt_block_xpath)
        more_reject_block_text = more_rejt_block.text

        time.sleep(1)

        self.driver.refresh()

        menu_icon = self.driver.find_element(By.XPATH, webElements.menu_icon_xpath)
        menu_icon_text = "Action menu icon"
        self.validation(menu_icon,menu_icon_text)

        time.sleep(1)

        view_details = self.driver.find_element(By.XPATH, webElements.view_details_xpath)
        view_details_text = view_details.text
        self.validation(view_details,view_details_text)

        time.sleep(2)

        back_btn_element = self.driver.find_element(By.XPATH, webElements.back_btn)
        back_btn_element_text = f'View {back_btn_element.text} button'
        self.validation(back_btn_element,back_btn_element_text)

        time.sleep(2)

        menu_icon = self.driver.find_element(By.XPATH, webElements.menu_icon_xpath)
        menu_icon_text = "Action menu icon"
        self.validation(menu_icon,menu_icon_text)

        time.sleep(2)

        results_ele = self.driver.find_element(By.XPATH, webElements.results_xpath)
        results_ele_text = results_ele.text
        self.validation(results_ele,results_ele_text)

        time.sleep(2)

        json_btn = self.driver.find_element(By.XPATH, webElements.json_btn_xpath)
        json_btn_ele_text = json_btn.text
        self.validation(json_btn,json_btn_ele_text)
        time.sleep(1)

        json_copy_ele = self.driver.find_element(By.XPATH, webElements.json_copy_xpath)
        json_copy_ele_text = "Copy json"
        self.validation(json_copy_ele,json_copy_ele_text)
        time.sleep(1)

        json_download_ele = self.driver.find_element(By.XPATH, webElements.json_download_xpath)
        json_download_ele_text = "Json Download"
        self.validation(json_download_ele,json_download_ele_text)
        time.sleep(1)

        self.driver.refresh()

        time.sleep(1)

        back_btn_element = self.driver.find_element(By.XPATH, webElements.back_btn)
        back_btn_element_text = f'Results {back_btn_element.text} button'
        self.validation(back_btn_element,back_btn_element_text)


        time.sleep(1)

        crawl_place_next = self.driver.find_element(By.XPATH, webElements.crawl_place_next_xpath)
        crawl_place_next_text = crawl_place_next.text
        self.validation(crawl_place_next,crawl_place_next_text)

        time.sleep(2)

        crawl_place_prev = self.driver.find_element(By.XPATH, webElements.crawl_place_prev_xpath)
        crawl_place_prev_text = crawl_place_prev.text
        self.validation(crawl_place_prev,crawl_place_prev_text)

        time.sleep(1)

        crawl_place_loader = self.driver.find_element(By.XPATH, webElements.crawl_place_loader_xpath)
        crawl_place_loader_text = crawl_place_loader.text
        self.validation(crawl_place_loader,crawl_place_loader_text)

        time.sleep(1)

        crawl_place_100 = self.driver.find_element(By.XPATH, webElements.crawl_place_100_xpath)
        crawl_place_100_text = crawl_place_100.text
        self.validation(crawl_place_100,crawl_place_100_text)

        Web_UI_Elements.logout(self)


        web_text_buttons_list = {

            "Web side menu" : web_side,
            "Web page title" : web_title_text,
            "Filter text" : filter_text,
            "Filter close icon" : filter_close_icon,
            "Add button" : add_btn,
            "Add crawl page close icon" : add_close_icon,
            "File upload" : file_text,
            "Download icon" :download_check,
            "More option button": more_text ,
            "Approve button" : more_approve_text,
            "Reject button" : more_reject,
            "Reject & Block button" :more_reject_block_text,
            "Action menu icon" : menu_icon_text,
            "View details button" :view_details_text ,
            "View details back button":back_btn_element_text,
            "Results button":results_ele_text,
            "View json button":json_btn_ele_text,
            "Copy json button":json_copy_ele_text,
            "Download json button":json_download_ele_text,
            "Results page back button":back_btn_element_text,
            "Progress bar Next button":crawl_place_next_text,
            "Progress bar Prev button":crawl_place_prev_text,
            "Progress bar dropdown button":crawl_place_loader_text,
            "Progress bar select 100 button":crawl_place_100_text,

        }

        for i,(key , value) in enumerate(web_text_buttons_list.items(),start=1):
            print(f' {key} : {value}')
            if not value:
                results_status = "Failed"
            else:
                results_status = "Pass"

            self.results.append({
                "Test Case ID" :f'TC_00{i}',
                'Test Scenario': f' ✔ Verify :\n[ {key} ] ',
                'Preconditions':f'User is logged in and on the Web Crawling page',
                'Test Steps':f'1. Click on the Web Crawling button\n2. Check :\n[ {key} ] displayed or not ',
                'Actual Output': f' ✔ {key}  :\n[ {value} ] ',
                'Expected Output': f' ✔ [ {key} ]\nshould display',
                'Test Environment':environ,
                'Priority':'Medium',
                'Result': results_status

            })

        #write_excel(self.results,'Web Elements')


if (__name__) == "__main__":
    crawl = Web_UI_Elements()
    crawl.browser()
    crawl.login()
    crawl.crawl()




