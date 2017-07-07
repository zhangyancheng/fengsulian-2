import os
from time import sleep
from public.base import Page
from test_case.page_obj.login_enter import Log_on
from config import globalparam
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "a2_sta")

class personal(Log_on,Page):
    """
    个人中心的个人资料页面
    """
    url = "/user/info"
    #定位器
    personal_name_loc = ("id", "name")
    personal_sex_loc = ("css selector", "input[value = '女']")
    personal_email_loc = ("id", "email")
    personal_place1_loc = ("xpath", "//form/div/div/div[5]/div/span[1]/input[1]")
    personal_place11_loc = ("xpath", "//form/div/div/div[5]/div/span[1]/ul/li[1]")
    personal_place2_loc = ("xpath", "//form/div/div/div[5]/div/span[2]/input[1]")
    personal_place22_loc = ("xpath", "//form/div/div/div[5]/div/span[2]/ul/li[1]")
    personal_place3_loc = ("xpath", "//form/div/div/div[5]/div/span[3]/input[1]")
    personal_place33_loc = ("xpath", "//form/div/div/div[5]/div/span[3]/ul/li[1]")
    personal_address_loc = ("css selector", "input[name = 'address']")
    personal_edit_loc = ("css selector", "span[class = 'edit_pic cropper']")
    personal_select_loc = ("css selector", "label[class = 'btn_select_file']")
    personal_confirm1_loc = ("css selector", "div[class = 'submit btn_com btn_blue cropper_upload w140']")
    personal_confirm2_loc = ("css selector", "input[class = 'per_sure btn_submit']")
    modify_nickname1_loc = ("class name", "sc_nick")
    button_cancel_loc = ("id", "ss_cancel")
    modify_phone_loc = ("class name", "alter_mobile")
    preview_card_loc = ("xpath", "html/body/div[3]/div/div/div/span")
    close_card_loc = ("xpath", "html/body/div[5]/div/a")

    #action
    def personal_name(self,name):
        """输入姓名"""
        self.clear_type(self.personal_name_loc,name)
    def personal_email(self,email):
        """输入地址"""
        self.clear_type(self.personal_email_loc,email)
    def personal_data(self,address):
        """选择性别、输入邮箱"""
        self.click(self.personal_sex_loc)
        self.clear_type(self.personal_address_loc,address)
    def personal_place1(self):
        """选择省"""
        self.click(self.personal_place1_loc)
        self.click(self.personal_place11_loc)
    def personal_place2(self):
        """选择市"""
        self.click(self.personal_place2_loc)
        self.click(self.personal_place22_loc)
    def personal_place3(self):
        """选择区"""
        self.click(self.personal_place3_loc)
        self.click(self.personal_place33_loc)
    def personal_picture(self):
        """上传头像"""
        self.click(self.personal_edit_loc)
        sleep(1)
        self.click(self.personal_select_loc)
        os.system(globalparam.auto_path + "./" + "head_sculpture.exe")
        self.click(self.personal_confirm1_loc)
    def personal_confirm(self):
        """确认修改"""
        self.click(self.personal_confirm2_loc)
    def  modify_nickname(self):
        """修改昵称"""
        self.click(self.modify_nickname1_loc)
        self.click(self.button_cancel_loc)
    def modify_phone(self):
        """修改手机号"""
        self.click(self.modify_phone_loc)
    def preview_card(self):
        """预览名片"""
        self.click(self.preview_card_loc)
        sleep(1)
    def close_card(self):
        """关闭预览名片"""
        self.click(self.close_card_loc)
    def open_again(self):
        self.open()


    #修改资料入口
    def personal_alter1(self,name = data1[0]['name'],email = data1[0]['email'],address = data1[0]['address']):
        """修改资料入口1"""
        self.open()
        self.login_entry()
        self.personal_name(name)
        self.personal_email(email)
        self.personal_data(address)
        # self.personal_picture()
        # sleep(1)
        self.personal_confirm()
    def personal_alter2(self, name=data1[1]['name'], email=data1[1]['email'],address=data1[1]['address']):
        """修改资料入口2"""
        self.open()
        self.personal_name(name)
        self.personal_email(email)
        self.personal_data(address)
        # self.personal_picture()
        # sleep(1)
        self.personal_confirm()
    def personal_alter3(self):
        """选择省入口3"""
        self.open()
        self.personal_place1()
        self.personal_confirm()
    def personal_alter4(self):
        """选择市入口4"""
        self.open()
        self.personal_place2()
        self.personal_confirm()
    def personal_alter5(self):
        """选择区入口5"""
        self.open()
        self.personal_place3()
        self.personal_confirm()
    def personal_alter6(self, name=data1[2]['name'], email=data1[2]['email'], address=data1[2]['address']):
        """修改资料入口6"""
        self.open()
        self.personal_name(name)
        self.personal_email(email)
        self.personal_data(address)
        self.personal_picture()
        # sleep(3)
        self.personal_confirm()

    #定位器
    modify_name_loc = ("xpath", "//div[3]/div/div/form/div/div/div[1]/span")
    modify_email_loc = ("xpath", "//div[3]/div/div/form/div/div/div[4]/span")
    modify_successful_loc = ("css selector", "html body div.dialog_pop div.dialog_box div.dialog_main div.dialog_main.dialog_alert")
    cancle_nickname_loc = ("xpath", "html/body/div[2]/div/div/div[2]/p[1]/span[2]")
    enter_modifyphone_loc = ("xpath", "html/body/div[3]/div/div/div[1]/h6")
    card_nickname_loc = ("xpath", "html/body/div[5]/div/div/div/div[2]")
    card_place_loc = ("xpath", "html/body/div[5]/div/div/div/div[4]/a[1]")
    clocard_success_loc = ("xpath", "html/body/div[3]/div/div/div/h6")
    #action
    def province_null(self,actual):
        """请选择省"""
        return self.is_text_in_value(self.personal_place1_loc,actual)
    def city_null(self,actual):
        """请选择市"""
        return self.is_text_in_value(self.personal_place2_loc,actual)
    def area_null(self,actual):
        """请选择区"""
        return self.is_text_in_value(self.personal_place3_loc,actual)
    def modify_successful(self,actual):
        """修改成功"""
        return self.is_text_in_element(self.modify_successful_loc,actual)
    def modify_name(self,actual):
        """姓名输入1或11个文字"""
        return self.is_text_in_element(self.modify_name_loc,actual)
    def modify_email(self,actual):
        """输入错误的邮箱"""
        return self.is_text_in_element(self.modify_email_loc,actual)
    def cancle_nickname(self,actual):
        """取消修改昵称"""
        return self.is_text_in_element(self.cancle_nickname_loc,actual)
    def enter_modifyphone(self,actual):
        """进入更改手机号页面"""
        return self.is_text_in_element(self.enter_modifyphone_loc,actual)
    def card_nickname(self,actual):
        """预览名片昵称"""
        return self.is_text_in_element(self.card_nickname_loc,actual)
    # def card_place(self,actual):
    #     """预览名片位置"""
    #     return self.get_text(self.card_place_loc)
    def clocard_success(self,actual):
        """关闭名片预览窗口"""
        return self.is_text_in_element(self.clocard_success_loc,actual)
