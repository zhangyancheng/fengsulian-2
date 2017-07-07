from public.base import Page
from test_case.page_obj.login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet = "b5_sta")

class card_collection(Log_on,Page):
    """
    收藏公司名片
    """
    url = "/user/cards"

    #定位器
    view_enterprise_loc = ("css selector", "a[class='ss_nearcom']")
    view_card_loc = ("css selector", "div[class='wf_content_list_view fr']>a")
    click_collect_loc = ("css selector", "i[class='fa fa-heart-o']")
    #action
    def view_enterprise(self):
        """点击查看企业"""
        self.click(self.view_enterprise_loc)
    def view_card(self):
        """点击查看名片"""
        self.click(self.view_card_loc)
    def click_collect(self):
        """点击收藏"""
        self.click(self.click_collect_loc)
    def next_open(self):
        self.open()

    def enter_card1(self):
        """入口1"""
        self. next_open()
        self.login_entry()

    #定位器
    enter_cardmanage_loc = ("css selector", "a[class='per_active']")
    viewenter_success_loc = ("css selector", "a[href='/enterprise/1549']>h2")
    viewcard_success_loc = ("css selector", "div[class='title cardName_ajax']")
    collect_success_loc = ("css selector", "span[class='collect']")
    #action
    def enter_cardmanage(self, actual):
        return self.is_text_in_element(self.enter_cardmanage_loc, actual)
    def viewenter_success(self, actual):
        return self.is_text_in_element(self.viewenter_success_loc, actual)
    def viewcard_success(self, actual):
        return self.is_text_in_element(self.viewcard_success_loc, actual)
    def collect_success(self, actual):
        return self.is_text_in_element(self.collect_success_loc, actual)
