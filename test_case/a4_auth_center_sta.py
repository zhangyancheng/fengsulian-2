import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a4_authentication_center import center
from time import sleep
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a4_sta")

"""企业中心/认证企业/上传企业基本资料->21"""
# @unittest.skip("跳过此用例")
class centerTest(myunit.MyTest,Page):
    """上传企业基本资料"""
    def test_basic_document1(self,expected=True):
        """公司名称为空"""
        center(self.driver).upload_information1(name = data1[1]['name'])
        po = center(self.driver)
        self.assert_equal(po.company_name_null(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]['screenshot_name'])

    def test_basic_document2(self,expected=True):
        """公司名称输入3位"""
        center(self.driver).upload_information2(name = data1[2]['name'])
        po = center(self.driver)
        self.assert_equal(po.company_name_null(actual=data1[2]['result']),expected)
        function.insert_img(self.driver,data1[2]['screenshot_name'])

    def test_basic_document3(self,expected=True):
        """公司名称输入21位"""
        center(self.driver).upload_information2(name = data1[3]['name'])
        po = center(self.driver)
        self.assert_equal(po.company_name_null(actual=data1[3]['result']),expected)
        function.insert_img(self.driver,data1[3]['screenshot_name'])

    def test_basic_document4(self,expected=True):
        """营业执照编号为空"""
        center(self.driver).upload_information2(number = data1[4]['number'])
        po = center(self.driver)
        self.assert_equal(po.license_number_null(actual=data1[4]['result']),expected)
        function.insert_img(self.driver,data1[4]['screenshot_name'])

    def test_basic_document5(self,expected=True):
        """营业执照编号输入错误"""
        center(self.driver).upload_information2(number = data1[5]['number'])
        po = center(self.driver)
        self.assert_equal(po.license_number_null(actual=data1[5]['result']),expected)
        function.insert_img(self.driver,data1[5]['screenshot_name'])

    def test_basic_document6(self,expected=True):
        """公司地址为空"""
        center(self.driver).upload_information2(address = data1[6]['address'])
        po = center(self.driver)
        self.assert_equal(po.company_address_null(actual=data1[6]['result']),expected)
        function.insert_img(self.driver, data1[6]['screenshot_name'])

    def test_basic_document7(self,expected=True):
        """公司地址输入1位"""
        center(self.driver).upload_information2(address = data1[7]['address'])
        po = center(self.driver)
        self.assert_equal(po.company_address_null(actual=data1[7]['result']),expected)
        function.insert_img(self.driver, data1[7]['screenshot_name'])

    def test_basic_document8(self,expected=True):
        """公司电话为空"""
        center(self.driver).upload_information2(phone1 = data1[8]['phone1'])
        po = center(self.driver)
        self.assert_equal(po.company_phone_null(actual=data1[8]['result']),expected)
        function.insert_img(self.driver, data1[8]['screenshot_name'])

    def test_basic_document9(self,expected=True):
        """公司电话输入错误"""
        center(self.driver).upload_information2(phone1 = data1[9]['phone1'])
        po = center(self.driver)
        self.assert_equal(po.company_phone_null(actual=data1[9]['result']),expected)
        function.insert_img(self.driver, data1[9]['screenshot_name'])

    def test_basic_documentA(self,expected=True):
        """联系人姓名为空"""
        center(self.driver).upload_information2(contact = data1[10]['contact'])
        po = center(self.driver)
        self.assert_equal(po.contacts_null(actual=data1[10]['result']),expected)
        function.insert_img(self.driver, data1[10]['screenshot_name'])

    def test_basic_documentB(self,expected=True):
        """联系人姓名输入1位"""
        center(self.driver).upload_information2(contact = data1[11]['contact'])
        po = center(self.driver)
        self.assert_equal(po.contacts_null(actual=data1[11]['result']),expected)
        function.insert_img(self.driver, data1[11]['screenshot_name'])

    def test_basic_documentC(self,expected=True):
        """联系人姓名输入11位"""
        center(self.driver).upload_information2(contact = data1[12]['contact'])
        po = center(self.driver)
        self.assert_equal(po.contacts_null(actual=data1[12]['result']),expected)
        function.insert_img(self.driver, data1[12]['screenshot_name'])

    def test_basic_documentD(self,expected=True):
        """联系人职位为空"""
        center(self.driver).upload_information2(title = data1[13]['title'])
        po = center(self.driver)
        self.assert_equal(po.contact_title_null(actual=data1[13]['result']),expected)
        function.insert_img(self.driver, data1[13]['screenshot_name'])

    def test_basic_documentE(self,expected=True):
        """联系人职位输入1位"""
        center(self.driver).upload_information2(title = data1[14]['title'])
        po = center(self.driver)
        self.assert_equal(po.contact_title_null(actual=data1[14]['result']),expected)
        function.insert_img(self.driver, data1[14]['screenshot_name'])

    def test_basic_documentF(self,expected=True):
        """联系人职位输入11位"""
        center(self.driver).upload_information2(title = data1[15]['title'])
        po = center(self.driver)
        self.assert_equal(po.contact_title_null(actual=data1[15]['result']),expected)
        function.insert_img(self.driver, data1[15]['screenshot_name'])

    def test_basic_documentG(self,expected=True):
        """邮箱为空"""
        center(self.driver).upload_information2(email = data1[16]['email'])
        po = center(self.driver)
        self.assert_equal(po.contact_email_null(actual=data1[16]['result']),expected)
        function.insert_img(self.driver, data1[16]['screenshot_name'])

    def test_basic_documentH(self,expected=True):
        """邮箱输入错误"""
        center(self.driver).upload_information2(email = data1[17]['email'])
        po = center(self.driver)
        self.assert_equal(po.contact_email_null(actual=data1[17]['result']),expected)
        function.insert_img(self.driver, data1[17]['screenshot_name'])

    def test_basic_documentI(self,expected=True):
        """联系方式为空"""
        center(self.driver).upload_information2(phone2 = data1[18]['phone2'])
        po = center(self.driver)
        self.assert_equal(po.contact_phone_null(actual=data1[18]['result']),expected)
        function.insert_img(self.driver, data1[18]['screenshot_name'])

    def test_basic_documentJ(self,expected=True):
        """联系方式输入10位"""
        center(self.driver).upload_information2(phone2 = data1[19]['phone2'])
        po = center(self.driver)
        self.assert_equal(po.contact_phone_null(actual=data1[19]['result']),expected)
        function.insert_img(self.driver, data1[19]['screenshot_name'])

    def test_basic_documentK(self,expected=True):
        """联系方式输入12位"""
        center(self.driver).upload_information2(phone2 = data1[20]['phone2'])
        po = center(self.driver)
        self.assert_equal(po.contact_phone_null(actual=data1[20]['result']),expected)
        function.insert_img(self.driver, data1[20]['screenshot_name'])

    def test_basic_documentL(self,expected=True):
        """企业基本资料填写正确"""
        center(self.driver).upload_information3()
        sleep(1)
        po = center(self.driver)
        self.assert_equal(po.base_success(actual=data1[21]['result']),expected)
        function.insert_img(self.driver, data1[21]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()
