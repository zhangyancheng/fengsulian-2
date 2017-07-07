import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a8_personal_wallet import wallet
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a8_sta")

"""个人中心/个人钱包/页面跳转"""
# @unittest.skip("跳过此用例")
class walletTest(myunit.MyTest,Page):
    """个人钱包页面确认"""
    def test_wallet_skip1(self,expected=True):
        """成功进入充值页面"""
        po = wallet(self.driver)
        po.open_page()
        po.enter_page()
        po.top_up()
        self.assert_equal(po.topup_success(actual=data1[0]['result']), expected)
        function.insert_img(self.driver, data1[0]['screenshot_name'])

    def test_wallet_skip2(self,expected=True):
        """成功进入提现页面"""
        po = wallet(self.driver)
        po.open_page()
        po.withdraw_deposit()
        self.assert_equal(po.deposit_success(actual=data1[1]['result']), expected)
        function.insert_img(self.driver, data1[1]['screenshot_name'])

    def test_wallet_skip3(self,expected=True):
        """成功进入红包页面"""
        po = wallet(self.driver)
        po.open_page()
        po.red_packet()
        self.assert_equal(po.packet_success(actual=data1[2]['result']), expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_wallet_skip4(self,expected=True):
        """成功进入交易记录页面"""
        po = wallet(self.driver)
        po.open_page()
        po.trading_record()
        self.assert_equal(po.record_success(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
