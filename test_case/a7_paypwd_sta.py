import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a7_pay_password import  paypwd
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a7_sta")

"""个人中心/设置交易密码->9"""
# @unittest.skip("跳过此用例")
class payTest(myunit.MyTest,Page):
    """设置交易密码"""
    def test_set_paypwd1(self,expected=True):
        """成功进入设置交易密码页面"""
        paypwd(self.driver).modify_paypwd1()
        po = paypwd(self.driver)
        self.assert_equal(po.enter_paypage(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_set_paypwd2(self,expected=True):
        """设置交易密码输入为空"""
        paypwd(self.driver).modify_paypwd2(pay = data1[2]['pay'])
        po = paypwd(self.driver)
        self.assert_equal(po.paypwd_error(actual=data1[2]['result']),expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_set_paypwd3(self,expected=True):
        """设置交易密码输入5位"""
        paypwd(self.driver).modify_paypwd2(pay = data1[3]['pay'])
        po = paypwd(self.driver)
        self.assert_equal(po.paypwd_error(actual=data1[3]['result']),expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    def test_set_paypwd4(self,expected=True):
        """设置交易密码输入17位"""
        paypwd(self.driver).modify_paypwd2(pay = data1[4]['pay'])
        po = paypwd(self.driver)
        self.assert_equal(po.paypwd_error(actual=data1[4]['result']),expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_set_paypwd5(self,expected=True):
        """重复交易密码输入为空"""
        paypwd(self.driver).modify_paypwd2(ppay = data1[5]['ppay'])
        po = paypwd(self.driver)
        self.assert_equal(po.ppaypwd_error(actual=data1[5]['result']),expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    def test_set_paypwd6(self,expected=True):
        """重复交易密码输入5位"""
        paypwd(self.driver).modify_paypwd2(ppay = data1[6]['ppay'])
        po = paypwd(self.driver)
        self.assert_equal(po.ppaypwd_error(actual=data1[6]['result']),expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_set_paypwd7(self,expected=True):
        """重复交易密码输入17位"""
        paypwd(self.driver).modify_paypwd2(ppay = data1[7]['ppay'])
        po = paypwd(self.driver)
        self.assert_equal(po.ppaypwd_error(actual=data1[7]['result']),expected)
        function.insert_img(self.driver, data1[7]['screenshot_name'])

    def test_set_paypwd8(self,expected=True):
        """验证码输入为空"""
        paypwd(self.driver).modify_paypwd2(code = data1[8]['code'])
        po = paypwd(self.driver)
        self.assert_equal(po.code_error(actual=data1[8]['result']),expected)
        function.insert_img(self.driver, data1[8]['screenshot_name'])

    def test_set_paypwd9(self,expected=True):
        """验证码输入错误"""
        paypwd(self.driver).modify_paypwd2()
        po = paypwd(self.driver)
        self.assert_equal(po.code_error(actual=data1[9]['result']),expected)
        function.insert_img(self.driver, data1[9]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()