#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 10:33
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_tuple.py

# 元组 tuple()

# 空元组 （,） 查看数据的类型type()
t = ()
print(type(t))
# 2：元组里面的数据可以是任意类型,元素以逗号来进行分隔
t = (1, 0.3, True, 'hell', (8, 'lemon', 99.9))
# 3 元组里面的只有一个数据的时候，加一个逗号，保持元组的属性
# 元组取值 方法同 字符串 表示元组有索引的，从0开始，也会有正序和倒序

# 元组取单个值 元组名[索引值]
print(t[0])

# 支持切片
print(t[1:3])
# 嵌套元组的取值 元组里面还有元组或其他数据类型
print(t[4][2])

# 7 元组是一个有序不可变数据类型
t[0] = -1  # 报错TypeError: 'tuple' object does not support item assignment