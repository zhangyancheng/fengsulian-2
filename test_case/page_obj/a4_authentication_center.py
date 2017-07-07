import os
from time import sleep
from public.base import Page
from .login_enter import Log_on
from config import globalparam
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a4_sta")

class center(Log_on,Page):
    """
    企业中心的认证中心页面
    """
    url = "/user/company/confirm"
    #定位器
    enter_authentication_loc = ("xpath", "/html/body/div[3]/div/div/p[3]/a[1]")
    company_name_loc = ("name", "enterpriseName")
    license_number_loc = ("name", "businessLicense")
    upload_credentials_loc = ("xpath", "//form/div[1]/div/div[3]/div[2]/div/span[2]/span")
    select_picture_loc = ("css selector", "label[class = 'btn_select_file']")
    confirm_upload_loc = ("css selector", "div[class = 'submit btn_com btn_blue cropper_upload w140']")
    select_province_loc1 = ("id", "areaOut1")
    select_province_loc2 = ("xpath", ".//*[@id='sArea1Id']/li[3]")
    select_city_loc1 = ("id", "areaOut2")
    select_city_loc2 = ("xpath", ".//*[@id='sArea2Id']/li[2]")
    select_area_loc1 = ("id", "areaOut3")
    select_area_loc2 = ("xpath", ".//*[@id='sArea3Id']/li[2]")
    company_address_loc = ("name", "address")
    company_phone_loc = ("name", "linkManPhone")
    contacts_loc = ("name", "linkMan")
    contact_title_loc = ("name", "linkManJob")
    contact_email_loc = ("name", "linkManEmail")
    contact_phone_loc = ("name", "linkManMobile")
    next_step_loc = ("css selector", "a[class = 'per_sure btn_submit']")

    #action
    #进入认证中心
    def enter_enthentication(self):
        sleep(2)
        self.click(self.enter_authentication_loc)
    def company_name(self,name):
        self.clear_type(self.company_name_loc,name)
    def license_number(self,number):
        self.clear_type(self.license_number_loc,number)
    def upload_credentials(self):
        self.click(self.upload_credentials_loc)
        self.click(self.select_picture_loc)
        os.system(globalparam.auto_path + "./" + "upload_credentials.exe")
        self.click(self.confirm_upload_loc)
    def select_area(self):
        self.click(self.select_province_loc1)
        self.click(self.select_province_loc2)
        self.click(self.select_city_loc1)
        self.click(self.select_city_loc2)
        self.click(self.select_area_loc1)
        self.click(self.select_area_loc2)
    def company_address(self,address):
        self.clear_type(self.company_address_loc,address)
    def company_phone(self,phone1):
        self.clear_type(self.company_phone_loc,phone1)
    def contacts(self,contact):
        self.clear_type(self.contacts_loc,contact)
    def contact_title(self,title):
        self.clear_type(self.contact_title_loc,title)
    def contact_email(self,email):
        self.clear_type(self.contact_email_loc,email)
    def contact_phone(self,phone2):
        self.clear_type(self.contact_phone_loc,phone2)
    def next_step(self):
        self.click(self.next_step_loc)

    #上传基本资料入口
    def upload_information1(self,name = data1[0]['name'],number = data1[0]['number'],address = data1[0]['address'],
        phone1 = data1[0]['phone1'],contact = data1[0]['contact'],title = data1[0]['title'],email = data1[0]['email'],
        phone2 = data1[0]['phone2']):
        """
        填写基本资料1
        """
        self.open()
        self.login_entry()
        # self.enter_enthentication()
        self.company_name(name)
        self.license_number(number)
        self.upload_credentials()
        self.select_area()
        self.company_address(address)
        self.company_phone(phone1)
        self.contacts(contact)
        self.contact_title(title)
        self.contact_email(email)
        self.contact_phone(phone2)
        sleep(1)
        self.next_step()

    def upload_information2(self, name=data1[0]['name'], number=data1[0]['number'], address=data1[0]['address'],
        phone1=data1[0]['phone1'], contact=data1[0]['contact'], title=data1[0]['title'],email=data1[0]['email'],
        phone2=data1[0]['phone2']):
        """
        填写基本资料2
        """
        self.open()
        # self.enter_enthentication()
        self.company_name(name)
        self.license_number(number)
        self.select_area()
        self.company_address(address)
        self.company_phone(phone1)
        self.contacts(contact)
        self.contact_title(title)
        self.contact_email(email)
        self.contact_phone(phone2)
        # sleep(1)
        self.next_step()

    def upload_information3(self, name=data1[0]['name'], number=data1[0]['number'], address=data1[0]['address'],
        phone1=data1[0]['phone1'], contact=data1[0]['contact'], title=data1[0]['title'],email=data1[0]['email'],
        phone2=data1[0]['phone2']):
        """
        填写基本资料3
        """
        self.open()
        # self.enter_enthentication()
        self.company_name(name)
        self.license_number(number)
        # self.upload_credentials()
        self.select_area()
        self.company_address(address)
        self.company_phone(phone1)
        self.contacts(contact)
        self.contact_title(title)
        self.contact_email(email)
        self.contact_phone(phone2)
        # sleep(1)
        self.next_step()

    #定位器
    company_name_null_loc = ("xpath", "//form/div[1]/div/div[1]/span[1]")
    license_number_null_loc = ("xpath", "//form/div[1]/div/div[2]/span[1]")
    company_address_null_loc = ("xpath", "//form/div[1]/div/div[5]/span[1]")
    company_phone_null_loc = ("xpath", "//form/div[1]/div/div[6]/span[1]")
    contacts_null_loc = ("xpath", "//form/div[1]/div/div[7]/span[1]")
    contact_title_null_loc = ("xpath", "//form/div[1]/div/div[8]/span[1]")
    contact_email_null_loc = ("xpath", "//form/div[1]/div/div[9]/span[1]")
    contact_phone_null_loc = ("xpath", "//form/div[1]/div/div[10]/span[1]")
    base_success_loc = ("xpath", "//form/div[3]/div/div/div/div/div[1]/label/span[1]")

    #输入框为空
    def company_name_null(self,actual):
        return self.is_text_in_element(self.company_name_null_loc,actual)
    def license_number_null(self,actual):
        return self.is_text_in_element(self.license_number_null_loc,actual)
    def company_address_null(self,actual):
        return self.is_text_in_element(self.company_address_null_loc,actual)
    def company_phone_null(self,actual):
        return self.is_text_in_element(self.company_phone_null_loc,actual)
    def contacts_null(self,actual):
        return self.is_text_in_element(self.contacts_null_loc,actual)
    def contact_title_null(self,actual):
        return self.is_text_in_element(self.contact_title_null_loc,actual)
    def contact_email_null(self,actual):
        return self.is_text_in_element(self.contact_email_null_loc,actual)
    def contact_phone_null(self,actual):
        return self.is_text_in_element(self.contact_phone_null_loc,actual)
    def base_success(self,actual):
        return self.is_text_in_element(self.base_success_loc,actual)

