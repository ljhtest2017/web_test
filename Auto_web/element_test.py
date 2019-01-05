#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'liujiahai'
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 元素定位方式
# # 1 id 动态id不能通过id定位
# element = driver.find_element_by_id("kw")
# print(element.tag_name)
# # 2 name name元素并不绝对唯一，如果有多个元素的name值一样，那么直接取第一个
# driver.find_element_by_name('wd')
# # 查找匹配表达式的所有元素
# driver.find_element_by_name('wd')
#
# # 3 class_name class 属性——多个class时，只能取其中一个class值，如class=“bg s_ipt_wr quickdelete-wrap”取bg或s_ipt_wr或quickdelete-wrap
# driver.find_element_by_class_name('s_ipt')
# # 4 tag_name  tag属性 元素的标签名
# driver.find_element_by_tag_name('input')
# # 针对a元素——通过链接的文本内容来定位元素
# # 5 link_text 链接文本——完全匹配
# driver.find_element_by_link_text('新闻')
# # 6 partial_link_text 链接文本部分——部分匹配（包含）
# driver.find_element_by_partial_link_text('新')
#
# # 万能定位 xpath css_selector
# # 7 xapth   xpath
# driver.find_element_by_xpath('//*[@id="kw"]')
# # 8 css_selector  css选择器
# driver.find_element_by_css_selector(#kw)

# xpath
# 绝对路径  相对路径
# 1 相对定位：
    # 在这个页面当中，有没有这个元素，无关元素的位置和第几代
    # 以// 开头
    # //标签名[@属性名=属性值]  *星号表示所有标签名
    # 多个属性组合 支持逻辑运算符 and or eg. //input[@id="phone" and @class="abc"]
    # contains函数() contains(@属性，值）  //input[contains(@class, 'username')
    # text()函数  //div[test()="请输入正确的手机号"]
                # //div[contains(text(),"手机号")]
    # 使用轴定位表达式
    # 轴运算名称
    # acestor 祖父节点 包含父
    # parent 父节点
    # preceding 当前元素节点标签之前的所有节点。（html页面先后顺序）
    # preceding-sibling 当前元素节点标签之前的所有兄弟节点（同级）
    # following：当前元素节点标签之后的所有节点。（html页面先后顺序）
    # following-sibling 当前元素标签之后的所有兄弟（同级）
    # 使用语法：轴名称：：节点名称
    # xpath = '//div//table//td/preceding::td'
    # xpath = 'h2[text()="软件测试从零开始"/parent::div/preceding-sibli::div//img'
                

# 2 绝对定位
    # /html/input/input/input[1]
    # 以/开头


driver.quit()