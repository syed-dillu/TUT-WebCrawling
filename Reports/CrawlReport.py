import allure
import os
import sys


dir = os.getcwd()
sys.path.append(dir)
from module.web_add_site import Web_Add_Site
from module.web_list_page import Web_List_Page
from module.web_crawl_results import Web_Crawl_Results
from module.web_text_buttons import Web_UI_Elements


class Test_Crawl():

    @allure.title("Add Website")
    def test_addsite(self):
        crawl = Web_Add_Site()
        crawl.browser()
        crawl.login()
        crawl.crawl_input()

    @allure.title("Listing Page")
    def test_listpage(self):
        crawl = Web_List_Page()
        crawl.browser()
        crawl.login()
        crawl.crawl()
        
    @allure.title("Crawl Result")
    def test_resultpage(self):
        crawl = Web_Crawl_Results()
        crawl.browser()
        crawl.login()
        crawl.crawl()
        crawl.crawl_result()

    @allure.title("Crawling Elements")
    def test_crawlelements(self):
        crawl = Web_UI_Elements()
        crawl.browser()
        crawl.login()
        crawl.crawl()        



