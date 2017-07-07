from selenium import webdriver
from config import globalparam
from public.base import Page

#截图函数
def insert_img(driver,file_name):
    file_path = globalparam.img_path + "\\" + file_name
    Page(driver).take_screenshot(file_path )

