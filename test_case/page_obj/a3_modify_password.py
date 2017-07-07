from selenium.webdriver.common.by import By
from public.base import  Page
from .login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a3_sta")

class password(Log_on,Page):
    """
    个人中心的安全设置页面
    """
    url = "/user/fund/trader/password"
    #定位器
    old_password_loc = ("css selector", "input[placeholder = '请输入旧密码']")
    new_password_loc = ("css selector", "input[id = 'newPassword1']")
    repeat_password_loc = ("css selector", "input[id = 'newPassword2']")
    button_password_loc = ("css selector", "a[class = 'btn_com   btn_submit_p']")

    #action
    #进入安全设置界面并修改密码
    def old_password(self, password1):
        """输入旧密码"""
        self.clear_type(self.old_password_loc, password1)
    def new_password(self,password2):
        """输入新密码"""
        self.clear_type(self.new_password_loc, password2)
    def repeat_password(self,password2):
        """重新输入"""
        self.clear_type(self.repeat_password_loc, password2)
    def button_password(self):
        """确认修改"""
        self.click(self.button_password_loc)

    #修改密码入口
    def modify_password_entry1(self, password1=data1[0]['pwd1'], password2=data1[0]['pwd2'],
                                password3=data1[0]['pwd3']):
        """安全设置页面入口1"""
        self.open()
        self.login_entry()
        self.old_password(password1)
        self.new_password(password2)
        self.repeat_password(password3)
        self.button_password()
    def modify_password_entry2(self, password1=data1[0]['pwd1'], password2=data1[0]['pwd2'],
                               password3=data1[0]['pwd3']):
        """安全设置页面入口2"""
        self.open()
        self.old_password(password1)
        self.new_password(password2)
        self.repeat_password(password3)
        self.button_password()

    #定位器
    old_password_null_loc = ("xpath", "//div[2]/div[2]/div/div[1]/div[1]/form/div[1]/span[2]")
    new_password_null_loc = ("xpath", "//div[2]/div[2]/div/div[1]/div[1]/form/div[2]/span[2]")
    repeat_password_null_loc = ("xpath", "//div[2]/div[2]/div/div[1]/div[1]/form/div[3]/span[2]")
    modify_success_loc = ("css selector", "html body div.dialog_pop div.dialog_box div.dialog_main div.dialog_main.dialog_alert")
    #action
    def old_password_null(self,actual):
        """旧密码为空"""
        return self.is_text_in_element(self.old_password_null_loc,actual)
    def new_password_null(self,actual):
        """新密码为空"""
        return self.is_text_in_element(self.new_password_null_loc,actual)
    def repeat_password_null(self,actual):
        """重复密码为空"""
        return self.is_text_in_element(self.repeat_password_null_loc,actual)
    def modify_success(self,actual):
        """更改成功"""
        return self.is_text_in_element(self.modify_success_loc,actual)
