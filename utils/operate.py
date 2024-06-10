import os
import sys
from selenium.webdriver.support import expected_conditions as EC
import allure
import os
import sys
from allure_commons.types import AttachmentType

dir = os.getcwd()
sys.path.append(dir)

from utils.launch import Initiate


def click_element(element):
    Initiate.wait.until(EC.element_to_be_clickable(element))
    element.click()
    
def sendkeys_element(element,action):
    Initiate.wait.until(EC.element_to_be_clickable(element))
    element.send_keys(action)

def get_screenshot(screen_name):

    allure.attach(Initiate.driver.get_screenshot_as_png(),name =screen_name,attachment_type=AttachmentType.PNG)


def get_text(element):
     element.strip().replace('\n', ' : ')
     