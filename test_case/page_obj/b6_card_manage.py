from public.base import Page
from test_case.page_obj.login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "b6_sta")

class card_manage(Log_on,Page):
    """
    企业名片管理操作
    """
    url = "/user/cards"

    #定位器
    view_collectcard_loc = ("css selector", "a[class='see_card']")
    click_delete_loc = ("css selector", "div[class='del_btn']>i")
    click_cancel_loc = ("css selector", "div[class='cancel btn_com btn_red ml30']")
    click_confirm_loc = ("css selector", "div[class='submit btn_com btn_blue']")
    #action
    def view_collectcard(self):
        """查看收藏企业名片"""
        self.click(self.view_collectcard_loc)
    def click_delete(self):
        """点击删除名片"""
        self.click(self.click_delete_loc)
    def click_cancel(self):
        """点击取消删除"""
        self.click(self.click_cancel_loc)
    def click_confrim(self):
        """点击确认删除"""
        self.click(self.click_confirm_loc)
    def next_open(self):
        self.open()

    def card_manage1(self):
        """入口1"""
        self.next_open()
        self.login_entry()

    #定位器
    collectcard_success_loc = ("css selector", "p[class='p_text']")
    view_card_loc = ("css selector", "div[class='title cardName_ajax']")
    delete_box_loc = ("css selector", "div[class='dialog_main dialog_alert']")
    cancel_delete_loc = ("css selector", "p[class='p_text']")
    confirm_delete_loc = ("css selector", "a[class='ss_nearcom']")
    #action
    def collectcard_success(self, actual):
        """企业名片收藏成功"""
        return self.is_text_in_element(self.collectcard_success_loc, actual)
    def view_card(self, actual):
        """查看企业名片"""
        return self.is_text_in_element(self.view_card_loc, actual)
    def delete_box(self, actual):
        """点击删除名片"""
        return self.is_text_in_element(self.delete_box_loc, actual)
    def cancel_delete(self, actual):
        """取消删除名片"""
        return self.is_text_in_element(self.cancel_delete_loc, actual)
    def confirm_delete(self, actual):
        """删除名片成功"""
        return self.is_text_in_element(self.confirm_delete_loc, actual)