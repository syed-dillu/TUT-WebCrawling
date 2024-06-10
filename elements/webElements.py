
# Web

#web_crawl_xpath ="(//span[contains(text(),'AML')])[1]"
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
file_upload_xpath = "//span[normalize-space()='File Upload']"
download_icon_display = "//img[@alt='download']"
more_option_btn = "//span[normalize-space()='More options']"
more_appr_xpath = "//div[contains(text(),'Approve')]"
more_rejt_xpath = "//div[contains(text(),'Reject')]"
more_rejt_block_xpath = "//div[contains(text(),'Reject And Block')]"
web_title_xpath = "//h2[normalize-space()='websites history']"
web_filter_close_icon = "//img[@alt='close']"
web_form_close = "(//img[@class='close_icon mt-2'])[1]"
down_load_xpath = "//span[normalize-space()='Download Sample']"
file_upload_btn_xpath = "//span[contains(text(),'Click to Upload')]"
menu_icon_xpath = "//tbody/tr[2]/td[11]/span[1]/div[1]/div[1]"
view_details_xpath = "//div[contains(text(),'View Details')]"
back_btn = " //span[normalize-space()='Back']"
results_xpath = "//div[contains(text(),'Results')]"


file_xpath = "//span[contains(text(),'File Upload')]"
upload_xpath = "//input[@id='fileInput']"
ok_xpath = "//button[normalize-space()='Ok']"
risk_xpath = "//tbody/tr[2]/td[7]"
percent_xpath = "//tbody/tr[2]/td[7]/span[1]"
scroll_element = "//p[contains(text(),'Content Risk')]"
link_xpath = "//tbody/tr[2]/td[3]/a[1]/div[1]"
list_weburl_xpath = " //tbody/tr[2]/td[4]/div[1]"
list_trade_xpath = "//tbody/tr[2]/td[5]"
list_crawl_status_xpath = "//tbody/tr[2]/td[9]/span[1]"
list_risk_xpath = "//tbody/tr[2]/td[7]"
list_crawlstart_xpath = "//tbody/tr[2]/td[6]"

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
login_present_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"

web_category_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]"

# Game info
banned_xpath = "(//strong[normalize-space()='Banned Info'])[1]"
game_info_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[2]"
prohibhited_info_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/p[2]"
pharmeceutical_info_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p[2]"

#Security

security_xpath = "(//strong[normalize-space()='Security Analysis'])[1]"
malware_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
spam_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]"
untrusted_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]"



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
filter_click_xpath = "(//div[@class='ant-select-selector'])[2]"
fil_case_id = "//div[contains(text(),'Case Id')]"
fil_enter_xpath = "(//div[@class='ant-select-selector'])[3]"
fil_status_xpath = "(//div[@class='ant-select-selector'])[4]"
fil_pending_status = "//div[@title='pending']"
fil_url_xpath = "//div[contains(text(),'Website Url')]"
fil_trade_xpath = "//div[contains(text(),'Trade Name')]"
fil_url_xpath = "//div[contains(text(),'Risk Level')]"

# history reports

reports_xpath = "(//span[contains(text(),'Reports')])[2]"
his_reports_xpath = "(//span[contains(text(),'History Report')])[2]"
crawl_his_xpath = "(//h4[normalize-space()='Crawling History'])[1]"
view_report_xpath = "(//span[contains(text(),'View Report')])[2]"
filter_reports_xpath = "//span[normalize-space()='Filters']"
fil_report_url_xpath = "#rc_select_4"
fil_apply_xpath = "//span[normalize-space()='Apply']"



reports_link_xpath = "//tbody/tr[2]/td[3]"
reports_list_weburl_xpath = "//tbody/tr[2]/td[2]/div[1]"
reports_list_trade_xpath = "//tbody/tr[2]/td[5]"
reports_list_crawl_status_xpath = "//tbody/tr[2]/td[12]"
reports_list_risk_xpath = "//tbody/tr[2]/td[13]"
reports_list_riskscore_xpath = "//tbody/tr[2]/td[14]"
reports_list_createddata_xpath = "//tbody/tr[2]/td[1]"
reports_list_crawlstart_xpath = "//tbody/tr[2]/td[10]"


# Run ODD flow

result_type_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/p[1]"
end_data_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[1]"

run_ODD_xpath = "//span[normalize-space()='Run ODD']"
odd_history_xpath = "//span[normalize-space()='ODD History']"
history_logs_xpath = "//div[contains(@class,'header-tag')]"

parent_case_xpath = "/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]/p[1]"
parent_created_xpath = "//body/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[2]/p[1]"
parent_completed_per_xpath = "//body/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/p[1]"
parent_start_time_xpath = "//body/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[2]/p[2]"
child1_case_xpath = "/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/button[1]/p[1]"
child1_created_xpath = "//body/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/p[1]"
child1_completed_per_xpath = "//body/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/p[1]"
child1_start_time_xpath = "//body/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/p[2]"


child1_percentage_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/p[1]"
child1_crawl_status = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[1]"