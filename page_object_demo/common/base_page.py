# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_page
   Description :
   Author :       jz
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""
__author__ = 'jz'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
import dir_config
import logger
import logging
import os
import random


class BasePage(object):

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()


    # 等待元素可见
    def wait_eleVisible(self, locator, by=By.XPATH, wait_times=40, poll_frequency=1):
        if by not in By.__dict__.values():
            logging.error(u"定位类型[{0}]不在支持类型内，请修改定位类型。".format(by))
            raise InvalidSelectorException

        # 开始时间
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times,poll_frequency).until(EC.visibility_of_element_located((by, locator)))
            t2 = time.time()
            # 结束时间-两者之差就是真正等待时间
            logging.info("等待结束，等待开始时间：{0}， 结束等待时间：{1}， 等待时长为：{2}".format(t1, t2, t2-t1))
        except TimeoutException as e:
            logging.exception(u"等待元素超时，截取当前页面。")
            self.save_screenshot()
            # 抛出异常
            raise e
        except InvalidSelectorException as e:
            logging.exception("元素定位表达式：{0} 不正确，请修正".format(locator))

    # 等待元素存在
    def wait_eleExists(self, locator, by=By.XPATH, wait_times=40):
        if by not in By.__dict__.values():
            logging.error(u"定位类型[{0}]不在支持类型内，请修改定位类型。".format(by))
            raise InvalidSelectorException

        # 开始时间
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times).until(
                EC.presence_of_element_located((by, locator)))
            t2 = time.time()
            # 结束时间-两者之差就是真正等待时间
            logging.info("等待结束，等待开始时间：{0}， 结束等待时间：{1}， 等待时长为：{2}".format(t1, t2, t2 - t1))
        except TimeoutException as e:
            logging.exception(u"等待元素超时，截取当前页面。")
            self.save_screenshot()
            # 抛出异常
            raise e
        except InvalidSelectorException as e:
            logging.exception("元素定位表达式：{0} 不正确，请修正".format(locator))

    # 查找元素 -- 一个元素
    def find_element(self, locator, by=By.XPATH, wait_times=40, type="visible"):
        """

        :param locator: 元素定位表达式
        :param by: 元素定位类型，比如id,xpath,name等
        :param wait_times: 等待元素出现或者存在的时长。默认为40s
        :param type: 等待的条件类型。是可见还是元素存在。默认是visible，目前只考虑可见和存在两者情况
        :return: 返回WebElement元素对象
        """

        logging.info("当前元素定位类型：{0}， 当前查找的元素表达式为：{1}".format(by, locator))
        if type == "visible":
            logging.info("开始等待元素在当前页面可见")
            self.wait_eleVisible(locator, by, wait_times)
        else:
            logging.info("开始等待元素在当前页面存在")
            self.wait_eleExists()

        try:
            ele = self.driver.find_element(by, locator)
            return ele
        except NoSuchElementException as e:
            logging.exception("元素查找失败，找不到该元素。开始截取当前页面图像")
            self.save_screenshot()
            raise e

    # 截图函数
    def save_screenshot(self):
        # 随机数字字符串
        r = ""
        for index in xrange(3):
            r += str(random.randint(1000,10000))

        # 截屏
        file_path = os.path.join(screenshot_dir, "{0}.png".format(time.strftime("%Y%m%d_%H%M%S_{0}".format(r))))
        self.driver.save_screenshot(file_path)
        logging.info("已截取当前页，文件路径：{0}".format(file_path))
    # 处理alert弹出框
    def alert_handler(self, action="accept"):
        # 等待alert出现
        WebDriverWait(self.driver, 10, 1).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert
        message = alert.text
        if action == "accept":
            alert.accept()
        else:
            alert.dismiss()
        return message