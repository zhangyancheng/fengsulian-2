from time import sleep
from data.testdata.data_read import Test1
from public.base import Page
data1 = Test1().a1_data(sheet = "a1_sta")

class login(Page):
    """
    用户登录页面
    """
    url = "/login"
    #定位器
    login_username_loc = ("id","username")
    login_password_loc = ("id","password")
    login_button_loc = ("css selector","input[class = 'btn_com btn_blue login_btn_submit sy_in']")
    #Action
    def login_username(self,username):
        """输入用户名"""
        self.clear_type(self.login_username_loc,username )
    def login_password(self,password):
        """输入密码"""
        self.clear_type(self.login_password_loc,password)
    def login_button(self):
        """点击登录按钮"""
        self.click(self.login_button_loc)

    #定义统一登录入口
    def user_login(self,username = data1[0]['username'],password = data1[0]['password']):
        """
        获取的用户名密码登录
        """
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        # sleep(1)

    #定位器
    user_error_null_loc = ("css selector","div[class = 'in_r']")
    pawd_error_null_loc = ("xpath","//div[2]/div[2]/div/div[1]/form/div[2]/div/span[1]")
    user_login_success_loc = ("xpath","//div[1]/div[1]/div[1]/div/div[1]/div[1]/span")
    #Action
    def user_null_hint(self,actual):
        """用户名为空"""
        return self.is_text_in_element(self.user_error_null_loc,actual)
    def pawd_null_hint(self,actual):
        """密码为空"""
        return self.is_text_in_element(self.pawd_error_null_loc,actual)
    def user_login_success(self,actual):
        """成功登录获取当前账号"""
        return self.is_text_in_element(self.user_login_success_loc,actual)
