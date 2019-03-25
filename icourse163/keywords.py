#!/usr/bin/python3
'''
True False None为内置常量
True False是布尔类型常量，True的值是整数1，False的值是整数0
None比较特殊，表示什么也没有，它有自己的数据类型，NoneType
'''
print(True, "是一个内置常量，其值为整数1?", True == 1)
print(False, "是一个内置常量，其值为整数0?", False == 0)
print(True, "是什么类型常量?", type(True))
print(False, "是什么类型常量?", type(False))
print(None)
print(None, "是什么类型常量?", type(None))
"""
and or not
Python具有短路逻辑，
False and 返回 False,不执行后面的语句
True or 直接返回True，不执行后面的语句
x and y:
如果x是False None 0,返回x，否则返回y
x or y:
如果x是False None 0,返回y，否则返回x
not x:
如果x是False None 0,返回True，否则返回False
"""
print(None, "取反是:", not None)
print(0, "取反是:", not 0)
print(1, "取反是:", not 1)
print(2, "取反是:", not 2)
"""
del
列表本身包含的是变量,
"""
#li包含li[0],li[1],li[2],li[3],li[4]，并不包含1,2,3,4,5
li = [1, 2, 3, 4, 5]
print(li)
#拷贝列表，也不会有数据对象复制，而是创建新的变量引用
first = li[0]
#列表本身包含的是变量，del删除的是变量
del li[0]
print(li)
print(first)
"""
pass是空语句，为了保证程序结构的完整性
pass不做任何事情，一般用作占位语句，
当你编写程序，部分内容还没想好，可用pass语句占位
"""
for letter in "python":
	if letter == "h":
		pass
		print("this is pass block")
	print("当前字母是: ", letter)
print("bye bye")
"""
yield: yield的意思是生产，返回了一个生成器对象，每个生成器只能使用一次
一个带有yield的函数就是一个generation，他和普通函数不同，
生成一个generator看起来像函数调用，但不会执行任何函数代码，
直到对其调用.__next__()(在for循环中会自动调用__next__())才开始执行
虽然执行流程仍按函数的流程执行，但每次执行到一个yield语句就会中断，并返回一个迭代值，
下次执行时从yield的下一个语句继续执行。
看起来就好像一个函数在正常执行过程中被yield中断了数次，每次中断都会通过yield返回当前的迭代值。
send与__next__
send()可以传递yield表达式的值进去，而__next__()不能传递特定的值，只能传递None进去
因此，我们可以看做c.__next__()和c.send(None)作用一样的
注意!!!第一次调用时，请使用__next__()语句或是send(None),
不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收
有效利用生成器这个工具，可以有效节约系统资源，避免不必要的内存占用。
生成器和迭代器差不多，但是它只能运行一次，因为它不是把值存储在内存中，而是直接运行生成值
"""
def h():
	print("wen chuan")
	yield 5
	print("fighting")
from inspect import isgeneratorfunction
print("h函数是generator吗?", isgeneratorfunction(h))
c = h()
c.__next__()
#再次运行c.__next__()时，由于没有了yield所以报错
#print(c.__next__())
print("*******************************************************")
def generator():
    print("wen chuan")
    m = yield 5
    print(m)
    d = yield 12
    print("We are together!")
c1 = generator()
m = c1.__next__()
d = c1.send("Fighting")
print("we will never foget the date ", m, ".", d)
"""
兔子繁殖问题: 斐波那契数列
F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
"""
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fab(10):
    print(n, " ", end = "")
print()
"""
生成器:可迭代，只能读取一次，实时生成数据，不全存在内存中
"""
mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)
#生成器只能读取一次，第二次调用没有输出
for i in mygenerator:
    print(i)
"""
控制生成器的穷尽
"""
class bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"
hsbc = bank()
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.__next__())
print(corner_street_atm.__next__())
print([corner_street_atm.__next__() for crash in range(5)])
hsbc.crisis = True
#这个时候调用corner_street_atm.__next__()会抛出异常StopIteration
wall_street_atm = hsbc.create_atm()
#这个时候调用corner_street_atm.__next__()会抛出异常StopIteration,因为没有yield
hsbc.crisis = False
#这个时候调用corner_street_atm.__next__()也会抛出异常StopIteration，因为已经结束迭代了
brand_new_atm = hsbc.create_atm()
#下面的循环迭代，会一直往出吐钱
#for cash in brand_new_atm:
#    print(cash)
"""
with用于处理异常
1.不用with处理异常：
file = open('tempExchange.py')
try:
	data = file.read()
finally:
	file.close()
**********************************
2.紧跟在with后面的语句被求值后，返回对象的enter()方法被调用，
这个方法的返回值将复制给as后面的变量，
当with后面的代码块全部执行完后，将调用前面返回对象的exit()方法
3.with的真正强大之处是它可以处理异常，
异常抛出时，与之关联的type，value，stack trace传给exit()方法
4.开发库时，清理资源，关闭文件等等操作，都可以放在exit方法中
"""
print('*********************tempExchange.py***************************')
with open('tempExchange.py') as file:
	data = file.read()
print(data)
print('***************************************************************')
class Sample:
	def __enter__(self):
		print("in __enter__")
		return "Foo"
	def __exit__(self, type, value, trace):
		print("in __exit__")
def getSample():
	return Sample()
with getSample() as sample:
	print("sample: ", sample)
class withDealException:
	def __enter__(self):
		return self
	def __exit__(self, type, value, trace):
		print("type: ", type)
		print("value: ", value)
		print("trace: ", trace)
	def doSomething(self):
		assert(1 == 2)
with withDealException() as demo:
	demo.doSomething()
"""
assert: 断言其布尔值必须为真的判定，如果发生异常就说明表达式为假的
"""
