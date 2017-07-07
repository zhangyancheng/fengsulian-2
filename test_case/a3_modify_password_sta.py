import unittest
from public import function,myunit
from public.base import Page
from test_case.page_obj.a3_modify_password import password
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a3_sta")

"""个人中心/安全设置修改->3"""
# @unittest.skip("跳过此用例")
class passwordTest(myunit.MyTest,Page):
    """登录密码修改"""
    def test_modify_password1(self,expected=True):
        """旧密码输入为空"""
        po = password(self.driver)
        po.modify_password_entry1(password1 = data1[1]['pwd1'])
        self.assert_equal(po.old_password_null(actual=data1[1]['result']),expected)
        function.insert_img(self.driver,data1[1]["screenshot_name"])

    def test_modify_password2(self,expected=True):
        """新密码输入为空"""
        po = password(self.driver)
        po.modify_password_entry2(password2 = data1[2]['pwd2'])
        self.assert_equal(po.new_password_null(actual=data1[2]['result']),expected)
        function.insert_img(self.driver,data1[2]["screenshot_name"])

    def test_modify_password3(self,expected=True):
        """重复新密码为空"""
        po = password(self.driver)
        po.modify_password_entry2(password3 = data1[3]['pwd3'])
        self.assert_equal(po.repeat_password_null(actual=data1[3]['result']),expected)
        function.insert_img(self.driver,data1[3]["screenshot_name"])

    # def test_modify_password4(self,expected=True):
    #     """密码修改成功"""
    #     self.modify_password_verify(password1 = data1['password4'],
    #        password2= data1['password44'],password3= data1['password444'])
    #     po = password(self.driver)
    #     self.assertEqual(po.modify_success(actual=data1['result4']),expected)
    #     function.insert_img(self.driver,"a3_4.jpg")

if __name__ == "__main__":
    unittest.main()
