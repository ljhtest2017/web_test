#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 10:45
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_list.py
# 列表： list []

# 空列表 查看数据的类型type()
l = []
print(type(l))
# 2 列表里面的数据可以是任意类型数据类型，元素以逗号来进行分隔
L = [1, 0.3, True, 'hello', (0, 'lemon', 99.9), ['刘家海', '徐艳荣']]
# 列表取值同字符串方法
# 支持切片
# 嵌套列表的取值 列表里面还有列表或其他数据类型  层层取
# 列表是一个有序可变数据类型， 可以进行修改
L[-1][-1] = '123'
print(L)
# 特殊情况
t = (1, 0.3, True, 'hello', (0, 'lemon', 99.9), ['刘家海', '徐艳荣'])
t[-1][0] = 'qq'
print(t)
