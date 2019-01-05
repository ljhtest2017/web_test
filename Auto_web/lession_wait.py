#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'liujiahai'
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//div[@id='u1']//a[text()='登录']").click()
# 隐性等待 = 等待弹出框的元素
# id=TANGRAM__PSP_10__footerULoginBtn
locator = 'TANGRAM__PSP_10__footerULoginBtn'

# 等待元素可见
WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.ID, locator)))
# 操作元素
driver.find_element_by_id(locator).click()
# # 某一个元素存在
# WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, locator)))
# # 某一个元素可点击
# WebDriverWait(driver, 10, 1).until(EC.element_located_to_be_selected((By.ID, locator)))
driver.quit()


