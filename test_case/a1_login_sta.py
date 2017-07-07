import unittest
import ddt
from data.testdata.data_read import Test1
from public import myunit,function
from public.base import Page
from test_case.page_obj.a1_loginPage import login
data1 = Test1().a1_data(sheet = "a1_sta")

"""用户登录->3"""
# @ddt.ddt
# @unittest.skip("跳过此用例")
class loginTest(myunit.MyTest,Page):
    "风速链用户登录"

    def test_login1(self,expected=True):
        """用户名为空,密码正确"""
        po = login(self.driver)
        po.user_login(username = data1[1]['username'])
        self.assert_equal(po.user_null_hint(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_login2(self,expected=True):
        """用户名正确,密码为空"""
        po = login(self.driver)
        po.user_login(password=data1[2]['password'])
        self.assert_equal(po.pawd_null_hint(actual=data1[2]['result']),expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    #@ddt.data(*data1)
    def test_login3(self,expected=True):
        """用户名密码正确,登录成功"""
        po = login(self.driver)
        po.user_login(username=data1[3]['username'], password=data1[3]['password'])
        self.assert_equal(po.user_login_success(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()


