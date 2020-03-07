# coding=utf-8
import os
import time
from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
import sys
chrome_driver = "D:\work\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('http://www.5itest.cn/register')  # 进入百度首页
time.sleep(5)
# 验证某个元素是否存在
# print(EC.title_contains("注册"))
# 判断邮箱地址是否存在，存在就进行操作
# locator=(By.CLASS_NAME,"controls")
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
# email = driver.find_element_by_id("register_email")
# # 将List转成String
# user_name = ''.join(random.sample("123456abcdefghi", 5))
# email.send_keys(user_name)
# time.sleep(5)
driver.save_screenshot("D:\work\Selenium_Python\Screan.png")
code_element = driver.find_element_by_id("getcode_num")
# 坐标的起始点
left = code_element.location['x']
# 坐标的顶点
top = code_element.location['y']
#坐标的最右边零点
right = code_element.size['width'] + left
#左边的右上角
height = code_element.size['height'] + top
image=Image.open("D:\work\Selenium_Python\Screan.png")
im=image.crop((left,top,right,height))
im.save("D:\work\Selenium_Python\Screan1.png")

# def identifyingCode(startx, starty, endx, endy):
#     # driver.get_screenshot_as_file(os.getcwd() + '\\cirsschan.png')
#     imGetScreen = Image.open(os.getcwd() + '\\Screan.png')
#     box = (startx, starty, endx, endy)
#     imIndentigy = imGetScreen.crop(box)
#     imIndentigy.save(os.getcwd() + '\\indent.png')
#     sys.path.append("D:\software\tesseract")
#     strCommand = 'tesseract.exe ' + os.getcwd() + '\\indent.png ' + os.getcwd() + '\\1indet.txt'
#     print(''.join(strCommand))
#     os.system(strCommand)
#     rfindet = open(os.getcwd() + '\\1indet.txt', 'r')
#     strIndet = rfindet.readline()
#     return strIndet
# identifyingCode(left,top,right,height)
driver.close()
#
# if EC.visibility_of_element_located(  driver.find_element_by_id("register_email")):
#     driver.find_element_by_id("register_email").send_keys("123@1.com")
#     user_name = driver.find_elements_by_class_name("controls")[1]
#     user_name_node = user_name.find_element_by_class_name("form-control")
#     user_name_node.send_keys("123")
# else:
#     print("元素不存在")

