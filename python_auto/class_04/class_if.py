#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 11:19
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_if.py

# python 运算
# Python 条件语句
# 四星学习法
# 核心内容
# 为什么学
# 疑问和启发
# 可以应用操作

# 比较运算符：
# 0.01-200
# 假设你们输入的金额是x
# if 0.01 <= x <= 200:
#     发送成功
# else:
#     发送失败，提醒你金额的范围
# 运算符类型：算术运算符、比较（关系）运算符、赋值运算符、位运算符、成员运算符
# 运算符优先级
# 算术运算符： 加减乘除 整除 取余数 等
# + - * / %
# 判断奇数和偶数 x%2 = 0 x % 2 == 1
# 比较运算符： 比较左右两边的值的情况
# >= > <= < == !=
# 也是一种运算 运算结果是布尔值True or False or 0 or 1
# 情况： 期望结果是否邓毅实际结果

# 赋值运算 = -= += *= /=
# 逻辑运算符 and/or and 真真为真 其他情况为假  or 假假为假， 其他情况为真
# 成员运算符 in 存在/not in 不存在
# s1 = ['liu', 'abc']
# print('l' in s1)
# print('l' in s1[0])

# 简单的条件判断语句
# # if
# sex = input('请输入你的性别：')
# if sex == '女':  # 只对一种情况做了处理
#     print('和花花逛街')

# 2 if...else 当if后面的条件满足的时候，执行if的代码，否则执行else下面的代码
# 以下满足班级之星的条件
# task_score = 100 分数
# absence = 0 缺勤次数
# task_score = int(input('请输入你的分数'))
# absence = int(input('请输入你的缺勤次数'))
# if task_score == 100 and absence == 0
#     print('恭喜你获取班级之星')
# else:
#     print('不好意思，你的分数是{},你的缺勤次数{}'.format(task_score, absence))

# if 后面的条件 可以是 逻辑 比较 成员 True False 0 1

# if...elif...else
# if elif 可以加条件
# name = input('请输入你对象的名字')
# height = int(input('输入你对象身高'))
# if name == '马云':
#     print('这对象挺好的')
# elif name != '马云':
#     if height == 175:
#         print('对象挺好的')
#     else:
#         print('没啥好说的')
#
# # A :红绿灯
# color = input('请输入你看到的颜色')
# if color == 'red':
#     print('请不要乱动，请等待')
# elif color == 'yellow':
#     print('请等待')
# elif color == 'green':
#     print('可通行')
# else:
#     print('你是不是社盟')

# if 最前面 elif 中间 else最后面
# login_info = {'name':'huahua', 'pwd': '123456'}
# # name = input('请输入用户名：')
# # pwd = input('请输入密码：')
# # if name == login_info['name'] and pwd == login_info['pwd']:
# #     print('登录成功')
# # else:
# #     print('用户名或密码错误')


