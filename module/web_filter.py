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


class Web_Filter(Initiate):

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

        # time.sleep(2)

        # allure.attach(self.driver.get_screenshot_as_png(), name=f'Screenshot : {"Crawled Data"}', attachment_type=AttachmentType.PNG)

        crawling_btn = self.driver.find_element(By.XPATH, webElements.crawling_btn_xpath)
        click_element(crawling_btn)

        case_id = self.driver.find_element(By.XPATH, webElements.link_xpath)
        self.case_ID = case_id.text
        print(self.case_ID)


        filter_element = self.driver.find_element(By.XPATH, webElements.filter_btn_xpath)
        click_element(filter_element)

        time.sleep(200)

        # filter_click = self.driver.find_element(By.XPATH, webElements.filter_click_xpath)
        # click_element(filter_click)

        # filcase_id = self.driver.find_element(By.XPATH, webElements.fil_case_id)
        # click_element(filcase_id)

        # fil_enter = self.driver.find_element(By.XPATH, webElements.fil_enter_xpath)
        # sendkeys_element(fil_enter,self.case_ID)

        # fil_status = self.driver.find_element(By.XPATH, webElements.fil_status_xpath)
        # click_element(fil_status)

        # fil_pendingstatus = self.driver.find_element(By.XPATH, webElements.fil_pending_status)
        # click_element(fil_pendingstatus)


if (__name__) == "__main__":
    crawl = Web_Filter()
    crawl.browser()
    crawl.login()
    crawl.crawl()








