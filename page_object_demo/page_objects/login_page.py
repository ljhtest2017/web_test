# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LoginPage
   Description :
   Author :       jz
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""
__author__ = 'jz'

class LoginPage:
    # 用户名输入框
    login_username_xpath = "//*[@name='phone']"
    # 密码输入框
    login_passwd_xpath = "//*[@name='password']"
    # 登录按钮
    login_button_xpath = "//button"

    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)

    def login(self, username, passwd):
        # 找到登录用户名
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.login_passwd_xpath).send_keys(passwd)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def get_current_url(self):
        pass

    def get_wrongMsg_from_noUserPaswd(self):
        pass
    