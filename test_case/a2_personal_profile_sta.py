import unittest
from public import myunit,function
from public.base import Page
from test_case.page_obj.a2_personal_profile import personal
from data.testdata.data_read import Test1
from test_case.page_obj.login_enter import  Log_on
data1 = Test1().a1_data(sheet = "a2_sta")

"""个人中心/个人资料修改->7"""
# @unittest.skip("跳过此用例")
class PersonalTest(myunit.MyTest,Log_on,Page):
    """
    个人资料修改
    """
    def place_verify1(self):
        personal(self.driver).personal_alter3()
    def place_verify2(self):
        personal(self.driver).personal_alter4()
    def place_verify3(self):
        personal(self.driver).personal_alter5()
    def all_verify(self):
        personal(self.driver).personal_alter6()

    def test_personal_profile1(self,expected=True):
        """真实姓名输入1个文字"""
        personal(self.driver).personal_alter1(name = data1[3]['name'])
        po = personal(self.driver)
        self.assert_equal(po.modify_name(actual=data1[3]['result']), expected)
        function.insert_img(self.driver, data1[3]['screenshot_name'])

    def test_personal_profile2(self,expected=True):
        """真实姓名输入11个文字"""
        personal(self.driver).personal_alter2(name = data1[4]['name'])
        po = personal(self.driver)
        self.assert_equal(po.modify_name(actual=data1[4]['result']), expected)
        function.insert_img(self.driver, data1[4]['screenshot_name'])

    def test_personal_profile3(self,expected=True):
        """电子邮箱输入有误"""
        personal(self.driver).personal_alter2(email = data1[5]['email'])
        po = personal(self.driver)
        self.assert_equal(po.modify_email(actual=data1[5]['result']), expected)
        function.insert_img(self.driver, data1[5]['screenshot_name'])

    def test_personal_profile4(self,expected=True):
        """未选择省，提示请选择"""
        self.place_verify1()
        po = personal(self.driver)
        self.assert_equal(po.province_null(actual=data1[6]['result']),expected)
        function.insert_img(self.driver,data1[6]['screenshot_name'])

    def test_personal_profile5(self,expected=True):
        """未选择市，提示请选择"""
        self.place_verify2()
        po = personal(self.driver)
        self.assert_equal(po.city_null(actual=data1[7]['result']),expected)
        function.insert_img(self.driver,data1[7]['screenshot_name'])

    def test_personal_profile6(self,expected=True):
        """未选择区，提示请选择"""
        self.place_verify3()
        po = personal(self.driver)
        self.assert_equal(po.area_null(actual=data1[8]['result']),expected)
        function.insert_img(self.driver,data1[8]['screenshot_name'])

    def test_personal_profile7(self,expected=True):
        """个人资料更新成功"""
        self.all_verify()
        po = personal(self.driver)
        self.assert_equal(po.modify_successful(actual=data1[9]['result']), expected)
        function.insert_img(self.driver, data1[9]['screenshot_name'])

    def test_personal_profile8(self,expected=True):
        """取消修改个人昵称"""
        po = personal(self.driver)
        po.open_again()
        po.modify_nickname()
        self.assert_equal(po.cancle_nickname(actual=data1[10]['result']),expected)
        function.insert_img(self.driver, data1[10]['screenshot_name'])

    def test_personal_profile9(self,expected=True):
        """成功跳转至修改手机号"""
        po = personal(self.driver)
        po.open_again()
        po.modify_phone()
        self.assert_equal(po.enter_modifyphone(actual=data1[11]['result']),expected)
        function.insert_img(self.driver, data1[11]['screenshot_name'])

    def test_personal_profileA(self,expected=True):
        """预览名片信息"""
        po = personal(self.driver)
        po.open_again()
        po.preview_card()
        self.assert_equal(po.card_nickname(actual=data1[12]['result']), expected)
        function.insert_img(self.driver, data1[12]['screenshot_name'])

    def test_personal_profileB(self,expected=True):
        """关闭预览名片窗口"""
        po = personal(self.driver)
        po.open_again()
        po.preview_card()
        po.close_card()
        self.assert_equal(po.clocard_success(actual=data1[13]['result']), expected)
        function.insert_img(self.driver, data1[13]['screenshot_name'])

if __name__ == "__main__":
    unittest.main()



