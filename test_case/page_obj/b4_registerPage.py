from time import sleep
from test_case.page_obj.login_enter import  Log_on
from data.testdata.data_read import Test1
from public.base import Page
data1 = Test1().a1_data(sheet = "b4_sta")

class login_register(Page):
    """
    用户登录页面
    """
    url = "/register"

    #定位器
    input_phone_loc = ("id", "account")
    input_code_loc = ("id", "code")
    input_password_loc = ("id", "password")
    register_agree_loc = ("class name", "txt_blue")
    click_agree_loc = ("id", "userRegisterAgree")
    enter_login_loc = ("css selector", "a[class = 'btn_blue_r btn_com reg_go_login']")
    click_regisetr_loc = ("css selector", "a[class = 'btn_com btn_blue w100p btn_submit']")
    #action
    def input_phone(self,phone):
        """输入手机号"""
        self.clear_type(self.input_phone_loc,phone)
    def input_code(self,code):
        """输入验证码"""
        self.clear_type(self.input_code_loc,code)
    def input_password(self,pwd):
        """输入密码"""
        self.clear_type(self.input_password_loc,pwd)
    def register_agree(self):
        """进入注册协议"""
        self.click(self.register_agree_loc)
        self.into_new_window()
    def click_agree(self):
        """点击同意协议"""
        self.click(self.click_agree_loc)
    def enter_login(self):
        """进入登录"""
        self.click(self.enter_login_loc)
    def click_register(self):
        """点击注册"""
        self.click(self.click_regisetr_loc )
    def next_open(self):
        self.open()

    def register1(self,phone=data1[0]["phone"],code=data1[0]["code"],pwd=data1[0]["pwd"]):
        """注册入口1"""
        self.next_open()
        self.input_phone(phone)
        self.input_code(code)
        self.input_password(pwd)

    #定位器
    phone_error_loc = ("xpath", "//form/div/div[2]/span[1]")
    code_error_loc = ("xpath", "//form/div/div[3]/span[1]")
    pwd_error_loc = ("xpath", "//form/div/div[4]/span[1]")
    enter_agree_loc = ("xpath", "//div[2]/div[1]/h1")
    not_agree_loc = ("css selector", "span[class = 'wrong registerAlert']")
    enterlogin_suc_loc = ("xpath", "//div[2]/div[2]/div/div[1]/p/span[1]")
    #action
    def phone_error(self,actual):
        return self.is_text_in_element(self.phone_error_loc, actual)
    def code_error(self,actual):
        return self.is_text_in_element(self.code_error_loc, actual)
    def pwd_error(self,actual):
        return self.is_text_in_element(self.pwd_error_loc, actual)
    def enter_agree(self,actual):
        return self.is_text_in_element(self.enter_agree_loc, actual)
    def not_agree(self,actual):
        return self.is_text_in_element(self.not_agree_loc, actual)
    def enterlogin_suc(self,actual):
        return self.is_text_in_element(self.enterlogin_suc_loc,actual)



