# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from config import globalparam
import unittest
import time

test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir,pattern = "*sta.py")

if __name__ == "__main__":
#指定测试用例为当前文件夹下的mail目录
    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # 定义报告存放路径
    filename = globalparam.report_path + "\\" + now + "result.html"
    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况:")
    runner.run(discover )  # 运行测试用例
    fp.close()  # 关闭测试报告

