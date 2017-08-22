from public.base import  Page
from .login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a7_sta")

class paypwd(Log_on,Page):
    """
    修改交易密码
    """
    url = "/user/fund/trader/password"

    #定位器
    button_pay_loc = ("class name", "setPassword")
    input_paypwd_loc = ("id", "payPassword")
    confirm_paypwd_loc = ("id", "payPassword1")
    identifying_code_loc = ("xpath", "//div[2]/div[2]/div/div[2]/div/form/div[3]/input[1]")
    confirm_modify_loc = ("css selector", "input[class = 'per_sure btn_submit']")
    #action
    def button_pay(self):
        """进入交易密码页面"""
        self.click(self.button_pay_loc)
    def input_paypwd(self,pay):
        """设置交易密码"""
        self.clear_type(self.input_paypwd_loc, pay)
    def confirm_paypwd(self,ppay):
        """确认交易密码"""
        self.clear_type(self.confirm_paypwd_loc, ppay)
    def iden_code(self,code):
        """输入验证码"""
        self.clear_type(self.identifying_code_loc, code)
    def confirm_modify(self):
        """确认修改交易密码"""
        self.click(self.confirm_modify_loc)

    #交易密码入口
    def modify_paypwd1(self):
        """入口1"""
        self.open()
        self.login_entry()
        self.button_pay()
    def modify_paypwd2(self,pay = data1[0]['pay'],ppay = data1[0]['ppay'],code = data1[0]['code']):
        """入口2"""
        self.open()
        self.button_pay()
        self.input_paypwd(pay)
        self.confirm_paypwd(ppay)
        self.iden_code(code)
        self.confirm_modify()

    #定位器
    enter_paypage_loc = ("xpath", "//form/div[1]/label/span")
    paypwd_error_loc = ("xpath", "//div[2]/div[2]/div/div[2]/div/form/div[1]/span[1]")
    ppypwd_error_loc = ("xpath", "//div[2]/div[2]/div/div[2]/div/form/div[2]/span[1]")
    code_error_loc = ("xpath", "//div[2]/div[2]/div/div[2]/div/form/div[3]/span[1]")
    #action
    def enter_paypage(self,actual):
        """进入交易密码页面"""
        return self.is_text_in_element(self.enter_paypage_loc, actual)
    def paypwd_error(self,actual):
        """设置交易密码错误"""
        return self.is_text_in_element(self.paypwd_error_loc, actual)
    def ppaypwd_error(self,actual):
        """确认交易密码错误"""
        return self.is_text_in_element(self.ppypwd_error_loc, actual)
    def code_error(self,actual):
        """验证码错误"""
        return self.is_text_in_element(self.code_error_loc, actual)


