# -*- coding:utf-8 -*-
"""
5.11 窗口切换
    步骤
        1 获取当前所有的窗口
        windows = driver.window_handles
        2 切换到指定的窗口
        chrome.switch_to.window(windows[-1]  # 最新打开的窗口
        3 切回原来的窗口
        chrome.swtich_to.window(windows[0]  #切换到第一个窗口
        4 获取当前窗口的句柄
        chrome.current_window_handle

    示例：百度搜索-柠檬班，选择第一条搜索结果。并切入新的窗口
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# 开启浏览器会话
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 百度首页，搜索Selenium
driver.find_element_by_id("kw").send_keys(u"柠檬班")
driver.find_element_by_id("su").click()
# 获取当前浏览器打开的窗口数
handles = driver.window_handles
print handles
print len(handles)
# 定位selenium官网网站，并点击链接
selenium_officer_xpath = '//div[@id="3"]/h3/a'
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, selenium_officer_xpath)))
driver.find_element_by_xpath(selenium_officer_xpath).click()
# 等待新的窗口出现
WebDriverWait(driver, 30, 1).until(EC.new_window_is_opened(handles))
# 获取到新的窗口， 再切换到新的窗口，进行新页面的操作
handles = driver.window_handles
print len(handles)
print handles
driver.switch_to.window(handles[-1])
handle = driver.current_window_handle
print handle

driver.quit()