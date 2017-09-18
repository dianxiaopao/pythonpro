# !/usr/bin/env python
# -*-coding:utf-8
import os

s = 'lovepython'

# 输出从第5个开始至列表末尾的所有元素
print s[4:]
# 从0开始计数，娶不到上限
# 输出从第2个开始第4个元素
print s[1:4]

print s * 2

lists = ['runoob', 786, 2.23, 'john', 70.2]
tinlist = ['test1', 88888]
print lists[0]   # 输出列表的第一个元素
print lists[1:3]  # 输出第二个至第三个的元素
print lists * 2   # 输出列表两次
print lists + tinlist
print lists      # 输出完整列表
# 元组是另一个数据类型，类似于List（列表）。 元组用"()"标识。内部元素用逗号隔开。
# 但是元组不能二次赋值，相当于只读列表。
tuples = ('1', '2', 99)
#tuples[1] = 888
lists[1] = 'nibbn'
print lists


"""
Python 字典
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
"""
dicts = {"name": "张三", "password": "888888", 'dept': 'sales'}
print '**************start*************'
# 直接循环 循环的是  key
for i in dicts:
    print i
print '**************end***********'

print '*************iterkeys**************'
# iterkeys 循环的是  key
for i in dicts.iterkeys():
    print i
print '************end***************'

print '*************iteritems**************'
# iteritems 循环的是  key,value
for i in dicts.iteritems():
    print i
print '************end***************'


print '*************viewkeys**************'
# viewkeys,返回set 循环的是  key,value
for i in dicts.viewkeys():
    print i
print '************end***************'
# 注意列表取值 方式有两种 1.dics['key']  直接点 是不行的
# 2.dicts.get('name', '') 第二参数 指定 如果值不在字典中返回的值 在
print dicts['name']
print dicts.get('name', '11')
print dicts.get('names', '11')
print dicts.values()
# 删除
print str(dicts)
# 删除指定key的值，不存在 返回 1
print dicts.pop('depts', '1')
print str(dicts)

# path
print os.path.dirname(__file__)
