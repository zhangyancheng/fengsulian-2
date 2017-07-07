import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a9_recharge_amount import recharge
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a9_sta")

"""个人中心/个人钱包/充值"""
# @unittest.skip("跳过此用例")
class rechargeTest(myunit.MyTest,Page):
    """账户余额充值"""
    def test_recharge_amount1(self,expected=True):
        """验证输入框为空错误提示"""
        po = recharge(self.driver)
        po.money1(data1[1]['money'])
        self.assert_equal(po.write_null(actual=data1[1]['result']), expected)
        function.insert_img(self.driver, data1[1]['screenshot_name'])

    def test_recharge_amount2(self,expected=True):
        """金额输入为空充值"""
        po = recharge(self.driver)
        po.money2(data1[2]['money'])
        self.assert_equal(po.pay_fail(actual=data1[2]['result']), expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_recharge_amount3(self,expected=True):
        """跳转至联系客服"""
        po = recharge(self.driver)
        po.money2(data1[3]['money'])
        po.customer_service()
        self.assert_equal(po.skip_service(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    def test_recharge_amount4(self,expected=True):
        """金额输入10元充值"""
        po = recharge(self.driver)
        po.money2(data1[4]['money'])
        self.assert_equal(po.input_amount(actual=data1[4]['result']), expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_recharge_amount5(self,expected=True):
        """选择支付宝充值"""
        po = recharge(self.driver)
        po.money2(data1[5]['money'])
        po.select_alipay()
        po.click_pay()
        self.assert_equal(po.skip_paypage(actual=data1[5]['result']), expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
