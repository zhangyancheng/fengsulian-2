from public.datainfo import ExcelUtil
from config import globalparam

class Test1():
    """获取excel数据"""
    def a1_data(self,sheet):
        """a1_login_sta's values"""
        filepath = globalparam.data_path + "./" + "datas.xlsx"
        sheetName = sheet
        data = ExcelUtil(filepath, sheetName)
        data1 = data.dict_data()
        return data1

# filepath = "F:\\selenium-git\\data\\testdata\\a1-a9.xlsx"
# sheetName = "a1_sta"
# data = ExcelUtil(filepath, sheetName)
# data1 = data.dict_data()
# print(data1[2]['username'])