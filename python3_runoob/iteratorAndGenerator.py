#!/usr/bin/python3
"""
迭代是Python最强大的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，知道所有的元素被访问完结束。迭代器只能往前不会后退
迭代器有两个基本的方法: iter()和__next__()
字符串，列表或元组对象都可用于创建迭代器
"""
aList = [1, 2, 3, 4]
aIt = iter(aList)
"""
next(...)
next(iterator[, default])
Return the next item from the iterator. 
If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
"""
print(next(aIt))
print(next(aIt))
#迭代器对象可以使用常规for语句进行遍历
bList = [1, 2, 3, 4]
bIt = iter(bList)
for x in bIt:
    print(x, end=' ')
#import sys
#cList = [1, 2, 3, 4]
#cIt = iter(cList)
#while True:
#    try:
#        print(next(cIt))
#    except StopIteration:
#        sys.exit()
"""
把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()和__next__()方法
Python的构造函数为__init__()，它会在对象初始化的时候执行
__iter__()方法返回一个特殊的迭代器，这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
__next__()方法会返回下一个迭代器对象
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x    
  
myclass = MyNumbers()
myiter = iter(myclass)
print(type(myclass))
print(type(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""
StopIteration异常用于标识迭代的完成，防止出现无限循环的情况，
在__next__()方法中我们可以设置在完成指定循环次数后触发StopIteration异常来结束迭代
"""
class MyNumbersUpdate:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclassUpdate = MyNumbersUpdate()
myiterUpdate = iter(myclassUpdate)
for x in myiterUpdate:
    print(x)
"""
在Python中，使用了yield的函数被称为生成器(generator)
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行
调用一个生成器函数，返回的是一个迭代器对象
"""
import sys
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
print(type(f))
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
