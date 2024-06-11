import requests
import os
import sys
import time

count = 9
dir = os.getcwd()
os.chdir(dir)
sys.path.append(dir)

from utils.helper import *
from excel_data.crawl_data import *

class Web_external():
    url_list = random.choices(get_excel_url())
    url = ''.join(url_list)

    print("URL ",url)

    case_id = ''

    def initiate_api(self):
        
        print(getLine())
        print("Website URL",self.url)

        crawl_data = {
        "website":self.url,
        "level" : "basic",
        "merchant" : {
        "trade_name" : "tabs"
        }
        }
        print("Web Initiate Api :",web_initiate_url)
        print(getLine())


        response = requests.post(f'{web_initiate_url}',headers=headers, auth=web_auth,json=crawl_data)
        json_data = response.json()
        message = json_data['message']
        print(json_data)      

        if message != "Queue added":
            print(json_data)      

        status = json_data['success']
        code = json_data['code']
        data = json_data['data']
        self.case_id = data['caseId']

        try:
                if status == True:
                        website = data['websiteName']

                        print(getLine())

                        print(f'Website :', website)
                        print(getLine())

                        print(f'Status :', status)
                        print(getLine())

                        print(f'Message :', message)
                        print(getLine())

                        print(f'Code :', code)
                        print(getLine())

                        print(f'Case ID :', self.case_id)
                        print(getLine())

                        for key , value in data.items():
                            print(f'Crawling {key} : {value}' )
                            print(getLine())
                        print(getDotLine())

                else:
                        print(f'Status :', status)
                        print(f'Message :', message)

                        
        except ValueError as e:
                print(e)

        if message != "Queue added":
            return json_data   
        
        else:        
                return ({
                
                        f'Website ': website,
                        f'Case ID ' : self.case_id,
                        f'Status ': status,
                        f'Message ': message,
                        f'Code ' : code,
                })  

                
    def status_check(self):
        status = f'{web_status_url}{self.case_id}'
        print(getLine())

        print("Web Status Api :",status)

        print(getLine())

        response = requests.get(status,headers=headers, auth=web_auth)
        json_data = response.json()
        status = json_data['success']
        message = json_data['message']
        code = json_data['code']
        data = json_data['data']

        try:
                if status == True:

                        print(f'Status :', status)
                        print(getLine())

                        print(f'Message :', message)
                        print(getLine())

                        print(f'Code :', code)
                        print(getLine())


                        for key , value in data.items():
                            print(f'Crawling {key} : {value}' )
                                  
                            print(getLine())
                        print(getDotLine())

                else:
                        print(f'Status :', status)
                        print(f'Message :', message)

                        
        except ValueError as e:
                print(e)


        return ({
        
                f'Status ': status,
                f'Message ': message,
                f'Case ID ' : self.case_id,
                f'Code ' : code,
        }) 
        
    def result_check(self):

        result = f'{web_result_url}{self.case_id}'

        print(getLine())
        print("Web Result Api :",result)

        print(getLine())

        response = requests.get(result,headers=headers, auth=web_auth)
        json_data = response.json()
        status = json_data['success']
        message = json_data['message']
        code = json_data['code']
        data = json_data['data']
        website = data['website']
        client_data = data['client']
        self.percentage = data['percentage']

        business_name = data['merchant']
        data_status = data['status']
        self.risk_score = data['risk_score']

        try:
                if status == True:

                        print(f'Status :', status)
                        print(getLine())

                        print(f'Message :', message)
                        print(getLine())

                        print(f'Code :', code)
                        print(getLine())

                        print(f'Client :', client_data)
                        print(getLine())

                        print(f'website :', website)
                        print(getLine())

                        print(f'business_name :', business_name)
                        print(getLine())

                        print(f'Crawling status :', data_status)
                        print(getLine())

                        print(f'Percentage :', self.percentage)
                        print(getLine())

                        print(f'Risk_score :', self.risk_score)
                        print(getLine())
                        print(getDotLine())
                else:
                        print(f'Status :', status)
                        print(getLine())
                        print(f'Message :', message)
                        
        except ValueError as e:
                print(e)

        return ({
              
                 f'Website ': website,
                 f'Status ': status,
                 f'Message ': message,
                 f'Code ' : code,
                f'Client ' : client_data,
                f'business_name ' : business_name,
                f'Crawling status ' : data_status,
                f'Percentage ' : self.percentage,
                f'Risk_score ' : self.risk_score

        }) 
    
if(__name__) == ("__main__"):
        crawl = Web_external()
        crawl.initiate_api()
        crawl.status_check()
        crawl.result_check()







      












        


      

# #crawl.result_check("thHH182XyX5oyrR8Nw2sx4")

