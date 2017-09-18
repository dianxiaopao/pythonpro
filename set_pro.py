# -*- coding: utf-8 -*-
from random import randint
import timeit

__author__ = 'zb'
__date__ = '2017/9/17 10:06'
## #### 筛出集合{77,89,32, 20…}中能被3整除的元素
# 列表
data = [randint(-10, 10) for _ in xrange(10)]
print data
# 取出 list 中所有正数
# 方法1
datanew = [x for x in data if x >= 0]
print datanew
# 方法2 filter
datanew2 = filter(lambda x: x >= 0, data)
print datanew2

# 列表转集合

set1 = set(data)
print set1
set2 = {i for i in set1 if i % 3 == 0}
print set2
