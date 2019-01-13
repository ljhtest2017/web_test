# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_login
   Description :
   Author :       jz
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""
from page_object_demo.page_objects.index_page import IndexPage

import unittest
from page_object_demo.page_objects.login_page import LoginPage
from selenium import webdriver
from time import sleep
from  page_object_demo.test_datas.login_data import *

class Test_Login(unittest.TestCase):

    def setUp(self):
        url = "XXXXXXXXXXXXX"
        self.driver = webdriver.Chrome()
        self.lp = LoginPage(self.driver, url)

    def tearDown(self):
        self.driver.quit()

    # 用例一： 登录成功
    def test_1_login_success(self):
        # 步骤
        self.lp.login(login_success_dict["username"], login_success_dict["passwd"])

        # 结果比对
        sleep(3)
        ip = IndexPage(self.driver)
        self.assertEqual(ip.get_url(), login_success_dict["check_url"])
        self.assertEqual(ip.get_nickname(), login_success_dict["check_nickname"])

    # 用例二 没有用户名
    def test_2_login_noUsername(self):
        # 步骤
        self.lp.login(login_noUser_dict["username"], login_noUser_dict["passwd"])

        # 结果比对
        sleep(3)
        url = self.lp.get_current_url()
        wrong_msg = self.lp.get_wrongMsg_from_noUserPaswd()
        self.assertEqual(url, login_noUser_dict["check_url"])
        self.assertEqual(wrong_msg, login_noUser_dict["check_msg"])