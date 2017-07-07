from public.base import Page
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a1_sta")

class Log_on(Page):
    """
    用户登录页面
    """
    #定位器
    login_username_loc = ("id","username")
    login_password_loc = ("id","password")
    login_button_loc = ("css selector","input[class = 'btn_com btn_blue login_btn_submit sy_in']")
    #Action
    def login_entry(self,username = data1[0]['username'],password = data1[0]['password']):
        """用户登录成功"""
        self.clear_type(self.login_username_loc,username)
        self.clear_type(self.login_password_loc,password)
        self.click(self.login_button_loc)

