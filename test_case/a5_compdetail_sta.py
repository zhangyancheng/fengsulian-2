import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a5_company_detail import cpy_detail
from time import sleep
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a5_sta")

"""企业中心/认证企业/填写企业详情->8"""
# @unittest.skip("跳过此用例")
class detailTest(myunit.MyTest,Page):
    """企业中心填写企业详情"""
    def test_company_detail1(self,expected=True):
        """企业标语输入为空"""
        cpy_detail(self.driver).write_detaill(slogan = data1[1]['slogan'])
        po = cpy_detail(self.driver)
        self.assert_equal(po.company_slo_error(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_company_detail2(self,expected=True):
        """企业标语输入1位文字"""
        cpy_detail(self.driver).write_detail2(slogan=data1[2]['slogan'])
        po = cpy_detail(self.driver)
        self.assert_equal(po.company_slo_error(actual=data1[2]['result']),expected)
        function.insert_img(self.driver, data1[2]['screenshot_name'])

    def test_company_detail3(self,expected=True):
        """企业标语输入31位文字"""
        cpy_detail(self.driver).write_detail2(slogan=data1[3]['slogan'])
        po = cpy_detail(self.driver)
        self.assert_equal(po.company_slo_error(actual=data1[3]['result']),expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    # def test_company_detail4(self):
    #     """公司介绍输入为空"""
    #     cpy_detail(self.driver).write_detail2(slogan=data1[4]['slogan'],comtext=data1[4]['comtext'])
    #     po = cpy_detail(self.driver)
    #     self.assert_equal(po.company_int_error(actual=data1[4]['result']),expected)
    #     function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_company_detail5(self,expected=True):
        """公司介绍输入99位文字"""
        cpy_detail(self.driver).write_detail2(slogan=data1[5]['slogan'], comtext=data1[5]['comtext'])
        po = cpy_detail(self.driver)
        self.assert_equal(po.company_int_error(actual=data1[5]['result']),expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    # def test_company_detail6(self,expected=True):
    #     """业务介绍输入为空"""
    #     cpy_detail(self.driver).write_detail2(bustext=data1[6]['bustext'])
    #     po = cpy_detail(self.driver)
    #     self.assert_equal(po.business_int_error(actual=data1[6]['result']),expected)
    #     function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_company_detail7(self,expected=True):
        """业务介绍输入99位"""
        cpy_detail(self.driver).write_detail2(bustext=data1[7]['bustext'])
        po = cpy_detail(self.driver)
        self.assert_equal(po.business_int_error(actual=data1[7]['result']),expected)
        function.insert_img(self.driver, data1[7]['screenshot_name'])

    def test_company_detail8(self,expected=True):
        """企业详情填写正确"""
        cpy_detail(self.driver).write_detail2()
        po = cpy_detail(self.driver)
        self.assert_equal(po.company_int_success(actual=data1[8]['result']),expected)
        function.insert_img(self.driver, data1[8]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
