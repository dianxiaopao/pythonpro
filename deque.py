# !/usr/bin/env python
# -*-coding:utf-8

"""
双端队列


很多应用程序都有浏览用户的历史记录的功能,例如：
浏览器可以记录最近访问过的网页.
视频播放器可以査看最近播放过视频文件.
Shell可以査看用户输入过的命令.
现在我们制作了一个简单的猜数字的小游戏，
添加历史记录功能，显示用户最近猜过的数字,
如何实现？


解决方案：


使用容量为n的队列存储历史记
使用标准库collections中的deque,它是一个双端循环队列
程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入



python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
　　基本接口：
　　pickle.dump(obj, file, [,protocol])
　　注解：将对象obj保存到文件file中去。
　　　　　protocol为序列化使用的协议版本，0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；1：老式的二进制协议；2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为0。
　　　　　file：对象保存到的类文件对象。file必须有write()接口， file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。如果protocol>=1，文件对象需要是二进制模式打开的。
　　pickle.load(file)
　　注解：从file中读取一个字符串，并将它重构为原来的python对象。
　　file:类文件对象，有read()和readline()接口。


"""
from collections import deque
from random import randint

import pickle

N = randint(0, 100)
# 初始化一个长度为 5 的 双端队列
history = deque([], 5)
print N
q2 = pickle.load(open('history.txt'))
print q2


def guess(k):
    if k == N:
        print 'right'
        return True
    if k < N:
        print '%s is less than N' % k
    else:
        print '%s is greater than N' % k
    return False


while True:
    line = raw_input('请输入数字:\n')
    # 检测字符串是否只由数字组成
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            pickle.dump(history, open('history.txt', 'w'))
            break
    elif line == "history" or line == "h?":
        print list(history)
    elif line == "exit":
        # 退出循环，结束程序，记录到文件
        pickle.dump(history, open('history.txt', 'w'))
        break

