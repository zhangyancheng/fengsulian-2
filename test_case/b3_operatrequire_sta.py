import unittest
from time import sleep
from public import function,myunit
from public.base import Page
from test_case.page_obj.b3_operat_requirement import oprequire
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b3_sta")

"""个人中心/需求列表"""
# @unittest.skip("跳过此用例")
class demand(myunit.MyTest,Page):
    """需求列表操作"""
    @unittest.skipIf(True, "为True的时候跳过")
    def test_operat_require1(self,expected=True):
        """点击编辑进入需求编辑"""
        po = oprequire(self.driver)
        po.next_open()
        po.login_entry()
        sleep(1)
        po.edit_demand()
        self.assert_equal(po.enter_edit(actual=data1[0]['result']), expected)
        function.insert_img(self.driver, data1[0]['screenshot_name'])

    def test_operat_require2(self,expected=True):
        """点击需求名称进入需求详情"""
        po = oprequire(self.driver)
        po.next_open()
        po.login_entry()
        po.click_describe()
        self.assert_equal(po.enter_describe(actual=data1[1]['result']), expected)
        function.insert_img(self.driver, data1[1]['screenshot_name'])

    def test_operat_require3(self,expected=True):
        """继续发布进入发布需求页面"""
        po = oprequire(self.driver)
        po.next_open()
        po.click_describe()
        po.continue_release()
        self.assert_equal(po.enter_edit(actual=data1[2]['result']), expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    @unittest.skipIf(True, "为True的时候跳过")
    def test_operat_require4(self,expected=True):
        """需求列表点击进入需求详情"""
        po = oprequire(self.driver)
        po.next_open()
        po.click_detail()
        self.assert_equal(po.enter_describe(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    @unittest.skipIf(True, "为True的时候跳过")
    def test_operat_require5(self,expected=True):
        """点击删除弹出提示框"""
        po = oprequire(self.driver)
        po.next_open()
        po.click_delete()
        self.assert_equal(po.enter_delete(actual=data1[4]['result']), expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    @unittest.skipIf(True, "为True的时候跳过")
    def test_operat_require6(self,expected=True):
        """成功取消删除操作"""
        po = oprequire(self.driver)
        po.next_open()
        po.click_delete()
        po.cancel_delete()
        self.assert_equal(po.cancel_success(actual=data1[5]['result']), expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    @unittest.skipIf(True, "为True的时候跳过")
    def test_operat_require7(self,expected=True):
        """成功删除需求"""
        po = oprequire(self.driver)
        po.next_open()
        po.click_delete()
        po.confirm_delete()
        self.assert_notequal(po.delete_success(actual=data1[6]['result']), expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
