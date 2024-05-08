import os 
import pandas as pd
import numpy as np
from openpyxl import workbook
from openpyxl.styles import PatternFill
import sys

dir = os.getcwd()


website_url = f"{dir}/testinputs/web_website_url.xlsx"

admin_edit_data = f"{dir}/testinputs/admin_crawl_edit.xlsx"

crawl_input_file =f'{dir}/testinputs/crawl_test_data.xlsx'

crawl_output = 'testoutput/webform.xlsx'

print(website_url)

data = pd.read_excel(website_url)
edit_crawl = pd.read_excel(crawl_output)
crawl_data = pd.read_excel(crawl_input_file,'Crawl Input',header=10).fillna('')

def get_excel_url():
    return data["WebsiteURL"]

def get_excel_trade():
    return data["Tradename"]

def get_mcc_bussiness():
    return edit_crawl["MCC Code"][0]

def get_web_site_cat():
    return edit_crawl["Website Category"][0]

def get_mcc_risk():
    return edit_crawl["MCC Risk"][0]

def get_crawl_company():
    return edit_crawl["Company Legal Name"][0]

def get_crawl_email():
    return edit_crawl["Email"][0]

def get_crawl_phone():
    return edit_crawl["Phone Number"][0]

def get_Percentage():
    return edit_crawl["Percentage"][0]

def get_crawl_Status():
    return edit_crawl["Status"][0]

def get_Addresss():
    return edit_crawl["Address"][0]

def get_login_info():
    return edit_crawl["Login info"][0]

def get_contact_url():
    return edit_crawl["Contact url"][0]

def get_transa_highly():
    return edit_crawl["Highly Transactable MCC"][0]

def get_crawl_input():
    crawl_input_data = crawl_data.to_dict(orient='records')
    return crawl_input_data
# print(get_crawl_input())


# results = []

# def output():

#     for data in get_crawl_input():
#         results.append((data['Website URL'],data['Trade Name']))
#     return results

# print(output())

# output_result = pd.DataFrame(output(),columns=['WebsiteURL', 'Tradename'])


# with pd.ExcelWriter('testoutput/webform.xlsx',mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
#     output_result.to_excel(writer,sheet_name='Results', index=False)
