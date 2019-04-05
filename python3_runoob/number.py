#!/usr/bin/python3
"""
Python数字数据类型用于存储数值。
数据类型是不允许改变的，这就意味着如果改变数字数据类型的值，将重新分配内存空间。
"""
var = 1
print("var = ", var, "; id(var) = ", id(var))
var = 2
print("var = ", var, "; id(var) = ", id(var))
"""
Python支持3种不同的数值类型:
整型: python3的整型是没有限制大小的，可以当作Long类型使用。所以python3没有python2的Long型
浮点型: 可以使用科学计数法来表示。(2.5e2 = 2.5 * 10 ** 2 = 250)
复数: 可以用a + bj或者complex(a, b)表示，复数的实部和虚部都是浮点型
"""
print("2.5e2 = ", 2.5e2)
print("1 + 2j的实部是: ", (1 + 2j).real)
print("1 + 2j的实部是: ", (1 + 2j).imag)
print("1 + 2j的模是: ", abs(1 + 2j))

import math
print("pi = ", math.pi)
print("e = ", math.e)

#有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
print("int(2.5) = ", int(2.5))
print("float(2) = ", float(2))
print("complex(2) = ", complex(2))
print("complex(2.5) = ", complex(2.5))

#//得到的并不一定是整数类型的数，它与分母分子的数据类型有关系
print("7 // 2 = ", 7 // 2)
print("7.0 // 2 = ", 7.0 // 2)
print("7 // 2.0 = ", 7 // 2.0)

#交互模式中，最后被输出的表达式结果被赋值给变量_

"""
abs(x)与math.fabs(x)的区别:
abs(x): Return the absolute value of the argument.
math.fabsx(): Return the absolute value of the float x.
所以math.fabs(x)只适用于float和interger类型，而abs(x)也适用于复数
"""
print("-1的模是: ", abs(-1))
print("-1.3232的模是: ", abs(-1.3232))
print("1+1.0j的模是: ", abs(1+1.0j))
print("-1的模是: ", math.fabs(-1))
print("-1.3232的模是: ", math.fabs(-1.3232))

#ceil(x): Return the ceiling of x as an Integral. This is the smallest integer >= x.
print("ceil(-1.3232) = ", math.ceil(-1.3232))
print("ceil(1.3232) = ", math.ceil(1.3232))

#exp(): Return e raised to the power of x. e**x
print("e ** 0 = ", math.exp(0))
print("e ** 2 = ", math.exp(2))

#floor(): Return the floor of x as an Integral. This is the largest integer <= x.
print("floor(-1.3232) = ", math.floor(-1.3232))
print("floor(1.3232) = ", math.floor(1.3232))

#log(x[, base]): Return the logarithm of x to the given base. If the base not specified, returns the natural logarithm (base e) of x.
#log10(x): Return the base 10 logarithm of x.
print("log(x) = ", math.log(10))
print("log(1) = ", math.log(1))
print("log(8, 2) = ", math.log(8, 2))
print("log10(1) = ", math.log10(1))
print("log10(1000) = ", math.log10(1000))

#max(iterable, *[, default=obj, key=func]) -> value
#max(arg1, arg2, *args, *[, key=func]) -> value
#With a single iterable argument, return its biggest item. The default keyword-only argument specifies an object to return if the provided iterable is empty.
#With two or more arguments, return the largest argument.
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print("if the provided iterable is empty, return a", max([], default='a'))

#min(iterable, *[, default=obj, key=func]) -> value
#min(arg1, arg2, *args, *[, key=func]) -> value
#With a single iterable argument, return its smallest item. The default keyword-only argument specifies an object to return if the provided iterable is empty.
#With two or more arguments, return the smallest argument.
print ("min(80, 100, 1000) : ", min(80, 100, 1000))
print("if the provided iterable is empty, return a", min([], default='a'))

#Return the fractional and integer parts of x.  Both results carry the sign of x and are floats.
print ("-1.2的(小数部分，整数部分)是: ", math.modf(-1.2))

#pow(x, y, z=None, /)
#Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
#Some types, such as ints, are able to use a more efficient algorithm when invoked using the three argument form.
#could return int type
print("pow(2, 4) = ", pow(2, 4))
print("pow(2, 4, 6) = ", pow(2, 4, 6))

#math.pow(x, y)
#Return x**y (x to the power of y). return float type
print("math.pow(2, 4) = ", math.pow(2, 4))

#round(number[, ndigits]) -> number
#Round a number to a given precision in decimal digits (default 0 digits). This returns an int when called with one argument, otherwise the same type as the number. ndigits may be negative
print("round(22.42) = ", round(22.42))
print("round(22.42) = ", round(22.42, 1))
print("round(22.42) = ", round(22.42, -1))

#sqrt(x)
#Return the square root of x.
print("sqrt(2) = ", math.sqrt(2))

import random
#random.choice(seq)
#Choose a random element from a non-empty sequence.
print("random.choice(range(20)) = ", random.choice(range(20)))

#randrange(start, stop=None, step=1, _int=<class 'int'>)
#Choose a random item from range(start, stop[, step]).
print("random.randrange(1, 10, 2) = ", random.randrange(1, 10, 2))

#random() -> x in the interval [0, 1)
print("random.random() = ", random.random())

#shuffle(x, random=None)
#Shuffle list x in place, and return None.
#Optional argument random is a 0-argument function returning a random float in [0.0, 1.0); if it is the default None, the     standard random.random will be used.
listDemo = list(range(0, 20))
print("random.shuffle(listDemo) = ", random.shuffle(listDemo))
print("随机排序后的listDemo是: = ", listDemo)

#uniform(a, b)
#Get a random number in the range [a, b) or [a, b] depending on rounding.
print("random.uniform(3.5, 5.5) = ", random.uniform(3.5, 5.5))

#math.sin(): Return the sine of x (measured in radians).
#math.cos(): Return the cosine of x (measured in radians).
#math.tan(): Return the tangent of x (measured in radians).
#math.asin(): Return the arc sine (measured in radians) of x
#math.acos(): Return the arc cosine (measured in radians) of x.
#math.atan(): Return the arc tangent (measured in radians) of x.
#math.atan2(x,y): Return the arc tangent (measured in radians) of y/x. Unlike atan(y/x), the signs of both x and y are considered.
#math.degrees(): Convert angle x from radians to degrees.
#math.radians(): Convert angle x from degrees to radians.
#math.hypot(x, y): Return the Euclidean distance, sqrt(x*x + y*y)

print("math.sin(math.pi / 6) = ", math.sin(math.pi / 6))
print("math.cos(math.pi / 6) = ", math.cos(math.pi / 6))
print("math.asin(0.5) = ", math.asin(0.5))
print("math.acos(math.sqrt(3) / 2) = ", math.acos(math.sqrt(3) / 2))
print("math.tan(math.pi / 4) = ", math.tan(math.pi / 4))
print("math.tan(math.pi / 2) = ", math.tan(math.pi / 2))
print("math.atan(1) = ", math.atan(1))
print("math.atan(1.633123935319537e+16) = ", math.atan(1.633123935319537e+16))
print("pi弧度是:", math.degrees(math.pi))
print("180度是多少弧度？: ", math.radians(180))
print("(1, 2)距离原点的距离: ", math.hypot(1, 2))
