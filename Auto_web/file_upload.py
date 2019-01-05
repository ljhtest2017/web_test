#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'liujiahai'
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://sahitest.com/demo/php/fileUpload.htm')
# upload = driver.find_element_by_id('file')
# upload.send_keys('d:\\baidu.py')  # send_keys
# print(upload.get_attribute('value'))  # check value
#
# driver.quit()
# autoIT，借助外力，我们去调用其生成的au3或exe文件。
# Python pywin32库+spy++，识别对话框句柄，进而操作
# SendKeys库
# keybd_event，跟3类似，不过是模拟按键，ctrl+a，ctrl+c， ctrl+v…

# 非input
from selenium import webdriver
import win32con
import win32gui
import time

dr = webdriver.Chrome()
dr.get('file:///F:/liujiahai/GitHub/web_test/data/upload.html')
upload = dr.find_element_by_id('file')
upload.click()
time.sleep(1)

# win32gui
#一级窗口
dialog = win32gui.FindWindow('#32770',u'打开')  # 对话框
#二级窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
#三级窗口
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
# Edit输入框
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

# 往输入框输入输入绝对路径
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'F:\\ac.xlsx')
# 按button
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

print(upload.get_attribute('value'))
dr.quit()