
# Web

#web_crawl_xpath = "//body/div[@id='root']/div[1]/div[1]/div[8]/div[1]/ul[1]/li[3]/a[1]/span[1]"
web_crawl_xpath = "(//a)[13]"
add_site_xpath = "//span[normalize-space()='Add Site']"
website_url_xpath = "(//input[@id='msg'])[1]"
trade_xpath = "//input[@placeholder='Enter Trade Name']"
crawling_drop_xpath = "//div[@name='crawlingType']//div[@class='ant-select-selector']"
crawling_select_xpath = "//div[@class='ant-select-item-option-content']"
crawling_btn_xpath = "//span[normalize-space()='Submit']"
add_site_xpath = "//span[normalize-space()='Add Site']"
web_history_xpath = "(//span[normalize-space()='Websites History'])[1]"
filter_btn_xpath = "//span[normalize-space()='Filters']"
add_btn_xpath = "//span[normalize-space()='Add Site']"
file_upload_xpath = "//button[@class='ant-btn css-mzwlov ant-btn-default back__btn']"
download_icon_display = "(//button[@class='ant-btn css-mzwlov ant-btn-default trans-down m-l-10'])[1]"
more_option_btn = "//span[normalize-space()='More options']"
more_appr_xpath = "//a[normalize-space()='Approve']"
more_rejt_xpath = "//a[normalize-space()='Reject']"
more_rejt_block_xpath = "//a[normalize-space()='Reject And Block']"
web_title_xpath = "//h2[normalize-space()='websites history']"
web_filter_close_icon = "//img[@alt='close']"
web_form_close = "(//img[@class='close_icon mt-2'])[1]"
down_load_xpath = "//span[normalize-space()='Download Sample']"
file_upload_btn_xpath = "//span[contains(text(),'Click to Upload')]"
menu_icon_xpath = "//tbody/tr[2]/td[10]/span[1]/div[1]/div[1]"
view_details_xpath = "//a[contains(text(),'View Details')]"
back_btn = "//button[@type='button']"
results_xpath = "//a[normalize-space()='Results']"


file_xpath = "//span[contains(text(),'File Upload')]"
upload_xpath = "//input[@id='fileInput']"
ok_xpath = "//button[normalize-space()='Ok']"
risk_xpath = "//tbody/tr[2]/td[6]/span[1]"
percent_xpath = "//tbody/tr[2]/td[7]/span[1]"
scroll_element = "//p[contains(text(),'Content Risk')]"
link_xpath = "//tbody/tr[2]/td[2]"
list_weburl_xpath = "//tbody/tr[2]/td[3]/div[1]"
list_trade_xpath = "//tbody/tr[2]/td[4]/div[1]"
list_crawl_status_xpath = "//tbody/tr[2]/td[8]/span[1]"
list_risk_xpath = "//tbody/tr[2]/td[9]/div[1]/span[1]"


# crawl elements

trade_crawl_xpath =  "//div[h3[@class='m-0 f_17_web text-capitalize']]"
mcc_buss_xpath =  "//div[p[@class='f_15'][text()='Business Classification']]"
mcc_risk_xpath = "//div[p[@class='f_15'][text()='MCC Risk Classification']]"
mcc_trans_xpath = '//div[p[@class="f_15"][text()="Highly Transacting MCC\'s"]]'
phone_track_xpath = "//div[p[@class='f_15'][text()='Phone Found']]"
email_track_xpath = "//div[p[@class='f_15'][text()='Email Found']]"
address_xpath = "//div[@class='web_key' and text()='Address']/following-sibling::div[@class='web_val']"
web_cat_xpath =  "//div[@class='web_key' and text()='Website Categories']/following-sibling::div[@class='web_pill_flex']/div[@class='web_pill']"
contact_profile_xpath ="(//strong[normalize-space()='Contact Profile'])[1]"
phone_data_xpath = "//div[@class='m-b-15' and .//p[@class='web_key' and text()='Phone']]"
email_data_xpath = "//div[@class='m-b-15' and .//div[@class='web_key' and text()='Email']]"
crawl_status_xpath = "(//label[@class='crawling-name m-0']/following-sibling::p[contains(@class, 'data-crawling')])[1]"
risk_status_xpath = "(//p[@class='data__number text-warning text-capitalize'])[1]"
company_crawl = "(//div[contains(@class,'web_val')])[1]"
contact_url_xpath = "//div[@class='m-b-15' and .//div[@class='web_key' and text()='Contact Url']]"

json_btn_xpath = "//div[contains(text(),'View json')]"
json_copy_xpath = "//body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]"
json_download_xpath = "//img[@class='json_icon']"
crawl_place_next_xpath = "//button[normalize-space()='Next']"
crawl_place_prev_xpath = "//button[normalize-space()='Prev']"

crawl_place_loader_xpath = "//div[@class='ant-select-selector']"
crawl_place_100_xpath = "//div[contains(text(),'100')]"

dr ="(//span[contains(text(),'Data Repository')])[2]"

# filter

filter_xpath = "//span[normalize-space()='Filters']"

