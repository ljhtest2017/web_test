#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'liujiahai'

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 隐性等待
driver.implicitly_wait(10)

ele = driver.find_element_by_id("kw")
ele.send_keys(u"柠檬班")
driver.find_element_by_id("su").click()


# 因为click的操作带来了页面的变化  ====  一定要等待
driver.find_element_by_xpath('//a[contains(text(), "_腾讯课堂")]').click()