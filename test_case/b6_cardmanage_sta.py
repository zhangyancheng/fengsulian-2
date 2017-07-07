import unittest
from public.exceptionscr import Screen
from time import sleep
from public import function,myunit
from public.base import Page
from test_case.page_obj.login_enter import Log_on
from test_case.page_obj.b6_card_manage import card_manage
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b6_sta")

"""个人中心/名片管理"""
class cardmanageTest(myunit.MyTest,Page):
    """企业名片管理"""
    #@Screen(driver)
    def test_card_mannage1(self, expected=True):
        """企业名片收藏成功"""
        po = card_manage(self.driver)
        po.card_manage1()
        self.assert_equal(po.collectcard_success(actual=data1[0]["result"]), expected)
        function.insert_img(self.driver, data1[0]["screenshot_name"])

    def test_card_mannage2(self, expected=True):
        """查看收藏企业名片"""
        po = card_manage(self.driver)
        po.next_open()
        po.view_collectcard()
        self.assert_equal(po.view_card(actual=data1[1]["result"]), expected)
        function.insert_img(self.driver, data1[1]["screenshot_name"])

    def test_card_mannage3(self, expected=True):
        """弹出删除名片提示框"""
        po = card_manage(self.driver)
        po.next_open()
        po.click_delete()
        self.assert_equal(po.delete_box(actual=data1[2]["result"]), expected)
        function.insert_img(self.driver, data1[2]["screenshot_name"])

    def test_card_mannage4(self, expected=True):
        """取消删除企业名片"""
        po = card_manage(self.driver)
        po.next_open()
        po.click_delete()
        po.click_cancel()
        self.assert_equal(po.cancel_delete(actual=data1[3]["result"]), expected)
        function.insert_img(self.driver, data1[3]["screenshot_name"])

    def test_card_mannage5(self, expected=True):
        """取消删除企业名片"""
        po = card_manage(self.driver)
        po.next_open()
        po.click_delete()
        po.click_confrim()
        self.assert_equal(po.confirm_delete(actual=data1[4]["result"]), expected)
        function.insert_img(self.driver, data1[4]["screenshot_name"])

if __name__ == "__main__":
    unittest.main()
