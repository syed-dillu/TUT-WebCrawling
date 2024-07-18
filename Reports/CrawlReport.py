import allure
import os
import sys


dir = os.getcwd()
sys.path.append(dir)
from module.web_add_site import Web_Add_Site
from module.web_list_page import Web_List_Page
from module.web_file_upload import File_Upload
from module.web_text_buttons import Web_UI_Elements
from module.web_odd_flow import Web_ODD
from module.web_history_report import Web_History_Page

@allure.severity(allure.severity_level.NORMAL)
class Test_Crawl():



    @allure.title("Add Website")
    @allure.description('Check add site')
    def test_addsite(self):
        crawl = Web_Add_Site()
        crawl.browser()
        crawl.login()
        crawl.crawl_input()

    @allure.title("Crawling Elements")
    def test_crawlelements(self):
        crawl = Web_UI_Elements()
        crawl.logout_login()
        crawl.crawl() 

    @allure.title("Listing Page")
    @allure.description('Check Listing page')
    def test_listpage(self):
        crawl = Web_List_Page()
        crawl.logout_login()
        crawl.crawl()
    
 
    @allure.title("Crawl ODD Flow")
    def test_oddflow(self):
        crawl = Web_ODD()
        crawl.logout_login()
        crawl.crawl()
        crawl.parent_data()
        crawl.child_data()
        crawl.print_excel()

    @allure.title("Validate Listing Page")
    def test_validatelist(self):
        crawl = Web_History_Page()
        crawl.logout_login()
        crawl.crawl()  

    @allure.title("File Upload")
    def test_fileupload(self):
        crawl = File_Upload()
        crawl.logout_login()
        crawl.crawl()




