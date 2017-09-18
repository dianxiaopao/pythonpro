# -*- coding: utf-8 -*-
from collections import namedtuple
__author__ = 'zb'
__date__ = '2017/9/17 20:42'

# 此元祖取值只能采用 s索引额形式, 不方便
student = ('张三', 18, '男', '878@qq.com')
print student[0], student[1], student[2], student[3]

# 方法1
# 将 0,1,2,3 分别赋给四个变量
name, age, sex, email = xrange(4)
student = ('张三', 18, '男', '878@qq.com')
# 实际 是 student[0]  student[1]
print student[name], student[age], student[sex], student[email]

# 方法2
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
student2 = Student('张三', 18, '男', '878@qq.com')
print student2.name, student2.age, student2.sex, student2.email
