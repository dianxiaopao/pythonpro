# -*- coding: utf-8 -*-
from random import randint
import timeit
# 筛出字典 {'fLiLei1':79, 'Jim1':88, 'Lucy': 92 }中值高于90的值
__author__ = 'zb'
__date__ = '2017/9/17 10:06'

# 随机生成一个字典
data = {x:randint(50, 100) for x in xrange(1, 21)}
print data
# 取出  vulue值大于100 的
datanew = {k: v for (k, v) in data.iteritems() if v > 90}
print datanew
