from public.base import  Page
from .login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a8_sta")

class wallet(Log_on,Page):
    """
    个人钱包页面跳转
    """
    url = "/user/fund"

    #定位器
    top_up_loc = ("css selector", "a[class = 'btn_orange']")
    withdraw_deposit_loc = ("css selector", "a[class = 'btn_orange2']")
    red_packet_loc = ("css selector", "a[class = 'btn_blue_r']")
    trading_record_loc = ("css selector", "a[class = 'more_records']")
    #action
    def top_up(self):
        """跳转至充值页面"""
        self.click(self.top_up_loc)
    def withdraw_deposit(self):
        """跳转至提现页面"""
        self.click(self.withdraw_deposit_loc)
    def red_packet(self):
        """跳转至查看红包页面"""
        self.click(self.red_packet_loc)
    def trading_record(self):
        """查看交易记录"""
        self.click(self.trading_record_loc)
    def open_page(self):
        self.open()
    def enter_page(self):
        self.login_entry()

    """入口无"""

    #定位器
    topup_success_loc = ("xpath", "html/body/div[2]/div[2]/div/div/h1")
    deposit_success_loc = ("xpath", "html/body/div[2]/div[2]/div/div/h1")
    packet_success_loc = ("xpath", "html/body/div[2]/div[2]/div[1]/div/h1")
    record_success_loc = ("xpath", "html/body/div[2]/div[3]/div/h1")
    #action
    def topup_success(self,actual):
        return self.is_text_in_element(self.topup_success_loc,actual)
    def deposit_success(self,actual):
        return self.is_text_in_element(self.deposit_success_loc,actual)
    def packet_success(self,actual):
        return self.is_text_in_element(self.packet_success_loc,actual)
    def record_success(self,actual):
        return self.is_text_in_element(self.record_success_loc,actual)