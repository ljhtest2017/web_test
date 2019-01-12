# -*- coding:utf-8 -*-
"""
Js处理滚动条
    在页面当中，页面存在滚动条，而你要操作的元素在当前屏幕可见区域之外，那么要使用滚动条滚动到该元素处，然后操作他。
    selenium当中使用execute_script方法执行js语句来实现滚动功能
    语句：execute_script("arguments[0].scrollIntoView;",target)
    其中target为find_element_by_XX找到的元素对象
    所以滚动步骤是：
        1 通过selenium的查找元素的方法先找到元素
        2 通过执行js语句，将元素滚动到可见区域中
    示例代码：
        # 找到元素
        target = driver.find_element_by_xpath('//a[text()="我最可爱了"])
        # 将元素滚动到可见区域
        driver.execute_script("arguments[0].scrollIntoView();", target)

5.13 上传操作
有两种情况
    1 如果是input可以直接输入路径的，那么直接调用send_keys输入路径
    2 非input标签的上传，则需要借助第三方工具
        AutoIt 我们去调用其生成的au3或exe文件
        SendKeys第三方库， 目前只支持2.7
    3 python pywin32库，识别对话框句柄，并进行操作

使用pywin32库
工具：pywin32和WinSpy
    元素识别
    WinPy工具识别windows控件工具
    需要一层层往里面找到哟啊操作的文件输入框和打开按钮


5.14 js处理日历控件
    在web自动化过程中，我们会遇到日历控制这样的场景，大致分为两种
        1 可以直接输入日期
        2 不能直接输入日期，只能选择
    对于不能直接输入的日期控件，通过日历控件面板选择太繁琐了
    基本思路：
        利用js去掉readonly属性，然后直接输入时间
        示例： 12306的抢票页面，需要输入起始时间和结束时间

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 隐性等待一下
driver.implicitly_wait(30)
#
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_id("kw").send_keys(u"柠檬班")
# # 点击搜索按钮-显示搜索结果
# driver.find_element_by_id("su").click()
# # 等待元素存在
# ele_locator = '//a[text()="- CSDN博客"]'
# param = (By.XPATH, ele_locator)
# # 使用webdrivewait
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((param)))
#
# # 滚动操作1、找到这个元素
# ele = driver.find_element_by_xpath('//a[text()="用法详解 - 道高一尺 - 博客园"]')
# sleep(2)
# # 执行js语句，滚动页面
# driver.execute_script("arguments[0].scrollIntoView(false)", ele)


# js处理日志控件，12306 日期处理
driver.get("https://kyfw.12306.cn/otn/index/init")
# 去掉只读
js_pha = 'document.getElementById("train_date").readOnly = false;'
driver.execute_script(js_pha)

# 清除原来的内容并写入新的日期 -- 注意按照要求的日期格式
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2019-08-23")

# 直接通过js语句来修改日期
driver.execute_script('document.getElementById("train_date").value="2018-08-23";')
value = driver.find_element_by_id('train_date').get_attribute('value')
print value
