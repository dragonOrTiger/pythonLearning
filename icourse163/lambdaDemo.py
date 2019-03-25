#!/usr/bin/python3
"""
lambda只是一个表达式，定义了一个匿名函数，起到函数速写的作用
lambda并不会带来程序运行效率的提高，只会使代码更简洁
在python中，lambda的语法时唯一的。其形式如下:
lambda argument_list : expression
其中，lambda是python预留的关键字，argument_list和expression由用户自定义。
这里的argument_list是参数列表。它的结构与Python中函数(function)的参数列表是一样的。
具体来说，argument_list可以有非常多的形式。例如:
a, b    a = 1, b = 2    *args   **kwargs    a, b = 1, *args 空   等等
这里的expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的。以下都是合法的表达式:
1   None    a + b   sum(a)  1 if a > 10 else 0  等等
lambda *args : sum(args);输入任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
lambda **kwargs : 1;输入是任意键值对参数，输出是1

1. 将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数
2. 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
   time.sleep=lambda x:None可以将标准库time中的函数sleep的功能屏蔽。
3. 将lambda函数作为其他函数的返回值，返回给调用者。函数的嵌套。
4. 将lambda函数作为参数传递给其他函数。reduce， map, filter, sorted函数等等
"""
#python列表或python字典的成员可以是函数
#由于lambda是一个表达式，它可以直接作为python列表或python字典的成员
class cl():
    pass
def f():
    pass
print(type(f))
info = [lambda a : a ** 2, lambda b : b ** 3, f, cl, type(f)]
print(info)
print(type(info[0]))
g = lambda x : x + 1#其中x为入口参数，x+1为函数体
print("g(3) = ", g(3))
#lambda也可以用在函数中
def action(x):
    return lambda y : x + y
print("action(3)(22) = ", action(3)(22))
#lambda可以嵌套
qt = lambda x : lambda y : x + y
print("qt(3)(22) = ", qt(3)(22))
#lambda可以是一个或者多个参数
multiArg = lambda x, y, z : x + y + z
print("multiArg(2, 3, 4) = ", multiArg(2, 3, 4))
print("任意个数的参数: ", (lambda *z : z)('h', 'e', 'l', 'l', 'o'))
print("任意键值对参数: ", (lambda **z : z)(a = 1, b = 2, c = 3))
"""
filter(function or None, sequence) --> list, tuple,or string
function是一个谓词函数，接受一个参数，返回布尔值True或False
filter函数会对序列参数sequence的每个元素调用function函数
最后返回执行结果为True的
返回值的类型和参数sequence(list,tuple,string)的类型他相同
"""
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print("foo中能被3整除的数: ", list(filter(lambda x : x % 3 == 0, foo)))
print("foo中能被3整除的数: ", [x for x in foo if x % 3 == 0])
"""
map(function, sequence)
对sequence中的item译词执行function，将执行结果组成list返回
"""
str = ['a', 'b', 'c', 'd']
print("str的元素尾部都加.txt后: ", list(map(lambda x : x + '.txt', str)))
print("range(5)和range(5)对应元素相加后: ", list(map(lambda x, y : x + y, range(5), range(5))))
"""
reduce(function, sequence, starting_value)
对sequence中的item顺序迭代调用function，如果有starting_value
还可以作为初始值调用，
"""
from functools import reduce
print("2000 + 1到100求和: ", reduce(lambda x, y : x + y, range(1, 101), 2000))
"""
sorted(sequence, function or None)
lambda函数用于指定对列表中所有元素排序的准则
"""
print("[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5之间的距离从小到大排序: ", sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x)))
"""
求2-100之间的素数
素数：只能被1或被自己整除的数
"""
nums = range(2, 50)
for i in nums:
    nums = list(filter(lambda x : x == i or x % i, nums))
    print("第", i - 1, "次过滤后: ", nums)
