from time import sleep
from public.base import  Page
from test_case.page_obj.login_enter import  Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b3_sta")

class oprequire(Log_on,Page):
    """
    精准发布需求
    """
    url = "/user/demand"

    #定位器
    edit_demand_loc = ("xpath", "//div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/div[1]/div[2]/a")
    click_describe_loc = ("xpath", "//div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/div[2]/div[1]/a/p")
    continue_release_loc = ("xpath", "//div[2]/div[1]/div/div[2]/a")
    click_detail_loc = ("xpath", "//div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/div[2]/div[2]/span[5]/a")
    click_delete_loc = ("id", "demandListIcon2")
    cancel_delete_loc = ("xpath", "//div[4]/div/div[3]/div[2]")
    confirm_delete1_loc = ("xpath", "//div[4]/div/div[3]/div[1]")
    confirm_delete2_loc = ("xpath", "//div[4]/div/div[3]/div")
    #action
    def edit_demand(self):
        """编辑需求"""
        self.click(self.edit_demand_loc)
    def click_describe(self):
        """点击需求描述"""
        self.click(self.click_describe_loc)
    def continue_release(self):
        """点击继续发布"""
        self.click(self.continue_release_loc)
    def click_detail(self):
        """点击需求详情"""
        self.click(self.click_detail_loc)
    def click_delete(self):
        """点击删除按钮"""
        self.click(self.click_delete_loc)
    def cancel_delete(self):
        """取消删除"""
        self.click(self.cancel_delete_loc)
    def confirm_delete(self):
        """确认删除"""
        self.click(self.confirm_delete1_loc)
        # sleep(1)
        self.click(self.confirm_delete2_loc)
    def next_open(self):
        self.open()

    """无入口"""

    #定位器
    enter_edit_loc = ("xpath", "//form/div[2]/div[2]/div/div/div/input")
    enter_describe_loc = ("xpath", "//div[2]/div[1]/div/div[1]/div[1]/h6")
    enter_delete_loc = ("xpath", "//div[4]/div/div[2]/p")
    cancel_success_loc = ("xpath", "//div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/div[2]/div[1]/a/p")
    delete_success_loc = ("xpath", "//div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/div[2]/div[1]/a/p")
    #action
    def enter_edit(self,actual):
        """进行编辑/继续发布"""
        return self.is_text_in_value(self.enter_edit_loc,actual)
    def enter_describe(self,actual):
        """点击进入需求名称/需求详情"""
        return self.is_text_in_element(self.enter_describe_loc,actual)
    def enter_delete(self,actual):
        """点击删除弹出框"""
        return self.is_text_in_element(self.enter_delete_loc,actual)
    def cancel_success(self,actual):
        """点击取消成功"""
        return self.is_text_in_element(self.cancel_success_loc,actual)
    def delete_success(self,actual):
        """删除成功"""
        return self.is_text_in_element(self.delete_success_loc,actual)
