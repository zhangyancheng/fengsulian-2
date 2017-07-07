import unittest
from time import sleep
from public import function,myunit
from public.base import Page
from test_case.page_obj.login_enter import Log_on
from test_case.page_obj.b5_card_collection import card_collection
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b5_sta")

"""名片收藏"""
class cardcollectTest(myunit.MyTest,Log_on,Page):
    """收藏企业名片"""
    def test_card_collection1(self, expected=True):
        """进入名片管理页面"""
        po = card_collection(self.driver)
        po.enter_card1()
        self.assert_equal(po.enter_cardmanage(actual=data1[0]["result"]), expected)
        function.insert_img(self.driver, data1[0]["screenshot_name"])

    def test_card_collection2(self, expected=True):
        """跳转至查看企业列表"""
        po = card_collection(self.driver)
        po.next_open()
        po.view_enterprise()
        self.assert_equal(po.viewenter_success(actual=data1[1]["result"]), expected)
        function.insert_img(self.driver, data1[1]["screenshot_name"])

    def test_card_collection3(self, expected=True):
        """查看当前企业名片"""
        po = card_collection(self.driver)
        po.next_open()
        po.view_enterprise()
        po.view_card()
        self.assert_equal(po.viewcard_success(actual=data1[2]["result"]), expected)
        function.insert_img(self.driver, data1[2]["screenshot_name"])

    def test_card_collection4(self, expected=True):
        """收藏企业名片"""
        po = card_collection(self.driver)
        po.next_open()
        po.view_enterprise()
        po.view_card()
        po.click_collect()
        self.assert_equal(po.collect_success(actual=data1[3]["result"]), expected)
        function.insert_img(self.driver, data1[3]["screenshot_name"])

if __name__ == "__main__":
    unittest.main()
