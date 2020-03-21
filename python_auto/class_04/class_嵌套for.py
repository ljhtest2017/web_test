#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 13:26
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_嵌套for.py
#
# # while for 可以互相嵌套
# d = {'name': {'bb':'bb', 'snow': '消息', 'ac': '刘家海'},
#      'score': [99, 100, 120]}
# # 字典里面嵌套了列表和字典
# # for循环遍历字典的时候，遍历的是key
# for item in d:
#     print('key', item)
#     for x in d[item]:
#         print(x)

n = 1
m = 100
while n <= m:
    print(' '*int((m-n)/2) + '*'*n)
    n += 2
