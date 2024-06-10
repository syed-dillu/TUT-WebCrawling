import streamlit as st
import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from allure_commons.types import AttachmentType
import allure
import pandas as pd
dir = os.getcwd()
sys.path.append(dir)

from elements.loginElements import *
from messages.loginMessage import *

load_dotenv()

url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
url_web = os.getenv("URL")
email_web = os.getenv("EMAIL_WEB")
password_web = os.getenv("PASSWORD_WEB")


class Web_Streamlit():

    results= []

    def crawl_data(self):
        from module.web_odd_flow import Web_ODD
        Web_ODD.crawl_data(self)


    

    def validation(self,element,text):

        from module.web_text_buttons import Web_UI_Elements
        Web_UI_Elements.validation(self,element,text)


    def login(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(url)        
        email_input = self.driver.find_element(By.NAME, login_email)
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.NAME, login_pass)
        password_input.send_keys(password)
        print(password)

        terms_checkbox_ = self.driver.find_element(By.ID, login_check_box)
        terms_checkbox_.click()

        login_btn = self.driver.find_element(By.XPATH, login_button)
        login_btn.click()

        # multiple_button = self.driver.find_element(By.XPATH, "(//button[@class='ant-btn css-42nv3w ant-btn-primary btn btn-primary ml-2'])[1]")
        # multiple_button.click()
    

    def loginweb(self):



        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(url_web)        
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys(email_web)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password_web)

        terms_checkbox = self.driver.find_element(By.ID, "terms-section")
        terms_checkbox.click()

        login_button = self.driver.find_element(By.XPATH, "//span[text()='LOGIN']")
        login_button.click()

        # multiple_button = self.driver.find_element(By.XPATH, "(//button[@class='ant-btn css-42nv3w ant-btn-primary btn btn-primary ml-2'])[1]")
        # multiple_button.click()
  
    
    def web_ui_data(self):
        from module.web_text_buttons import Web_UI_Elements
        self.validation("hello","test"),

        self.login()
        return ({
            Web_UI_Elements.crawl(self),
        })

    def web_add_site(self):
        from module.web_add_site import Web_Add_Site
        self.login()
        return Web_Add_Site.crawl_input(self)
    
    def web_list_page(self):
        from module.web_list_page import Web_List_Page
        self.login()
        return Web_List_Page.crawl(self)
    
    def web_crawl_results(self):
        from module.web_crawl_results import Web_Crawl_Results
        self.login()

        return {
            Web_Crawl_Results.crawl(self),
            Web_Crawl_Results.crawl_result(self)
        }
    
    def web_run_odd(self):
        from module.web_odd_flow import Web_ODD

        self.login()

        return {
            Web_ODD.crawl(self),
            Web_ODD.parent_data(self),
            Web_ODD.child_data(self),
            Web_ODD.print_excel(self)
        }


    def web_validate_list(self):
        from module.web_history_report import Web_History_Page

        self.login()

        return{
            Web_History_Page.crawl(self),
            Web_History_Page.history_report(self),
            Web_History_Page.validate_report(self)
        }
    
    def web_multiple_site(self):
        from module.web_multiple_site import WebCrawl
        self.login()
        return ({
            WebCrawl.crawl(self),
        })

st.title("Web crawling flow with test cases")

add_site = st.button("Add Site")
listing_page = st.button("Web List Page")
web_crawl_elements  = st.button("Web Crawling Elements")
# crawl_results = st.button("Crawl Results")
run_odd = st.button("Run ODD")
validate_list_page = st.button("Web Validate List")
add_mutliple = st.button("Add Multiple Site")


try:

    if web_crawl_elements:
        Web_Streamlit().web_ui_data()

    if add_site:
        Web_Streamlit().web_add_site()

    if listing_page:
        Web_Streamlit().web_list_page()

    if run_odd:
        Web_Streamlit().web_run_odd()

    if validate_list_page:
        Web_Streamlit().web_validate_list()

    if add_mutliple:
        Web_Streamlit().web_multiple_site()


except Exception as e:
    print(e)


