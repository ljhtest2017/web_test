#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'liujiahai'
from selenium import webdriver
from time import sleep
# 启动一个与浏览器之间的会话
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 访问一个网址
driver.get("http://www.baidu.com")
# 访问一个网址
driver.get("http://www.taobao.com")
# 休眠
sleep(2)
# 上一个页面
driver.back()
# 休眠
sleep(2)
# 下一个页面
driver.forward()
# 休眠
sleep(2)
# 刷新页面
driver.refresh()
# 休眠
sleep(2)
# 关闭浏览器会话
# 设置窗口大小
driver.set_window_size(200, 300)
# 回去当前页URL
current_url = driver.current_url
print(current_url)
# 当前窗口的标题
title = driver.title
print(title)
# 获取当前窗口的句柄
print(driver.current_window_handle)




sleep(2)
driver.quit()