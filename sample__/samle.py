# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Set up Chrome options
# chrome_options = Options()
# #chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("user-agent=HeadlessChrome")  # Set custom user agent

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get("https://demo.fingerprint.com/playground")
# print(driver.title)
# time.sleep(5)

# # Retrieve and print console logs
# logs = driver.get_log("browser")
# for log in logs:
#     print(log)

# headless_mode = "HeadlessChrome" in driver.execute_script("return navigator.userAgent")
# print("Is running in headless mode:", headless_mode)

# input("Enter a name : ")
# driver.quit()


# response = ["response1", "response2", "response3"]
# buttons = ["button1", "button2", "button3"]

# for x, (i, j) in enumerate(zip(response, buttons), start=1):
#     print(f"Index: {x}, Response: {i}, Button: {j}")


import os 

import sys

dir = os.getcwd()
current_file_path = os.path.abspath(__file__)
print(current_file_path)

current_dir_path = os.path.dirname(current_file_path)
print(current_dir_path)

parent_directory = os.path.dirname(current_dir_path)
print(parent_directory)
