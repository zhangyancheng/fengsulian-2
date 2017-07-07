from public.base import  Page
from test_case.page_obj.login_enter import  Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b1_sta")

class withdraw(Log_on,Page):
    """
    金额提现
    """
    url = "/user/fund/cash"

    #定位器
    alipay_name_loc = ("xpath", "//form/div[1]/input[2]")
    alipay_username_loc = ("xpath", "//form/div[2]/input[2]")
    alipay_money_loc = ("id", "money")
    alipay_password_loc = ("xpath", "//form/div[4]/input")
    click_confirm_loc = ("css selector", "input[class = 'per_sure btn_submit']")
    #action
    def alipay_name(self, name):
        """支付姓名"""
        self.clear_type(self.alipay_name_loc,name)
    def alipay_username(self,username):
        """支付宝账号"""
        self.clear_type(self.alipay_username_loc,username)
    def alipay_money(self,money):
        """输入金额"""
        self.clear_type(self.alipay_money_loc,money)
    def alipay_password(self,password):
        """输入交易密码"""
        self.clear_type(self.alipay_password_loc,password)
    def click_confirm(self):
        """点击确定"""
        self.click(self.click_confirm_loc)

    def deposit1(self,name = data1[0]['name'],uname = data1[0]['uname'],
                 money = data1[0]['money'],pword = data1[0]['pword']):
        """提现入口1"""
        self.open()
        self.login_entry()
        self.alipay_name(name)
        self.alipay_username(uname)
        self.alipay_money(money)
        self.alipay_password(pword)
        self.click_confirm()

    def deposit2(self, name=data1[0]['name'], uname=data1[0]['uname'],
                 money=data1[0]['money'], pword=data1[0]['pword']):
        """提现入口2"""
        self.open()
        self.alipay_name(name)
        self.alipay_username(uname)
        self.alipay_money(money)
        self.alipay_password(pword)
        self.click_confirm()

    #定位器
    name_null_loc = ("xpath", "//form/div[1]/span[1]")
    username_null_loc = ("xpath", "//form/div[2]/span[1]")
    money_null_loc = ("xpath", "//form/div[3]/span[1]")
    password_null_loc = ("xpath", "//form/div[4]/span[1]")
    #action
    def name_null(self,actual):
        return self.is_text_in_element(self.name_null_loc,actual)
    def username_null(self,actual):
        return self.is_text_in_element(self.username_null_loc,actual)
    def money_null(self,actual):
        return self.is_text_in_element(self.money_null_loc,actual)
    def password_null(self,actual):
        return self.is_text_in_element(self.password_null_loc,actual)
