import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.b2_release_demand import release
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b2_sta")

"""个人中心/需求列表/发布需求"""
# @unittest.skip("跳过此用例")
class demand(myunit.MyTest,Page):
    """发布个人需求"""
    def test_relsdemand1(self,expected=True):
        """不同意交易协议"""
        po = release(self.driver)
        po.submit_demand1()
        self.assert_equal(po.not_agree(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_relsdemand2(self,expected=True):
        """未选择行业类目"""
        po = release(self.driver)
        po.submit_demand2()
        po.submit_comand()
        self.assert_equal(po.category_null(actual=data1[2]['result']),expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_relsdemand3(self,expected=True):
        """描述需求输入为空"""
        po = release(self.driver)
        po.submit_demand3(demand=data1[3]['demand'])
        po.submit_comand()
        self.assert_equal(po.demand_error(actual=data1[3]['result']),expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    def test_relsdemand4(self,expected=True):
        """描述需求输入31位"""
        po = release(self.driver)
        po.submit_demand3(demand=data1[4]['demand'])
        po.submit_comand()
        self.assert_equal(po.demand_error(actual=data1[4]['result']),expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_relsdemand5(self,expected=True):
        """具体要求输入为空"""
        po = release(self.driver)
        po.submit_demand3(require=data1[5]['require'])
        po.submit_comand()
        self.assert_equal(po.require_error(actual=data1[5]['result']),expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    def test_relsdemand6(self,expected=True):
        """未选择报价截止时间"""
        po = release(self.driver)
        po.submit_demand3()
        po.submit_comand()
        self.assert_equal(po.time_null(actual=data1[6]['result']),expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_relsdemand7(self,expected=True):
        """进入风速链交易协议页面"""
        po = release(self.driver)
        po.submit_demand2()
        po.trade_agreement()
        self.assert_equal(po.enter_agreement(actual=data1[7]['result']),expected)
        function.insert_img(self.driver, data1[7]['screenshot_name'])

    def test_relsdemand8(self,expected=True):
        """成功保存需求草稿"""
        po = release(self.driver)
        po.submit_demand3()
        po.cutoff_time()
        po.save_draft()
        self.assert_equal(po.draft_success(actual=data1[8]['result']),expected)
        function.insert_img(self.driver, data1[8]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
