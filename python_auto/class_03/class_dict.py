#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 10:59
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_dict.py
# 字典：dict {}

# 1 空字典 查看数据的类型type()
# d = {}
# print(type(d))
# 2 字典的数据格式： key: value形式的
# key: 不可变类型  整数 浮点数 布尔值 元组 字符串
# value: 任意数据类型都支持  整数 浮点数 布尔值 元组 字符串 列表 字典
d = {1: '666',
     1.01: "这是",
     True: [1, 2],
     (1, 2, 3): [3, 4],
     'name': ('ju', 'aw'),
     }
print(d)
# 3字典是可变的数据类型， 无序的--没有索引
# key 必须是唯一的，0，1 ，True ,False
# True 1 , False 0
# 取值 取值方式：字典名[键名】 函数字典名.get(键名)
print(d['name'])
print(d.get('name'))

# 赋值 字典名[键名]=值
d['name'] = '刘家海'
print(d)