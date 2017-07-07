from time import sleep
from public.base import  Page
from test_case.page_obj.login_enter import  Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="b2_sta")

class release(Log_on,Page):
    """
    精准发布需求
    """
    url = "/demand/add/demand/type?demandType=5"

    #定位器
    select_category1_loc = ("xpath", "//form/div[1]/div[2]/div/div/div/div/input[1]")
    select_category2_loc = ("xpath", "//form/div[1]/div[2]/div/div/div/div/ul/li[2]")
    describe_demand_loc = ("xpath", "//form/div[2]/div[2]/div/div/div/input")
    specific_require_loc = ("xpath", "//form/div[3]/div[2]/div/div/div/textarea")
    cutoff_time1_loc = ("xpath", "//form/div[6]/div[2]/div/div/div/input")
    cutoff_time2_loc = ("xpath", "//div[4]/div[1]/div[2]/table/tbody/tr[5]/td[6]/div")
    click_time_loc = ("xpath", "//form/div[6]/div[1]/h1")
    addition_file_loc = ("xpath", "//form/div[7]/div[2]/div[1]/div/div/div/span/span[3]/span/span/span/div[2]/label")
    to_read_loc = ("id", "check_agree")
    confirm_read_loc = ("css selector", "div[class = 'submit btn_com btn_blue']")
    trade_agreement_loc = ("xpath", "//form/div[8]/a")
    submit_demand_loc = ("id", "demandSavesaa")
    save_draft_loc = ("id", "trif")
    #action
    def select_category(self):
        """选择行业类目"""
        self.click(self.select_category1_loc)
        self.click(self.select_category2_loc)
    def describe_demand(self,demand):
        """一句话描述需求"""
        self.clear_type(self.describe_demand_loc,demand)
    def specific_require(self,require):
        """填写具体要求"""
        self.clear_type(self.specific_require_loc,require)
    def cutoff_time(self):
        """选择报名截止时间"""
        self.click(self.cutoff_time1_loc)
        sleep(1)
        self.click(self.cutoff_time2_loc)
        self.click(self.click_time_loc)
    def click_agree(self):
        """点击已阅读并同意"""
        self.click(self.to_read_loc)
    def confrim_read(self):
        """点击阅读弹框"""
        self.click(self.confirm_read_loc)
    def trade_agreement(self):
        """进入风速链交易协议"""
        self.click(self.trade_agreement_loc)
        self.into_new_window()
    def submit_comand(self):
        """点击提交需求"""
        self.click(self.submit_demand_loc)
    def save_draft(self):
        """点击保存草稿"""
        self.click(self.save_draft_loc)

    def submit_demand1(self,demand = data1[0]['demand'], require = data1[0]['require']):
        """提交需求入口1(验证不同意)"""
        self.open()
        self.login_entry()
        self.select_category()
        self.describe_demand(demand)
        self.specific_require(require)
        self.cutoff_time()
        self.click_agree()
        self.submit_comand()
    def submit_demand2(self,demand = data1[0]['demand'], require = data1[0]['require']):
        """提交需求入口2"""
        self.open()
        self.describe_demand(demand)
        self.specific_require(require)
    def submit_demand3(self,demand = data1[0]['demand'], require = data1[0]['require']):
        """提交需求入口2"""
        self.open()
        self.select_category()
        self.describe_demand(demand)
        self.specific_require(require)

    #定位器
    not_agree_loc = ("xpath", "//div[5]/div/div[2]/div")
    category_null_loc = ("xpath", "//form/div[1]/div[2]/div/div/div/div/span[1]")
    demand_error_loc = ("xpath", "//form/div[2]/div[2]/div/div/div/span[1]")
    require_error_loc = ("xpath", "//form/div[3]/div[2]/div/div/div/span[1]")
    time_null_loc = ("xpath", "//form/div[6]/div[2]/div/div/div/span[1]")
    enter_agreement_loc = ("xpath", "//div[2]/div[1]/h1")
    draft_success_loc = ("xpath", "//div[2]/div[1]/div[2]/div/div/div[3]/ul/li[2]/div[2]/div[1]/a/p")
    #action
    def not_agree(self,actual):
        return self.is_text_in_element(self.not_agree_loc,actual)
    def category_null(self,actual):
        return self.is_text_in_element(self.category_null_loc,actual)
    def demand_error(self,actual):
        return self.is_text_in_element(self.demand_error_loc,actual)
    def require_error(self,actual):
        return self.is_text_in_element(self.require_error_loc,actual)
    def time_null(self,actual):
        return self.is_text_in_element(self.time_null_loc,actual)
    def enter_agreement(self,actual):
        return self.is_text_in_element(self.enter_agreement_loc,actual)
    def draft_success(self,actual):
        return self.is_text_in_element(self.draft_success_loc,actual)
