import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.b1_withdraw_deposit import withdraw
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b1_sta")

"""个人中心/个人钱包/提现"""
# @unittest.skip("跳过此用例")
class depositTest(myunit.MyTest,Page):
    """余额提现至支付宝"""
    def test_withdraw_deposit1(self,expected=True):
        """支付宝姓名输入为空"""
        po = withdraw(self.driver)
        po.deposit1(name = data1[1]['name'])
        self.assert_equal(po.name_null(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_withdraw_deposit2(self,expected=True):
        """支付宝账号输入为空"""
        po = withdraw(self.driver)
        po.deposit2(uname = data1[2]['uname'])
        self.assert_equal(po.username_null(actual=data1[2]['result']),expected)
        function.insert_img(self.driver,data1[2]['screenshot_name'])

    def test_withdraw_deposit3(self,expected=True):
        """提现金额输入为空"""
        po = withdraw(self.driver)
        po.deposit2(money = data1[3]['money'])
        self.assert_equal(po.money_null(actual=data1[3]['result']),expected)
        function.insert_img(self.driver,data1[3]['screenshot_name'])

    def test_withdraw_deposit4(self,expected=True):
        """提现金额输入为空"""
        po = withdraw(self.driver)
        po.deposit2(pword = data1[4]['pword'])
        self.assert_equal(po.password_null(actual=data1[4]['result']),expected)
        function.insert_img(self.driver,data1[4]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
