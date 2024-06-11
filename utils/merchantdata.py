import os
import pandas as pd
import sys
import numpy as np
import string
import random

from tabulate import tabulate


dir = os.getcwd()

customer_data = f"{dir}/utils/MER_FILE.xlsx"

data = pd.read_excel(customer_data)
data_row = data['count'][1]
#print((data_row))


def get_tabular():

    datas = data.iloc[data_row]
    row_df = pd.DataFrame(datas).transpose()
    return tabulate(row_df, headers='keys', tablefmt='pretty')

#print(get_tabular())

def get_Null_data():
    null_columns = data.columns[data.isnull().any()]
    return null_columns
#print(get_Null_data())

def get_merchant_ref_id():
    alpha_numeric = string.ascii_uppercase + string.digits
    ref_id = ''.join(random.choices((alpha_numeric), k=14))
    return ref_id

def get_reseller_trade_name():
    return data['reseller_trade_name'][data_row]

def get_email():
    return data['email'][data_row]

def get_phone():
    return data['phone'][data_row]

def get_name():
    return data['name'][data_row]

def get_company_name():
    return data['company_name'][data_row]

def get_trade_name():
    return data['trade_name'][data_row]

def get_merchant_type():
    return data['merchant_type'][data_row]

def get_entity_type():
    return data['entity_type'][data_row]

def get_mcc_code():
    return data['mcc_code'][data_row]

def get_domain_creation_date():
    return data['domain_creation_date'][data_row]

def get_registration_number():
    return data['registration_number'][data_row]

def get_incorporation_date():
    return data['incorporation_date'][data_row]

def get_gst():
    return data['gst'][data_row]

def get_website_url():
    return data['website_url'][data_row]

def get_address():
    return data['address'][data_row]

def get_city():
    return data['city'][data_row]

def get_postal_code():
    return data['postal_code'][data_row]

def get_state():
    return data['state'][data_row]

def get_country():
    return data['country'][data_row]

def get_pan():
    return data['pan'][data_row]

def get_signatory_1():
    return data['signatory_1'][data_row]

def get_signatory_2():
    return data['signatory_2'][data_row]

def get_signatory_3():
    return data['signatory_3'][data_row]

def get_bank_name():
    return data['bank_name'][data_row]

def get_account_number():
    return data['account_number'][data_row]

def get_account_holder_name():
    return data['account_holder_name'][data_row]

def get_ifsc_code():
    return data['ifsc_code'][data_row]

def get_aadhaar():
    return data['aadhaar'][data_row]

def get_kyc_checks():
    return data['kyc_checks'][data_row]

def get_entity_code():
    code = 'vgyJiPbmQ'
    return code

def get_entity_name():
    name = 'Partnership / LLP'
    return name

def get_client_code():
    code = "O96ty9TSb"
    return code

def get_client_name():
    name = "Airlines"
    return name


def getLine():

    line = "                                                                        "

    #line = "•·······························•·······························•"
    return line

def getDotLine():


    dotline = "•·······························•·······························•"
    return dotline



# print(f'merchant_ref_id             ---- {get_merchant_ref_id()}')
# print(f'reseller_trade_name            ---- {get_reseller_trade_name()}')
# print(f'email                ---- {get_email()}')
# print(f'phone                 ---- {get_phone()}')
# print(f'company_name           ---- {get_company_name()}')
# print(f'email                  ---- {get_email()}')
# print(f'phone                  ---- {get_phone()}')
# print(f'trade_name            ---- {get_trade_name()}')
# print(f'merchant_type            ---- {get_merchant_type()}')
# print(f'entity_type          ---- {get_entity_type()}')
# print(f'mcc_code         ---- {get_mcc_code()}')
# print(f'domain_creation_date      ---- {get_domain_creation_date()}')
# print(f'registration_number            ---- {get_registration_number()}')
# print(f'incorporation_date         ---- {get_incorporation_date()}')
# print(f'gst            ---- {get_gst()}')
# print(f'website_url     ---- {get_website_url()}')
# print(f'address                 ---- {get_address()}')
# print(f'city               ---- {get_city()}')
# print(f'postal_code                   ---- {get_postal_code()}')
# print(f'state        ---- {get_state()}')
# print(f'country           ---- {get_country()}')
# print(f'pan        ---- {get_pan()}')
# print(f'signatory_1    ---- {get_signatory_1()}')
# print(f'signatory_2                 ---- {get_signatory_2()}')
# print(f'signatory_3               ---- {get_signatory_3()}')
# print(f'bank_name                   ---- {get_bank_name()}')
# print(f'account_number        ---- {get_account_number()}')
# print(f'account_holder_name           ---- {get_account_holder_name()}')
# print(f'ifsc_code        ---- {get_ifsc_code()}')
# print(f'aadhaar    ---- {get_aadhaar()}')
# print(f'Kyc_checks    ---- {get_kyc_checks()}')

# print(f'account_holder_name           ---- {get_account_holder_name()}')
# print(f'ifsc_code        ---- {get_ifsc_code()}')
# print(f'aadhaar    ---- {get_aadhaar()}')

