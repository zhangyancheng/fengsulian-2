import unittest
from time import sleep
from public import function,myunit
from public.base import Page
from test_case.page_obj.b4_registerPage import login_register
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b4_sta")

"""注册页面"""
class registerTest(myunit.MyTest,Page):
    """风速链用户注册"""
    def test_user_register1(self,expected=True):
        """手机号输入为空"""
        po = login_register(self.driver)
        po.register1(phone=data1[1]["phone"])
        po.click_register()
        self.assert_equal(po.phone_error(actual=data1[1]["result"]),expected)
        function.insert_img(self.driver, data1[1]['screenshot_name'])

    def test_user_register2(self,expected=True):
        """手机号输入有误"""
        po = login_register(self.driver)
        po.register1(phone=data1[2]["phone"])
        po.click_register()
        self.assert_equal(po.phone_error(actual=data1[2]["result"]),expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_user_register3(self,expected=True):
        """验证码输入有误"""
        po = login_register(self.driver)
        po.register1(code=data1[3]["code"])
        po.click_register()
        self.assert_equal(po.code_error(actual=data1[3]["result"]),expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    def test_user_register4(self,expected=True):
        """密码输入为空"""
        po = login_register(self.driver)
        po.register1(pwd=data1[4]["pwd"])
        po.click_register()
        self.assert_equal(po.pwd_error(actual=data1[4]["result"]),expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_user_register5(self,expected=True):
        """密码输入5位"""
        po = login_register(self.driver)
        po.register1(pwd=data1[5]["pwd"])
        po.click_register()
        self.assert_equal(po.pwd_error(actual=data1[5]["result"]),expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    def test_user_register6(self,expected=True):
        """手机号输入17位"""
        po = login_register(self.driver)
        po.register1(pwd=data1[6]["pwd"])
        po.click_register()
        self.assert_equal(po.pwd_error(actual=data1[6]["result"]),expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_user_register7(self,expected=True):
        """不同意注册协议"""
        po = login_register(self.driver)
        po.register1()
        po.click_agree()
        po.click_register()
        self.assert_equal(po.not_agree(actual=data1[7]["result"]),expected)
        function.insert_img(self.driver, data1[7]['screenshot_name'])

    def test_user_register8(self,expected=True):
        """进入登录页面"""
        po = login_register(self.driver)
        po.next_open()
        po.enter_login()
        self.assert_equal(po.enterlogin_suc(actual=data1[8]["result"]),expected)
        function.insert_img(self.driver, data1[8]['screenshot_name'])

    def test_user_register9(self,expected=True):
        """进入用户注册协议页面"""
        po = login_register(self.driver)
        po.next_open()
        po.register_agree()
        self.assert_equal(po.enter_agree(actual=data1[9]["result"]),expected)
        function.insert_img(self.driver, data1[9]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
