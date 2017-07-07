import os
from time import sleep
from public.base import Page
from .login_enter import Log_on
from config import globalparam
from test_case.page_obj.a4_authentication_center import  center
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a6_sta")

class order_cond(center,Log_on,Page):
    """
    企业中心的设置接单条件页面
    """
    url = "/user/company/confirm"
    #定位器
    button_kind_loc = ("css selector", "span[class = 'add_scope add_area']")
    province_loc1 = ("xpath", "//form/div/span[1]/input[1]")
    province_loc2 = ("xpath", "//form/div/span[1]/ul/li[3]")
    city_loc1 = ("xpath", "//form/div/span[2]/input[1]")
    city_loc2 = ("xpath", "//form/div/span[2]/ul/li[2]")
    area_loc1 = ("xpath", "//form/div/span[3]/input[1]")
    area_loc2 = ("xpath", "//form/div/span[3]/ul/li[2]")
    button_confirm_loc1 = ("xpath", "html/body/div[5]/div/div[3]/div")
    select_trade_loc1 = ("id", "businessOut1")
    select_trade_loc2 = ("xpath", "//form/div[5]/div[1]/div/div[2]/span/ul/li[2]")
    select_project_loc1 = ("id", "businessOut2")
    select_project_loc2 = ("xpath", "//form/div[5]/div[1]/div/div[3]/span/ul/li[2]")
    delete_range_loc = ("class name", "close")
    button_confirm_loc2 = ("xpath", "html/body/div[5]/div/div[3]/div[1]")
    come_back1_loc = ("css selector", "a[href='javascript:goStep(1)']")
    come_back2_loc = ("css selector", "a[href='javascript:goStep(0)']")
    submit_audit_loc = ("css selector", "a[class = 'per_sure btn_submit3']")
    select_service_loc1 = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[2]/a[1]")
    select_service_loc2 = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[2]/a[2]")
    select_service_loc3 = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[2]/a[3]")
    select_service_loc4 = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[2]/a[4]")
    select_service_loc5 = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[2]/a[5]")
    select_service_loc6 = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[2]/a[6]")
    #action
    def increase_kind(self):
        """增加类别"""
        self.click(self.button_kind_loc)
        self.click(self.province_loc1)
        self.click(self.province_loc2)
        self.click(self.city_loc1)
        self.click(self.city_loc2)
        self.click(self.area_loc1)
        self.click(self.area_loc2)
        sleep(1)
        self.click(self.button_confirm_loc1)
    def delete_kind(self):
        """删除类别"""
        self.click(self.delete_range_loc)
        self.click(self.button_confirm_loc2)
    def select_trade(self):
        """选择所属行业"""
        sleep(1)
        self.click(self.select_trade_loc1)
        self.click(self.select_trade_loc2)
    def select_project(self):
        """选择服务项目"""
        sleep(1)
        self.click(self.select_project_loc1)
        self.click(self.select_project_loc2)
    def submit_audit(self):
        """提交审核"""
        self.click(self.submit_audit_loc)
    def come_back1(self):
        """返回填写企业详情页面"""
        self.click(self.come_back1_loc)
    def come_back2(self):
        """返回上传企业基本资料页面"""
        self.click(self.come_back2_loc)
    def select_services(self):
        """选择6个业务"""
        self.click(self.select_service_loc1)
        self.click(self.select_service_loc2)
        self.click(self.select_service_loc3)
        self.click(self.select_service_loc4)
        self.click(self.select_service_loc5)
        self.click(self.select_service_loc6)

    """入口无"""

    #定位器
    trade_null_loc = ("xpath", "//form/div[5]/div[1]/div/div[2]/span/span[1]")
    project_null_loc = ("xpath", "//form/div[5]/div[1]/div/div[3]/span/span[1]")
    increase_kind_loc = ("xpath", "//form/div[5]/div[1]/div/div[1]/div/span[1]")
    delete_kind_loc = ("css selector", "span[class = 'add_scope add_area']")
    back_detail_loc = ("xpath", "//form/div[3]/div/div/div/div/div[1]/label/span[1]")
    back_base_loc = ("xpath", "//form/div[1]/div/div[1]/label/span")
    all_services_loc = ("xpath", "//form/div[5]/div[1]/div/div[4]/span[1]")
    double_checked_loc = ("xpath", "/html/body/div[5]/div/div[2]/div")

    #action
    def trade_null(self,actual):
        """所属行业选择为空"""
        return self.is_text_in_element(self.trade_null_loc,actual)
    def project_null(self,actual):
        """服务项目为空"""
        return self.is_text_in_element(self.project_null_loc,actual)
    def increkind_success(self,actual):
        """类别增加成功"""
        return self.is_text_in_element(self.increase_kind_loc,actual)
    def delekind_success(self,actual):
        """类别删除成功"""
        return self.is_text_in_element(self.delete_kind_loc,actual)
    def back_detail(self,actual):
        """返回至填写企业详情页面"""
        return self.is_text_in_element(self.back_detail_loc,actual)
    def back_base(self,actual):
        """返回至上传企业基本资料页面"""
        return self.is_text_in_element(self.back_base_loc,actual)
    def all_services(self,actual):
        """选择6个业务"""
        return self.is_text_in_element(self.all_services_loc,actual)
    def double_checked(self,actual):
        """重复审核提示"""
        return self.is_text_in_element(self.double_checked_loc,actual)

