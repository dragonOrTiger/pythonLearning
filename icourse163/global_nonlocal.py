#!/usr/bin/python3
"""
python引用变量的顺序: 当前作用域局部变量 -> 外层作用域变量 -> 当前模块中的全局变量 -> python内置变量
1. global关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字
"""
#第一行定义了一个全局变量，(可以省略global关键字)
gcount = 0
def global_test():
#如果在局部要对全局变量修改，需要在局部也要声明该全局变量
    global gcount
    gcount += 1
    print(gcount)
global_test()

gcount = 0
#在局部如果不声明全局变量，并且不修改全局变量。则可以正常使用全局变量
def global_test1():
    print(gcount)
global_test1()

"""
nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
"""
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())
make_counter_test()

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)
scope_test()
print("In global scope: ", spam)

#在函数add_b内global定义的变量b，只能在函数do_global内引用，如果要在do_global内修改，必须在do_global函数里面声明global b, 表明是修改外面的全局变量b:
def add_b():
    global b
    b = 42
    def do_global():
        global b
        b = b + 10
        print(b)
    do_global()
    print(b)
add_b()
print(b)

#global定义的变量，表明其作用域在局部以外，即局部函数执行完之后，不销毁函数内部以global定义的变量

def add_a():
    global a
    a = 3
add_a()
print(a)

def add_b1():
    global b1
    b1 = 42
    def do_global():
        global a1
        a1 = b1 + 10
        print(b1)
    do_global()
    print(a1)
add_b1()
print("a1 = %s, b1 = %s" % (a1, b1))

def add_b2():
    b2 = 42
    def do_global():
        global b2
        b2 = 10
        print(b2)
    do_global()
    print(b2)
add_b2()
print("b2 = %s" % b2)

def add_b3():
    b3 = 42
    def do_global():
        nonlocal b3
        b3 = 10
        print(b3)
    do_global()
    print(b3)
add_b3()

def add_b4():
    def do_global():
        global b4
        b4 = 10
        print(b4)
    do_global()
    print(b4)
add_b4()
print("b4 = %s" % b4)

def add_b5():
    def do_global():
        global b5
        b5 = 10
        print(b5)
    do_global()
    print(b5)
add_b5()
b5 = b5 + 30
print("b5 = %s" % b5)

def add_b6():
    b6 = 42
    def do_global():
        global b6
        b6 = 10
        print(b6)
    do_global()
    b6 = b6 + 5
    print(b)
add_b6()
b6 = b6 + 30
print("b6 = %s" % b6)
