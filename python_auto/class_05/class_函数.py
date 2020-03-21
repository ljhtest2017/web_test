#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/14 14:55
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : class_函数.py
# 自定义函数
# 内置函数
# 函数的参数类型
# 函数的相互调用和定义顺序
# 变量的作用域
# 解决问题： 学会写函数 提高代码的复用性
# def 函数名(参数列表):
#     """函数注释"""
#     执行代码
#     return 代码
# def 关键字 def 函数名
# 函数名： 字母数字下划线组成 不能数字开头 不能使用关键字 不能跟Python的其他函数重名


# def add(a, b):
#     """这是一个加法，完成两个数相加的功能"""
#     c = a + b  # 函数代码块
#     # print('{} + {} 的值是{}'.format(a, b, c))
#
#     return c  # return后面的表达式可加可不加 根据你自身的情况去调整
#
#
# # 怎么调用   函数名（参数列表）
# result = add(1, 20)  # 实参  当你调用函数的时候 传递的参数
# print(result)


# 关键字 return 当你调用一个函数的时候 会帮你返回return后面的表达式

# 返回数目=0 返回None
# 返回数目=1 返回对应值
# 返回数目>1  返回元组

def robot():
    print('hello')
    # 隐式的给你添加一个没有任何表达式的return


# 当你调用函数的时候，才会生效
print(robot())
# 调用函数时候才会执行函数下的代码

# len type int() str() float()

#
