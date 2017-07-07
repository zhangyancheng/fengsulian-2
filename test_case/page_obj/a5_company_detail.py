import os
from time import sleep
from public.base import Page
from config import globalparam
from test_case.page_obj.a4_authentication_center import  center
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a5_sta")

class cpy_detail(center,Page):
    """
    企业中心的填写企业详情页面
    """
    url = "/user/company/confirm"
    #定位器
    company_slogan_loc = ("xpath", ".//*[@id='slogan']")
    company_picture_loc = ("xpath", "//form/div[3]/div/div/div/div/div[2]/span/span[2]/div/div[1]/div/div[3]/label")
    company_introduce_loc = ("xpath", "//form/div[3]/div/div/div/div/div[5]/div/div[2]")
    business_introduction_loc = ("xpath", "//form/div[3]/div/div/div/div/div[6]/div/div[2]")
    next_step2_loc = ("css selector", "a[class = 'per_sure btn_submit2']")

    #action
    def company_slogan(self,slogan):
        """企业标语"""
        self.clear_type(self.company_slogan_loc,slogan)
    def company_picture(self):
        """上传公司图片"""
        self.click(self.company_picture_loc)
        os.system(globalparam.auto_path + "./" + "upload_credentials.exe")
    def company_introduce(self,comtext):
        """公司介绍"""
        self.clear_type(self.company_introduce_loc,comtext)
    def business_introduction(self,bustext):
        """业务介绍"""
        self.clear_type(self.business_introduction_loc,bustext)
    def next_step2(self):
        self.click(self.next_step2_loc)

    #企业详情入口
    def write_detaill(self,slogan = data1[0]['slogan'],comtext = data1[0]['comtext'],bustext = data1[0]['bustext']):
        """入口1"""
        center(self.driver).upload_information1()
        self.company_slogan(slogan)
        # self.company_picture()
        # sleep(1)
        self.company_introduce(comtext)
        self.business_introduction(bustext)
        self.next_step2()
    def write_detail2(self,slogan = data1[0]['slogan'],comtext = data1[0]['comtext'],bustext = data1[0]['bustext']):
        """入口2"""
        center(self.driver).upload_information3()
        self.company_slogan(slogan)
        # self.company_picture()
        # sleep(1)
        self.company_introduce(comtext)
        self.business_introduction(bustext)
        self.next_step2()
        # sleep(5)

    #定位器
    company_slo_error_loc = ("xpath", "//form/div[3]/div/div/div/div/div[1]/span")
    company_int_error_loc = ("xpath", "html/body/div[3]/div/div/form/div[3]/div/div/div/div/div[5]/label/span[1]")
    business_int_error_loc = ("xpath", "html/body/div[3]/div/div/form/div[3]/div/div/div/div/div[6]/label/span[1]")
    company_int_success_loc = ("xpath", "//form/div[5]/div[1]/div/div[1]/label/span")
    #action
    def company_slo_error(self,actual):
        """企业标语"""
        return self.is_text_in_element(self.company_slo_error_loc,actual)
    def company_int_error(self,actual):
        """公司介绍"""
        return self.is_text_in_element(self.company_int_error_loc,actual)
    def business_int_error(self,actual):
        """项目介绍"""
        return self.is_text_in_element(self.business_int_error_loc,actual)
    def company_int_success(self,actual):
        """资料正确"""
        return self.is_text_in_element(self.company_int_success_loc,actual)