#!/usr/bin/python3
'''
Python中的变量不需要声明，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
在Python中，变量就是变量，它没有类型，我们所说的“类型”是变量所指的内存中对象的类型
'''
counter = 100
miles = 1000.0
name = "runoob"
print(counter)
print(miles)
print(name)
'''
python中允许同时为多个变量赋值
'''
#创建一个整型对象，值为1,从后向前赋值，三个变量被赋予相同的数值
a = b = c = 1
print('a = ', a, ', b = ', b, ', c = ', c)
#两个整型对象1和2分配给变量a和b,字符串对象"runoob"分配给变量c
a, b, c = 1, 2, 'runoob'
print('a = ', a, ', b = ', b, ', c = ', c)
'''
Number数字
'''
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
a = 111
print(isinstance(a, int))
'''
isinstance和type的区别在于:
type()不会认为子类是一种父类类型
isinstance()会认为子类是一种父类类型
'''
class A:
	pass
class B(A):
	pass
print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
'''
当你指定一个值时，Number对象就会被创建，
您也可以使用del语句删除一些对象引用
del语句的语法是:
del var1[, var2[, var3[......,varN]]]
'''
'''
数值运算
2 / 4 除法得到一个浮点数
2 // 4 除法得到一个整数
2 ** 5 乘方
'''
print('5 + 4 = ', 5 + 4)
print('4.3 - 2 = ', 4.3 - 2)
print('3 * 7 = ', 3 * 7)
print('2 / 4 = ', 2 / 4)
print('2 // 4 = ', 2 // 4)
print('2 ** 5 = ', 2 ** 5)
two = 0b10110
eight = 0o26
ten  = 22
sixteen = 0x16
print("二进制的0b10110对应的八进制是:", oct(two))
print("二进制的0b10110对应的十进制是:", int(two))
print("二进制的0b10110对应的十六进制是:", hex(two))
print("八进制的0o26对应的二进制是:", bin(eight))
print("八进制的0o26对应的十进制是:", int(eight))
print("八进制的0o26对应的十六进制是:", hex(eight))
print("十进制的22对应的二进制是:", bin(ten))
print("十进制的22对应的八进制是:", oct(ten))
print("十进制的22对应的十六进制是:", hex(ten))
print("十六进制的0x16对应的二进制是:", bin(sixteen))
print("十六进制的0x16对应的八进制是:", oct(sixteen))
print("十六进制的0x16对应的十进制是:", int(sixteen))
"""
字符串
+是字符串的连接符，*表示复制当前字符串，紧跟的数字为复制的次数
"""
str = 'Runoob'
print("str: ", str)
print("str[0:-1]: ", str[0:-1])
print("str[0]: ", str[0])
print("str[2:5]: ", str[2:5])
print("str[2:]: ", str[2:])
print("str * 2: ", str * 2)
print("str + TEST: ", str + "TEST")
print("str[0::2]: ", str[0::2])
#Python使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个r,表示原始字符串
print('Ru\noob')
print(r'Ru\noob')
"""
List
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
列表是写在方括号[]之间，用逗号分隔开的元素列表
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
加号+是列表连接运算符，*是重复操作
与python字符串不一样的是，列表中的元素是可以改变的
"""
list = ['abcd', 786, 2.23, 'runoob', True, 1 + 2j, None]
print("list:", list)
print("list[0]:", list[0])
print("list[1:3]:", list[1:3])
print("list[2:]:", list[2:])
print("list * 2:", list * 2)
print("list + ['cdf', 'egad']:", list + ['cdf', 'egad'])
list[4] = False
print("list:", list)
print("list[0::2]:", list[0::2])
"""
元组 Tuple
与列表类似，不同之处在于元组的元素不能修改，元组写在小括号()里，元素之间用逗号隔开
元组的元素类型也可以不相同
其实，可以把字符串看作是一种特殊的元组
"""
tuple = ('abcd', 786, 2.23, 'runoob', True, 1 + 2j, None)
print("tuple:", tuple)
print("tuple[0]:", tuple[0])
print("tuple[1:3]:", tuple[1:3])
print("tuple[2:]:", tuple[2:])
print("tuple * 2:", tuple * 2)
print("tuple + ('cdf', 'egad'):", tuple + ('cdf', 'egad'))
print("tuple[0::2]:", tuple[0::2])
#构建包含0个或一个元素的元组比较特殊，所以有一些额外的语法规则
#一个元素，需要在元素后添加逗号
tup1 = ()
print("空元组: ", tup1)
tup2 = (20,)
print("包含一个元素的元组: ", tup2)
"""
集合(set)是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员
基本功能是进程成员关系测试和删除重复元素
可以用大括号{}或者set()函数创建集合
"""
setDemo = {'abcd', 786, 2.23, 'runoob', True, 1 + 2j, None, True, 786, 1 + 2j}
print("set: ", setDemo)
if 'Rose' in setDemo:
	print('Rose在set中')
else:
	print('Rose不在set中')
if 1 + 2j in setDemo:
    print('1 + 2j在set中')
else:
    print('1 + 2j不在set中')
a = set('abracadabra')
b = set('alacazam')
print("a集合: ", a)
print("b集合: ", b)
print("a与b的交集: ", a & b)
print("a与b的并集: ", a | b)
print("a - b: ", a - b)
print("b - a: ", b - a)
#a和b中不同时存在的元素
print("a ^ b: ", a ^ b)
#创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
emptySet = set()
emptyDic = {}
print("emptySet's type: ", type(emptySet))
print("emptyDic's type: ", type(emptyDic))
"""
Dictionary（字典）
字典是一种映射类型，字典用{}标识，它是一个无序的键(key):值(value)的集合
键(key)必须使用不可变类型
在同一个字典中，键(key)必须是唯一的。
"""
emptyDic['one'] = "1 - 菜鸟教程"
emptyDic[2] = "2 - 菜鸟工具"
print("字典emptyDic: ", emptyDic)
print("字典emptyDic中键'one'对应的值是: ", emptyDic['one'])
print("字典emptyDic中键2对应的值是: ", emptyDic[2])
print("字典emptyDic中所有键: ", emptyDic.keys())
print("字典emptyDic中所有值: ", emptyDic.values())
#构造函数dict()可以直接从键值对序列中构建字典如下:
dicDemo1 = dict([((1, 2), 1), ('Google', 2), ('Taobao', 3)])
print("字典dicDemo1: ", dicDemo1)
dicDemo2 = {x : x ** 2 for x in (2, 4, 6)}
print("字典dicDemo2: ", dicDemo2)
dicDemo3 = dict(Runoob = 1, Google = 2, Taobao = 3)
print("字典dicDemo3: ", dicDemo3)

