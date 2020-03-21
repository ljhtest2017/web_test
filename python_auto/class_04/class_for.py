#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 13:12
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_for.py
# for 循环 关键字for 一般用来遍历元素 或者是利用遍历元素的次数来控制循环
s = '123'
s1 = [1, 2, 3]
for item in s:  # item是一个变量，依次访问s这个字符串里面的元素并赋值给item
    print(item)
# for循环 in 后面的数据必须是可迭代 元素是可数的： 字符串 列表 元组 字典
# for循环遍历字典，遍历key
result = 0
for i in range(10):
    sex = input('请输入姓名（m表示男性，f表示女性）')
    age = int(input('请输入年龄'))
    if sex == 'm' and 10 <= age <= 12:
        result += 1
    else:
        print('不符合条件，请重新输入')

# 知道循环次数用for 不确定的次数while
