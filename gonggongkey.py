# !/usr/bin/env python
# -*-coding:utf-8

from random import randint, sample

"""
如何快速找到多个字典中的公共键(key)
案例：

西班牙足球甲级联赛，每轮球员进球统计：
第一轮:{'苏亚雷斯':1,'梅西':2}
第二轮:{'苏亚雷斯':2,'C罗':1, '贝尔':1...}
统计出前N轮，毎场比赛都有进球的球员.

"""
# 方法1  传统方法

"""
生成 随机 字典

"""
# random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
# 从字符串或者list中随机获取4个元素，作为一个片断返回
# seq = sample('abcdef', 4)

# 随机生成 每轮生成进球人员名单 列表
seq = sample('abcdef', randint(3, 6))
print seq

# 随机生成 每轮生成进球人员名单以及球数字典
data1 = {x: randint(1, 4) for x in seq}
# 第二轮
data2 = {x: randint(1, 4) for x in seq}
# 第三轮
data3 = {x: randint(1, 4) for x in seq}
print data1
print data2
print data3

retseq = []
for i in data1:
    if i in data2 and i in data3:
        retseq.append(i)
print retseq


"""
# 方法2  使用集合set 交集的方法
  
>>> x & y # 交集  
set(['a', 'm'])  
  
>>> x | y # 并集  
set(['a', 'p', 's', 'h', 'm'])  
  
>>> x - y # 差集  
set(['p', 's'])  

"""

# 对于3轮
sets = data1.viewkeys() & data2.viewkeys() & data3.viewkeys()
print sets

# 对于n轮
'''
map()函数接收两个参数，一个是函数(句柄，不需要带括号)，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
'''
s = map(dict.viewkeys, [data1, data2, data3])
print s

'''
reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
>>> def fn(x, y):
...   return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579

'''


def jiaoji(a, b):
    return a & b

print reduce(jiaoji, s)

# 简写
print reduce(lambda a, b: a & b, map(dict.viewkeys, [data1, data2, data3]))

