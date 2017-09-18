# -*- coding: utf-8 -*-
from random import randint
import timeit
###### 过滤掉列表[3,9, -1,10, 20, -2…]中的负数
__author__ = 'zb'
__date__ = '2017/9/17 10:06'


data = [randint(-10, 10) for _ in xrange(10)]
print data
# 取出 list 中所有正数
# 方法1
datanew = [x for x in data if x >= 0]
print datanew
# 方法2 filter
datanew2 = filter(lambda x: x >= 0, data)
print datanew2
