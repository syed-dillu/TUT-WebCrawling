import requests
import os
import sys
import time

dir = os.getcwd()
os.chdir(dir)
sys.path.append(dir)

from utils.helper import *
from utils.website_data import *


total_count = 1
trade_name =  gettrade()
class Web_external():
    urls = get_web_url()
    trade_names = get_trade_name()
    
    count = 0


    def initiate_api(self):
        
        
        for url,trade in zip(self.urls,self.trade_names):

                print(getLine())
                print("Website URL",url)

                crawl_data = {
                "website":url,
                "level" : "basic",
                "merchant" : {
                        "trade_name" : trade,
                }
                }
                print("Web Initiate Api :",web_initiate_url)
                print(getLine())


                response = requests.post(f'{web_initiate_url}',headers=headers, auth=web_auth,json=crawl_data)
                json_data = response.json()
                message = json_data['message']
                if message == 'Invalid authentication credentials' or 'You are not subscribe this product. Please contact admin.' or 'You cannot consume this service':
                        print(json_data)      

                status = json_data['success']
                code = json_data['code']
                data = json_data['data']
                case_id = data['caseId']

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

                                print(f'Case ID :', case_id)
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

                self.status_check(case_id)

                self.count += 1
                if(self.count == total_count):
                       break
                print(f'Webcrawl count {self.count}')


        
        return json_data

                
    def status_check(self,case_id):
        status = f'{web_status_url}{case_id}'
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

                self.result_check(case_id)

        return json_data

    def result_check(self,case_id):

        result = f'{web_result_url}{case_id}'

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
                
        return "hello world"    

if(__name__) == ("__main__"):
        crawl = Web_external()
        crawl.initiate_api()





      












        


      

# #crawl.result_check("thHH182XyX5oyrR8Nw2sx4")

