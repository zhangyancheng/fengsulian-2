from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.fengsulian.com/user/cards")

driver.find_element_by_id("username").send_keys("15868147450")
driver.find_element_by_id("password").send_keys("12345678")
driver.find_element_by_css_selector("input[class = 'btn_com btn_blue login_btn_submit sy_in']").click()

# ele0 = driver.find_element_by_css_selector("a[class='per_active']").text    #定位器2【进入名片管理页面】
# print(ele0)
#
# driver.find_element_by_css_selector("a[class='ss_nearcom']").click()        #定位器1【点击查看企业】
# ele1 = driver.find_element_by_css_selector("a[href='/enterprise/1549']>h2").text     #定位器2【查看企业】
# print(ele1)
#
# driver.find_element_by_css_selector("div[class='wf_content_list_view fr']>a").click()   #定位器1【点击查看名片】
# ele2 = driver.find_element_by_css_selector("div[class='title cardName_ajax']").text     #定位器2【点击查看名片】
# print(ele2)
#
# driver.find_element_by_css_selector("i[class='fa fa-heart-o']").click()          #定位器1【点击收藏】
# ele3 = driver.find_element_by_css_selector("span[class='collect']").text        #定位器2【收藏成功】
# print(ele3)

driver.get("http://www.fengsulian.com/user/cards")
ele4 = driver.find_element_by_css_selector("p[class='p_text']").text             #定位器2【名片需求里收藏成功】
print(ele4)

# driver.find_element_by_css_selector("a[class='see_card']").click()               #定位器1【需求列表点击查看名片】
# print(ele3)

driver.find_element_by_css_selector("div[class='del_btn']>i").click()            #定位器1【点击删除收藏】
ele5 = driver.find_element_by_css_selector("div[class='dialog_main dialog_alert']").text  #定位器2【弹出删除收藏框】
print(ele5)

driver.find_element_by_css_selector("div[class='cancel btn_com btn_red ml30']") .click()   #定位器1【取消删除收藏】
print(ele4)

driver.find_element_by_css_selector("div[class='del_btn']>i").click()
sleep(1)
driver.find_element_by_css_selector("div[class='submit btn_com btn_blue']").click()        #定位器1【确定删除收藏】
sleep(1)
ele6 = driver.find_element_by_css_selector("a[class='ss_nearcom']").text                    #定位器2【确定删除收藏】
print(ele6)
sleep(3)
driver.quit()
