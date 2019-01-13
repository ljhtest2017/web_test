# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     conftest.py
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
from selenium import webdriver


@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    yield driver
    driver.quit()

