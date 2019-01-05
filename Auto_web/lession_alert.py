#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'liujiahai'
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("file:///F:/liujiahai/GitHub/web_test/data/alert.html")
# 触发一个alert弹框
driver.find_element_by_id("bb").click()
# 等待弹出框出现
WebDriverWait(driver, 5).until(EC.alert_is_present())
# 先切换到alert Alert类实例化对象
alert = driver.switch_to.alert
# 2 操作alert
# accept  表示ok  dismiss  表示no
print(alert.text)
alert.accept()
