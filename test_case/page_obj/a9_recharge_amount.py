from public.base import Page
from .login_enter import Log_on
from data.testdata.data_read import Test1
data1 = Test1().a1_data(sheet="a9_sta")

class recharge(Log_on,Page):
    """
    充值余额
    """
    url = "/user/fund/recharge"

    #定位器
    write_amount_loc = "id", "money"
    #点击"充值金额"
    click_topup_loc = ("xpath", "//form/div[2]/label/span")
    click_recharge_loc = ("css selector", "input[class = 'btn_com btn_blue btn_submit']")
    select_alipay_loc = ("css selector", "div[class = 'pay_style']")
    click_pay_loc = ("id", "mm_pay")
    customer_service_loc = ("xpath", "//div[2]/div/div[2]/div[2]/a[1]")
    #action
    def write_aomunt(self,money):
        """输入金额"""
        self.clear_type(self.write_amount_loc,money)
    def click_topup(self):
        """点击'充值金额'"""
        self.click(self.click_topup_loc)
    def click_recharge(self):
        """点击立即充值"""
        self.click(self.click_recharge_loc)
    def select_alipay(self):
        """选择支付宝"""
        self.click(self.select_alipay_loc)
    def click_pay(self):
        """点击支付"""
        self.click(self.click_pay_loc)
    def customer_service(self):
        """点击联系客服"""
        self.click(self.customer_service_loc)

    """充值入口"""
    def money1(self,money = data1[0]['money']):
        """入口1"""
        self.open()
        self.login_entry()
        self.write_aomunt(money)
        self.click_topup()
    def money2(self,money = data1[0]['money']):
        """入口2"""
        self.open()
        self.write_aomunt(money)
        self.click_recharge()

    #定位器
    write_null_loc = ("xpath", "//form/div[2]/span[1]")
    pay_fail_loc = ("xpath", "//div[2]/div/div[2]/div[1]/h2")
    input_amount_loc = ("xpath", "//div[2]/div[1]/div[2]/h2/span")
    skip_paypage_loc = ("css selector", "strong[class = ' amount-font-22 ']")
    skip_service_loc = ("xpath", "//div[2]/div[1]/h1")
    #action
    def write_null(self,actual):
        return self.is_text_in_element(self.write_null_loc,actual)
    def pay_fail(self,actual):
        return self.is_text_in_element(self.pay_fail_loc,actual)
    def input_amount(self,actual):
        return self.is_text_in_element(self.input_amount_loc,actual)
    def skip_paypage(self,actual):
        return self.is_text_in_element(self.skip_paypage_loc,actual)
    def skip_service(self,actual):
        return self.is_text_in_element(self.skip_service_loc,actual)

