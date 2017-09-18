# !/usr/bin/env python
# -*-coding:utf-8
from collections import OrderedDict
from random import randint
from time import time

"""
如何让字典保持有序？
某编程竞赛系统，对参赛选手编程解题进行计时，选手完成题目后,
把该选手解题用时记录到字典中，以便赛后按选手名査询成绩.
(答题用时越短，成绩越优.）
{'LiLei': (2, 43), 'HanMeimei':(5,52), 'Jim': (1, 39)}

比赛结束后，需按排名顺序依次打印选手成绩，如何实现？
解决方法 ： collection.OrderedDict  按照放入字典的顺序维护

"""

d = {}
d['LiLei'] = (1, 49)
d['HanMeimei'] = (2, 48)
d['Jim'] = (3, 40)
# 无序的
for k in d: print k

d = OrderedDict()
d['LiLei'] = (1, 49)
d['HanMeimei'] = (2, 48)
d['Jim'] = (3, 40)
# 有序的
for k in d: print k

# 模拟编程提交成绩，记录排名
players = list("ABCDEFGH")
start = time()
d = OrderedDict()
for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7-i))
    end = time()
    print i+1, p, end - start,
    d[p] = (i+1, end-start,)


print
# 打印分割符号
print '_' * 20
for i in d: print i, d[i]

