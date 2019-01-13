# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_demo
   Description :
   Author :       jz
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""
__author__ = 'jz'
import pytest


@pytest.mark.usefixtures('init_driver')
class TestDemo(object):
    def test_ttttt(self, init_driver):  # 函数名作为参数入参
        # 函数名代表了fixture的返回值，即driver
        init_driver.find_element_by_id('kw').send_keys('selenium')
    @pytest.mark.smoke
    def test_first(self):
        print "first test case"