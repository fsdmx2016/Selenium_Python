# coding=utf-8
import time

from selenium import webdriver

from Util.find_element import findElement


class ActionMethod:
    def __init__(self):
        chrome_driver = "D:\work\chromedriver.exe"
        self.base_driver = webdriver.Chrome(executable_path=chrome_driver)
        self.findelement = findElement(self.base_driver)
        self.base_driver.get('http://www.5itest.cn/login?goto=http%3A//www.5itest.cn/')
    def open_browser(self):
        chrome_driver = "D:\work\chromedriver.exe"
        self.base_driver = webdriver.Chrome(executable_path=chrome_driver)

    def get_element(self, *args):
        element = self.findelement.get_element(*args)
        return element

    def input(self, *args):
        '''
        输入值
        '''
        # key,value

        element = self.findelement.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.clear()
        element.send_keys(args[1])

    def on_click(self, *args):
        '''
        元素点击
        '''
        element = self.findelement.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.click()

    def sleep_time(self, *args):
        time.sleep(int(args[0]))

    #
    # # 获取屏幕的宽高
    # def get_size(self, *args):
    #     size = self.driver.get_window_size()
    #     width = size['width']
    #     height = size['height']
    #     return width, height
    #
    # # 向左边滑动
    # def swipe_left(self, *args):
    #     # [100,200]
    #     x1 = self.get_size()[0] / 10 * 9
    #     y1 = self.get_size()[1] / 2
    #     x = self.get_size()[0] / 10
    #     self.driver.swipe(x1, y1, x, y1, 2000)
    #
    # # 向右边滑动
    # def swipe_right(self, *args):
    #     # [100,200]
    #     x1 = self.get_size()[0] / 10
    #     y1 = self.get_size()[1] / 2
    #     x = self.get_size()[0] / 10 * 9
    #     self.driver.swipe(x1, y1, x, y1, 2000)
    #
    # # 向上滑动
    # def swipe_up(self, *args):
    #     # [100,200]direction
    #     x1 = self.get_size()[0] / 2
    #     y1 = self.get_size()[1] / 10 * 6
    #     y = self.get_size()[1] / 10 * 2
    #     self.driver.swipe(x1, y1, x1, y, 1000)
    #
    # # 向下滑动
    # def swipe_down(self, *args):
    #     # [100,200]
    #     x1 = self.get_size()[0] / 2
    #     y1 = self.get_size()[1] / 10
    #     y = self.get_size()[1] / 10 * 9
    #     self.driver.swipe(x1, y1, x1, y)
