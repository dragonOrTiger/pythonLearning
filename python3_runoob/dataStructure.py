#!/usr/bin/python3
#Python中列表是可变的，这是它区别于字符串和元组的最重要的特点
a = [66.25, 333, 333, 1, 1234.5]
print("原始列表: ", a)
print("列表a中元素333出现%d次，元素66.25出现%d次，元素'x'出现%d次" % (a.count(333), a.count(66.25), a.count('x')))
a.insert(2, -1)
print("after insert(2, 1): ", a)
a.append(333)
print("after append(333): ", a)
a.remove(333)
print("afer remove(333): ", a)
a.reverse()
print("after reverse(): ", a)
a.sort()
print("after sort()", a)
"""
将列表当作堆栈来使用
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放。
用append方法可以把一个元素添加到栈顶，用不指定索引的pop方法可以把一个元素从栈顶释放出来
"""
stack = [3, 4, 5]
print("原始堆栈: ", stack)
stack.append(6)
print("6入栈后: ", stack)
stack.append(7)
print("7入栈后: ", stack)
print("栈顶元素: ", stack.pop(), "出栈后: ", stack)
print("栈顶元素: ", stack.pop(), "出栈后: ", stack)
print("栈顶元素: ", stack.pop(), "出栈后: ", stack)
print("栈顶元素: ", stack.pop(), "出栈后: ", stack)
"""
将列表当作队列使用
也可以把列表当作队列用，只是在队列里第一加入的元素，第一个取出来; 但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快, 然而在列表里插入或者从头部弹出速度却不快(因为所有其他的元素都得一个一个地移动)
"""
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
print("原始队列: ", queue)
queue.append('Terry')
print("Terry加入队列后: ", queue)
queue.append('Graham')
print("Graham加入队列后: ", queue)
print("第一个元素: ", queue.popleft(), "出列后: ", queue)
print("第一个元素: ", queue.popleft(), "出列后: ", queue)
"""
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列
每个列表推导式都在for之后跟一个表达式，然后有零到多个for或if子句，返回结果是一个根据表达从其后的for和if上下文环境中生成出来的列表。
"""
vec = [2, 4, 6]
print("vec中每个元素乘以3获得一个新列表: ", [3*x for x in vec])
print("vec中每个元素x->[x, x**2]获得新列表: ", [[x, x**2] for x in vec])
print("vec中大于3的元素乘以3获得一个新列表: ", [3*x for x in vec if x > 3])
print("vec中小于2的元素乘以3获得一个新列表: ", [3*x for x in vec if x < 2])
#圆括号返回的是生成器generator
print((3*x for x in vec))
#对序列里的每一个元素逐个调用某个方法
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("freshfruit中每个元素删除前导空格和后面的空格获得一个新列表: ", [x.strip() for x in freshfruit])
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec for y in vec2])
print([x + y for x in vec for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])
print([str(round(355/133, i)) for i in range(1, 6)])
#嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print("matrix = ", matrix)
print("matrix的转置矩阵: ", [[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("matrix的转置矩阵: ", transposed)
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("matrix的转置矩阵: ", transposed)
"""
del语句
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("a = ", a)
del a[0]
print("delete a[0]后a = ", a)
del a[2:4]
print("delete a[2:4]后a = ", a)
del a[:]
print("delete a[:]后a = ", a)
"""
元组和序列
元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号
"""
t = 12345, 54321, 'hello!'
print(type(t))
print("t = ", t)
"""
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素
元素必须是不可变的
可以用大括号{}创建集合
注意: 如果要创建一个空集合，你必须用set()而不是{}; 后者用于创建一个空字典
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket = ", basket)
print("basket include 'orange'?", 'orange' in basket)
print("basket include 'tamato'?", 'tamato' in basket)
a = set('abracadabra')
b = set('alacazam')
print("集合a: ", a)
print("集合b: ", b)
print("a - b = ", a - b)
print("b - a = ", b - a)
print("a & b = ", a & b)
print("a | b = ", a | b)
print("a ^ b = ", a ^ b)
#集合也支持推导式
a = {x for x in "abracadabra" if x not in "abc"}
print("a = ", a)
"""
字典
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值
理解字典的最佳方式是把它看作无序的键=>值对集合。
在同一个字典内，关键字必须是互不相同的
一对大括号创建一个空字典
"""
tel = {'jack' : 4098, 'sape' : 4139}
print("原始字典: ", tel)
tel['guido'] = 4127
print("添加'guido'=>4127之后: ", tel)
print("tel['jack'] = ", tel['jack'])
del tel['sape']
print("删除'sape'之后: ", tel)
tel['irv'] = 4127
print("添加'irv'=>4127之后: ", tel)
print("字典的键集合: ", list(tel.keys()))
print("字典的键集合经排序后: ", sorted(tel.keys()))
print("字典包含'guido'?", 'guido' in tel)
print("字典包含'jack'?", 'jack' not in tel)
#构造函数dict()直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
#字典推导可以用来创建任意键和值的表达式字典
print({x : x**2 for x in (2, 4, 6)})
#如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
print(dict(scape=4139, guido=4127, jack=4098))
"""
在字典中遍历时，关键字和对应的值可以使用items()方法同时解读出来
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print("%s => %s" % (k, v))
"""
enumerate(iterable[, start]) -> iterator for index, value of iterable
Return an enumerate object. 
iterable must be another object that supports iteration. 
The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
(0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""
for i, v in enumerate(['tic', 'tac', 'toe']):
    print("第%d元素是%s" % (i, v))
"""
zip(iter1 [,iter2 [...]]) --> zip object
Return a zip object whose .__next__() method returns a tuple where the i-th element comes from the i-th iterable argument. 
The .__next__() method continues until the shortest iterable in the argument sequence is exhausted and then it raises StopIteration.
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("what is your %s? It is %s." % (q, a))
#要反向遍历一个序列，首先指定这个序列，然后调用reversed()函数
for i in reversed(range(1, 10, 2)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
