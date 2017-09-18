# -*- coding: utf-8 -*-
from random import randint
from collections import Counter

__author__ = 'zb'
__date__ = '2017/9/17 20:58'

# 统计序列中元素出现的频度

# 随机 序列
data = [randint(0, 20) for x in xrange(20)]
print data
# 根基列表 生成字典 key 是data的值，value默认是0
dicts = dict.fromkeys(data, 0)
# print dicts
# 统计次数
for x in data:
    dicts[x] += 1
print dicts
# 根据values 排序x:x[1] ,按照key进行排序 x:x[1]
# 通过key这个参数，指定排序是按照value，也就是第一个元素d[1的值来排序。
# reverse = True表示是需要翻转的，默认是从小到大，翻转的话，那就是从大到小
#
newdicts = sorted(dicts.iteritems(), key=lambda x:x[1], reverse=True)
print newdicts


# 使用couter 对象

# 将序列传入Couter 构造器 ，得到Counter 对象是 元素频度的字段
t1 = Counter(data)
print t1
# Counter.most_common(n)  得到频度最高的
print t1.most_common(3)