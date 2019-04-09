#!/ust/bin/python3
"""
定义一个函数:
函数代码块以def关键词开头，后续函数标识符名称和圆括号()
def 函数名(参数列表)
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
函数的第一行语句可以选择性地使用文档字符串，用于存放函数说明
函数内容以冒号起始，并且缩进
return [表达式]结束函数，选择性的返回一个值给调用方。不带表达式的return相当于返回None 
"""
def test(a, b):
    "用来完成对2个数求和"
    print("%d + %d = %d" % (a, b, a + b))
#help(test)可以看到test函数的相关说明
help(test)
test(11, 22)
def hello():
    "say 'Hello World!'"
    print("Hello World!")
hello()
def area(width, height):
    return width * height
def print_welcome(name):
    print("Welcome", name)
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
def printme(str):
    print(str)
    return
printme("我要调用用户自定义函数！")
printme("再次调用同一函数")
"""
在python中，类型属于对象，变量是没有类型的
a = [1, 2, 3]
a = "Runoob"
以上代码中，[1, 2, 3]是List类型，"Runoob"是Sring类型，而变量a是没有类型的，
她仅仅是一个对象的引用(一个指针)，可以指向List类型对象，也可以是指向String类型对象
"""
"""
在python中，strings，tuples，和numbers是不可更改的对象，而list，dict等则是可以修改的对象
不可变类型: 变量赋值a = 5后再赋值a = 10,这里实际是新生成一个int值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a
可变类型: 变量赋值la = [1, 2, 3, 4]后再赋值la[2] = 5则是将list la的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了
python函数的参数传递:
不可变类型: 类似C++的值传递，如整数，字符串，元组。如fun(a), 传递的只是a的值，没有影响a对象本身。比如在fun(a)内部修改a的值，只是修改了另一个复制的对象，不会影响a本身
可变类型: 类似C++的引用传递，如列表，字典。如fun(la),则是将la真正的传过去，修改后fun外部的la也会受到影响
python中一切皆对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象
"""
"""
python传不可变对象实例
实例中有int对象2,指向它的变量b，在传递给ChangeInt函数时，按传值的方式复制了变量b，a和b都指向了同一个Int对象，在a=10时，则新生成一个int值对象10，并让a指向它
"""
def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print("b = %d" % b)
"""
传可变对象实例
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了
"""
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
#必须参数: 须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
printme("Hello World!")
#关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
#使用关键字参数允许函数调用时参数的顺序和声明时一致，因为Pyhthon解释器能够用参数名匹配参数值
printme(str = "菜鸟教程")
def printinfo(name, age):
    "打印任何传入的字符串"
    print("name: ", name)
    print("age: ", age)
    return
printinfo(age = 50, name = "runoob")
#默认参数: 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入age参数，则使用默认值
def printinfo(name, age = 35):
    "打印任何传入的字符串"
    print("name: ", name)
    print("age: ", age)
    return
print("------------------------------")
printinfo("runoob")
printinfo("runoob", age = 78)
printinfo(name = "runoob")
printinfo(name = "runoob", age = 78)
#不定长参数: 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名
#加了星号*的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
#如果在函数调用时没有指定参数，他就是一个空元组。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(70, 60, 50)
printinfo(10)
#加了两个星号**的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print(arg1)
    print(vardict)
printinfo(1, a = 2, b = 3)
#声明函数时，参数中星号*可以单独出现
#如果单独出现星号*后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c
print(f(1, 2, c = 3))
getSum = lambda arg1, arg2 : arg1 + arg2
print("相加后的值为: ", getSum(10, 20))
print("相加后的值为: ", getSum(20, 20))
"""
Python中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。
Python的作用域一共有四种，分别是:
L (Local): 局部作用域
E (Enclosing): 闭包函数外的函数中
G (Global): 全局作用域
B (Built-in): 内置作用域(内置函数所在模块的范围)
以L-->E-->G-->B的规则查找，即: 在局部找不到，便会去局部外部的局部找(例如闭包)，再找不到就会去全局找，再者去内置中找
内置作用域是通过一个名为builtins的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它
import builtins
dir(builtins)
Python中只有模块(module), 类(class), 以及函数(def, lambda)才会引入新的作用域，其它的代码块(如if/elif/else, try/except, for/while等)是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
"""
for x in range(4):
    print(x)
print(x)
if True:
    msg = 'I am from Runoob'
print(msg)
try:
    exception = "StopIteration"
    raise StopIteration
except StopIteration:
    pass
print(exception)
"""
全局变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
局部变量只能在其被生命的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
"""
total = 0
def getSum(a, b):
    total = a + b
    print("函数内是局部变量: ", total)
    return total
getSum(10, 20)
print("函数外是全局变量: ", total)
#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
num = 1
def fun1():
    global num#需要使用global关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)
#如果要修改嵌套作用域(enclosing作用域，外层非全局作用域)中的变量则需要nonlocal关键字了
def outer():
    number = 10
    def inner():
        nonlocal number
        number = 100
        print(number)
    inner()
    print(number)
outer()
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)
print(a)
