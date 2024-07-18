import os 
import pandas as pd
import numpy as np
from openpyxl import workbook
from openpyxl.styles import PatternFill
import sys
import random

dir = os.getcwd()


website_url = f"{dir}/testinputs/web_website_url.xlsx"
admin_edit_data = f"{dir}/testinputs/admin_crawl_edit.xlsx"
crawl_input_file =f'{dir}/testinputs/crawl_test_data.xlsx'
crawl_output = f'{dir}/testoutput/web_test_case.xlsx'
crawl_10 = f'{dir}/testinputs/crawl_10.xlsx'
crawl_empty_file = f'{dir}/testinputs/crawl_empty_file.xlsx'
Crawling_more_25 = f'{dir}/testinputs/Crawling_more_25.xlsx'
Crawl_type = f'{dir}/testinputs/Crawl_type.xlsx'
Crawl_website = f'{dir}/testinputs/Crawl_website.xlsx'
Crawl_trade = f'{dir}/testinputs/Crawl_trade.xlsx'


crawl_file_upload = [
    crawl_empty_file,
    Crawling_more_25,
    crawl_10,
    Crawl_website,
    Crawl_trade,
    Crawl_type,

]


crwl = pd.read_excel(crawl_output)
print(crwl)

print(website_url)

data = pd.read_excel(website_url)
crawl_data = pd.read_excel(crawl_input_file,'Crawl Input',header=10).fillna('')

def get_excel_url():
    return data["WebsiteURL"]

def get_excel_trade():
    return data["Tradename"]

def get_excel_address():
    return data["Address"]


def get_crawl_input():
    crawl_input_data = crawl_data.to_dict(orient='records')
    return crawl_input_data
print(get_crawl_input())
print(pd.DataFrame(get_crawl_input()))

# results = []

# def output():

#     for data in get_crawl_input():
#         results.append((data['Website URL'],data['Trade Name']))
#     return results

# print(output())

# output_result = pd.DataFrame(output(),columns=['WebsiteURL', 'Tradename'])


# with pd.ExcelWriter('testoutput/webform.xlsx',mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
#     output_result.to_excel(writer,sheet_name='Results', index=False)
