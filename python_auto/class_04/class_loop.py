#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 12:46
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_loop.py
# 循环语句逻辑
# while 循环
# for 循环
# 嵌套循环
# Python没有do...
# 语法：
# while 判断条件:
#     执行语句....
# while循环 关键字while while后面加条件
# while后面可以是  布尔值 非空的 空数字 比较 逻辑 成员
# 执行逻辑： 先判断  条件成立True 执行代码 执行完毕后再判断 如果条件不成立，False over
# n = 5
# while n < 10:
#     print('hello 我是while循环')
#     n += 1
#     if n == 7:
#         continue   # 结束本次循环
#     if n == 9:
#         break   # 终止循环
#     print(n)

# 不要让表达式成为永真式
sex = input('请输入姓名（m表示男性，f表示女性）')
age = int(input('请输入年龄'))
n = 1
result = 0
while n < 10:
    sex = input('请输入姓名（m表示男性，f表示女性）')
    age = int(input('请输入年龄'))
    if sex == 'm' and 10 <= age <= 12:
        result += 1
    else:
        print('不符合条件，请重新输入')
    n += 1
print(result)