import os
import pandas as pd
import sys
import numpy as np
import string
import random


dir = os.getcwd()

website_url = f"{dir}/utils/website_url.xlsx"

data = pd.read_excel(website_url)

def get_web_url():
    return data["WebsiteURL"]

def get_trade_name():
    return data["Tradename"]
