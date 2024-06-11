import json
import requests
import os
import sys
import time
from locust import task , HttpUser, between

dir = os.getcwd()
sys.path.append(dir)

from utils.helper import *
from utils.website_data import *


trade_name =  gettrade()
class Web_external(HttpUser):
    urls = get_web_url()
    trade_names = get_trade_name()
    host = base_url
    wait_time = between(1, 3) 
    count = 0
    

    @task
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
                

                response = self.client.post("api/v1/web-crawling/website-crawl", data=json.dumps(crawl_data), auth=web_auth,headers=headers)

                #response = requests.post(f'{web_initiate_url}',headers=headers, auth=web_auth,json=crawl_data)
                json_data = response.json()
                print("345345",json_data)
                
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
                                self.count += 1
                                print(f"The Crawling Count : {self.count}")

                        else:
                                print(f'Status :', status)
                                print(f'Message :', message)

                                
                except ValueError as e:
                        print(e)

                self.status_check(case_id)



        
        return json_data

                
    def status_check(self,case_id):
        web_status_url = "api/v1/web-crawling/get-status?case_id="
        status = f'{web_status_url}{case_id}'
        print(getLine())

        print("Web Status Api :",status)

        print(getLine())

        response = self.client.get(status, auth=web_auth,headers=headers)
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
        web_result_url = "api/v1/web-crawling/get-crawl-results?case_id="

        result = f'{web_result_url}{case_id}'

        print(getLine())
        print("Web Result Api :",result)

        print(getLine())
        response = self.client.get(result, auth=web_auth,headers=headers)

        #response = requests.get(result,headers=headers, auth=web_auth)
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

# if(__name__) == ("__main__"):
#         crawl = Web_external()
#         crawl.initiate_api()





      












        


      

# #crawl.result_check("thHH182XyX5oyrR8Nw2sx4")

