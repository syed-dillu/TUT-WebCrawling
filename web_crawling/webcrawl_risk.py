import requests
import os
import sys
import time

count = 1
dir = os.getcwd()
os.chdir(dir)
sys.path.append(dir)

from utils.helper import *

url = "https://bni-puneeast.in/"
class Web_Crawling():
    global percentage
    global case_id
    global risk_score




    def initiate_api(self):
        
        

        print(getLine())
        print("Website URL",url)

        crawl_data = {
        "website":url,
        "level" : "basic",
        "merchant" : {
        "trade_name" : "Squidee"
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

        self.status_check(self.case_id)

                
    def status_check(self,case_id):
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

        self.result_check(self.case_id)


    def result_check(self,case_id):

        result = f'{web_result_url}{self.case_id}'

        print(getLine())
        print("Web Result Api :",result)
        print("Percentage and Score Processing...")

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


                        while self.risk_score == 0:
                                time.sleep(6)
                                self.result_check(self.case_id)

                else:
                        print(f'Status :', status)
                        print(getLine())
                        print(f'Message :', message)
                        
        except ValueError as e:
                print(e)
       

   
if(__name__) == ("__main__"):

        crawl = Web_Crawling()

        crawl.initiate_api()
        percent = crawl.percentage
        score = crawl.risk_score
        caseID = crawl.case_id

        print("crawl percent:", percent)
        print("crawl risk score:", score)
        print("crawl case ID:", caseID)

        if(score != 0 ):
                print(f'the risk score is : {score}')


# while percent <= 0 or percent <= 50 or percent <= 85:
#     print("crawl percentage:", percent)
#     time.sleep(5)
#     crawl.result_check(caseID)
#     if score > 1:
#         print("crawl risk score:", score)
#         break


      












        


      

# #crawl.result_check("thHH182XyX5oyrR8Nw2sx4")

