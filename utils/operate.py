import os
import sys
from selenium.webdriver.support import expected_conditions as EC


dir = os.getcwd()
sys.path.append(dir)

from utils.launch import Initiate


def click_element(element):
    Initiate.wait.until(EC.element_to_be_clickable(element))
    element.click()
    
def sendkeys_element(element,action):
    Initiate.wait.until(EC.element_to_be_clickable(element))
    element.send_keys(action)