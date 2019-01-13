# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fixture_demo
   Description :
   Author :       jz
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""
__author__ = 'jz'
#
# import pytest
# from selenium import webdriver
#
# @pytest.fixture()  # 默认scope为function
# def my_fixture()
#
#     driver = webdriver.Chrome()
#
#     yield driver  # 将driver作为返回值，在测试用例中需要使用driver
#
#     driver.close()  # 测试用例执行完成之后，要执行的清理操作、
#     driver.quit()  # 测试用例执行完成之后，要执行的清理操作
#
#
# @pytest.fixture(scope="class")
# def test_class()
#     print u"我是class级别的fixture！！"
#
#
# @pytest.fixture(scope="session")
# def hello():
#     print u"我是session级别fixture！！！！"
#
# # 调用fixture
# # 测试用例、测试类中调用fixtrue的三种方式
# # 1 在测试用例中直接调用它
# # 将fixture的函数名字作为测试用例的参数
# # 如果fixture有返回值，那么测试用例中的fixture函数名字就接受返回值
#
# import unittest
# import pytest
# from selenium import webdriver
#
# class TestDemo(unittest.TestCase):
#
#     @pytest.fixture
#     def init_driver(self):
#         driver = webdriver.Chrome()
#         driver.get("http://www.baidu.com")
#         yield driver
#         driver.quit()
#
#     def test_ttt(self, init_driver):  # fixture函数名作为参数传入
#         init_driver.driver_element_by_xpath("//input[@id='kw']").send_keys('selenium') # 函数名代表了fixtrue的返回值，即driver
#
#     """
#     2 用fixture装饰其调用fixture：
#         在测试用例、测试类前面加上@pytest.mark.usefixtures("fixture函数名字")
#         ps:定义conftest.py，在此文件中可定义多个fixture.pytest会自动搜索词文件
#         示例代码
#     """
#     @pytest.mark.usefixtures('ini_driver')
#     def test_tttttt(self, init_driver):
#         init_driver.find_element_by_xpath("XXX") # 函数名代表了fixture的返回值，即driver
#
#     """
#     3 用autos调用fixture-不推荐使用
#     """
#
"""
6.4.1 conftest.py
    定义公共的fixture，多个测试类中可以调用
    pytest提供了conftest.py文件，可以叫fixture定义在此文件中
    运行测试用例时，不需要去导入这个文件，会自动去查找conftest.py文件，然后找到对应的fixture
    示例代码:
"""
