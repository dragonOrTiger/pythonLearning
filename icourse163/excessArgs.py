#!/usr/bin/python3
"""
位置参数:
在参数名之前使用一个星号，就是让函数接受任意多的位置参数
python把参数收集到一个元组中，作为变量args。
显式声明的参数之外如果没有位置参数，这个参数就作为一个空元组
"""
def multiply(*args):
    total = 1;
    for arg in args:
        total *= arg
    return total
print("2 * 3 * 4 * 5 * 6 = ", multiply(2, 3, 4, 5, 6))
"""
关键字参数:
python在参数名之前使用两个星号来支持任意多的关键字参数
kwargs是一个正常的python字典类型，包含参数名和值。
如果没有更多的关键字参数，kwargs就是一个空字典
"""
def accept(**kwargs):
    for keyword, value in kwargs.items():
        print("%s => %r" % (keyword, value))
accept(foo = 'bar', spam = 'eggs')
"""
混合参数类型
任意的位置参数和关键字参数可以和其他标准的参数声明一起使用。
混合使用时要加些小心，因为python中他们的次序是重要的。
参数归为4类，不是所有的类别都需要。他们必须按下面的次序定义。不用的可以跳过
1. 必须的参数
2. 可选参数
3. 过量的位置参数
4. 过量的关键字参数
def complex_function(a, b = None, *c, **d)
这个次序是必须的，因为*args和**kwargs只接受那些没有放进来的其他任何参数。
没有这个次序，当你调用一个带有位置参数的函数，python不知道哪个值是已声明参数想要的，
也不知道哪个被作为过量参数对待。
也要注意的是，当函数能接受许多必须的参数和可选的参数，那它只要定义一个过量的参数类型即可。
"""
def add(a, b, c):
    return a + b + c
print("add(1, 2, 3) = ", add(1, 2, 3))
print("add(a = 4, b = 5, c = 6) = ", add(a = 4, b = 5, c = 6))
args = (2, 3)
print("add(1, *args) = ", add(1, *args))
kwargs = {'b' : 8, 'c' : 9}
print("add(a = 7, **kwargs) = ", add(a = 7, **kwargs))

"""
默认参数很有用，但使用不当，也会掉坑里，默认参数有个最大的坑，演示如下:
先定义一个函数，传入一个list, 添加一个END再返回
"""
def add_end(L=[]):
    L.append('END')
    return L
#当你正常调用时，结果似乎不错:
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
#当你使用默认参数调用时，一开始结果也是对的:
print(add_end())
#但是，再次调用add_end()时，结果就不对了
print(add_end())
print(add_end())
#很多初学者很疑惑，默认参数是[]，但是函数似乎每次都'记住了'了上次添加了'END'后的list
#原因解释如下: python函数在定义的时候，默认参数L的值就被计算出来了，[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义的[]了
#定义默认参数要牢记一点: 默认参数必须指向不变对象
#要修改上面的例子，我们可以用None这个不变对象来实现:
def add_end_1(L1=None):
    if L1 is None:
        L1 = []
    L1.append('END')
    return L1
print(add_end_1())
print(add_end_1())
#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def cacl(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(cacl(1, 2))
print(cacl(1, 3, 5, 7, 9))
#python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(cacl(*range(10)))

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
#关键字参数有什么用呢？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是， 如果调用者愿意提供更多的参数，我们也能收到，试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw函数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city':'Beijing', 'job':'Enjineer'}
person('Jack', 24, **extra)
#如果要限制关键字参数的名字，就可以用命名关键字参数。例如，只接收city和job作为关键字参数。
def person1(name, age, *, city, job):
    print(name, age, city, job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*， *后面的参数被视为命名关键字参数。
person1('Jack', 24, city='Beijing', job='Engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person2(name, age, *arg, city, job):
    print(name, age, *arg, city, job)
person2('Jack', 24, [1, 2], city='Beijing', job='Engineer')

#命名关键字参数可以有缺省值，从而简化调用
def person3(name, age, *arg, city='Beijing', job):
    print(name, age, *arg, city, job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数
person3('Jack', 24, [1, 2], job='Engineer')

"""
参数组合
在python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数。这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是:必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
