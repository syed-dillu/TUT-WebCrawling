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
from excel_data.crawl_data import get_crawl_input,crawl_output, get_excel_url, get_excel_trade
from utils.operate import click_element, sendkeys_element, get_screenshot

crawl = "Basic Crawling"



class WebCrawl(Initiate):

    

    def crawl(self):
        countweb = 3

        self.count_loop = 0

        self.web_url = get_excel_url()
        self.trade_name = get_excel_trade()
        
        self.driver.implicitly_wait(50)

        time.sleep(1)

        web_crawl = self.driver.find_element(By.XPATH, webElements.web_crawl_xpath)
        self.driver.execute_script("arguments[0].click();", web_crawl)

        for url,trade in zip(self.web_url,self.trade_name):
            print("Case : ",self.count_loop)
            #self.website = single_url

            add_site = self.driver.find_element(By.XPATH, webElements.add_site_xpath)
            click_element(add_site)

            print("-------",url)
            website_url = self.driver.find_element(By.XPATH, webElements.website_url_xpath)
            sendkeys_element(website_url,url)

            time.sleep(1)

            trade_elt = self.driver.find_element(By.XPATH, webElements.trade_xpath)
            sendkeys_element(trade_elt,trade)


            crawling_drop = self.driver.find_element(By.XPATH, webElements.crawling_drop_xpath)
            click_element(crawling_drop)


            crawling_select = self.driver.find_element(By.XPATH, webElements.crawling_select_xpath)
            click_element(crawling_select)


            crawling_btn = self.driver.find_element(By.XPATH, webElements.crawling_btn_xpath)
            click_element(crawling_btn)


            time.sleep(1)

            self.count_loop += 1

            if(self.count_loop == countweb):
                 break
            
        WebCrawl.logout(self)


        return {
        "status" : "Success",
        "Crawled Website" : url,
        "Trade Name" : trade,
        }
        

if (__name__) == "__main__":
    crawl = WebCrawl()
    crawl.browser()
    crawl.login()
    crawl.crawl()

