# -*- coding:utf-8 -*-

"""
5.10 下拉框操作
    观察下拉框元素是select/option还是ul/li
    1 菜单栏-点击其中的 某个连接跳转。
    2 在下拉列表中选择一个值

    思路：
        1 等待下拉列表和下拉列表中值得存在
        2 对下拉列表中的元素进行操作
    三种方式
        一 获取所有的下拉列表值，然后用循去匹配相同的值
        二 通过text的内容来找到下拉列表的某个值
        三 如果是select/option组合，则可以使用Select类来处理
    示例：
        百度高级搜索

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
locator = "//div[@id='u1']/a[text()='设置']"
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
driver.find_element_by_xpath(locator).click()

locator2 = '//a[text()="高级搜索"]'
# 等待元素可见
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator2)))
driver.find_element_by_xpath(locator2).click()


# Select类使用
# 1、实例化类。参数为Select对象
locator3 = "//select[@name='ft']"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator3)))

select = Select(driver.find_element_by_xpath(locator3))
sleep(1)
# 2 根据下标来选择
select.select_by_index(1)
sleep(1)
# 3、根据option的value属性值来选择
select.select_by_value('xls')
sleep(1)
# 4、根据文本内容来选择
select.select_by_visible_text('所有格式')
sleep(3)

driver.quit()
