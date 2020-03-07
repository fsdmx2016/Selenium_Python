# coding=utf-8
from selenium import webdriver
import time
import random

chrome_driver = "D:\work\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)


def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)


def getElement(id):
    element = driver.find_element_by_id(id)
    return element


def get_range_user():
    user_info = ''.join(random.sample("123456abcdefghi", 5))
    return user_info
