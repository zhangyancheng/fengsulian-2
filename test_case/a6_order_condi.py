import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a5_company_detail import cpy_detail
from test_case.page_obj.a6_order_conditions import order_cond
from test_case.page_obj.login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a6_sta")

"""企业中心/认证企业/设置订单条件->7"""
class orderTest(myunit.MyTest,Log_on,Page):
    """企业中心填写设置填写条件"""
    # def test_order_conditions1(self):
    #     """所属行业选择为空"""
    #     cpy_detail(self.driver).write_detaill()
    #     po = order_cond(self.driver)
    #     po.submit_audit()
    #     self.assert_equal(po.trade_null(),data1[0]['result'])
    #     function.insert_img(self.driver, data1[0]['screenshot_name'])
    # def test_order_conditions2(self):
    #     """服务项目选择为空"""
    #     cpy_detail(self.driver).write_detail2()
    #     po = order_cond(self.driver)
    #     po.select_trade()
    #     self.assert_equal(po.project_null(),data1[1]['result'])
    #     function.insert_img(self.driver, data1[1]['screenshot_name'])
    # def test_order_conditions3(self):
    #     """成功添加接单范围类别"""
    #     cpy_detail(self.driver).write_detail2()
    #     po = order_cond(self.driver)
    #     self.assert_equal(po.increkind_success,data1[2]['result'])
    #     function.insert_img(self.driver, data1[2]['screenshot_name'])
    # def test_order_conditions4(self):
    #     """最多选择6项主营业务"""
    #     cpy_detail(self.driver).write_detail2()
    #     po = order_cond(self.driver)
    #     po.increase_kind()
    #     po.select_trade()
    #     po.select_project()
    #     po.select_services()
    #     self.assert_equal(po.all_services(),data1[3]['result'])
    #     function.insert_img(self.driver, data1[3]['screenshot_name'])
    # def test_order_conditions5(self):
    #     """成功删除接单范围类别"""
    #     cpy_detail(self.driver).write_detail2()
    #     po = order_cond(self.driver)
    #     po.delete_kind()
    #     self.assert_equal(po.delekind_success(),data1[4]['result'])
    #     function.insert_img(self.driver, data1[4]['screenshot_name'])
    # def test_order_conditions6(self):
    #     """返回填写企业详情页面"""
    #     cpy_detail(self.driver).write_detail2()
    #     po = order_cond(self.driver)
    #     po.come_back1()
    #     self.assert_equal(po.back_detail,data1[5]['result'])
    #     function.insert_img(self.driver, data1[5]['screenshot_name'])
    # def test_order_conditions7(self):
    #     """返回至上传企业基本资料页面"""
    #     cpy_detail(self.driver).write_detail2()
    #     po = order_cond(self.driver)
    #     po.come_back2()
    #     self.assert_equal(po.back_base(),data1[6]['result'])
    #     function.insert_img(self.driver, data1[6]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()