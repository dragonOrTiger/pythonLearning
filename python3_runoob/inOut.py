#!/usr/bin/python3
"""
eval(source, globals=None, locals=None, /)
Evaluate the given source in the context of globals and locals.
The source may be a string representing a Python expression or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping, defaulting to the current globals and locals.
If only globals is given, locals defaults to it.
globals()
Return the dictionary containing the current scope's global variables.
NOTE: Updates to this dictionary *will* affect name lookups in the current global scope and vice-versa.
locals()
Return a dictionary containing the current scope's local variables.
NOTE: Whether or not updates to this dictionary will affect name lookups in the local scope and vice-versa is *implementation dependent* and not covered by any backwards compatibility guarantees.
repr(obj, /)
Return the canonical string representation of the object.
For many object types, including most builtins, eval(repr(obj)) == obj.
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str
Create a new string object from the given object.
If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined) or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.s
"""
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
b = eval(a)
print(type(b))
print(b)
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
a = "{'a' : 1, 'b' : 2}"
print(type(a))
b = eval(a)
print(type(b))
print(b)
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
a = "([1,2], [3,4], [5,6], [7,8], [9,0])"
print(type(a))
b = eval(a)
print(type(b))
print(b)
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
x, y = 1, 1
num1 = eval("x + y")
print(num1)
def g():
    x, y = 2, 2
    num3 = eval("x + y")
    print(num3)
    print(globals())
    num2 = eval("x + y", globals())
    print(num2)
    print(locals())
    num4 = eval("x + y", locals())
    print(num4)
g()
print(globals())
print(locals())
print(globals() == locals())
print(globals() is locals())
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
print(eval("2+3"))
print(eval("a+b", {'a' : 8, 'b' : 9}))
print(eval("a+b", {'a' : 8, 'b' : 9}, {'a' : 18, 'b' : 40}))
print(eval('2==3'))
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
print(repr('Hello Runoob!\n'))
print(eval(repr('Hello Runoob!\n')) == 'Hello Runoob!\n')
print(type(str(1/7)))
x = 10 * 3.25
y = 200 * 200
print('x的值为: ' + repr(x) + ', y的值为: ' + repr(y) + '...')
#repr()函数可以转义字符串中的特殊字符
print("hello, runoob\n")
print(repr("hello, runoob\n"))
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
    print(repr(x * x * x).rjust(4))
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
for x in range(1, 11):
    print('{0:2d} {1:3} {2:4d}'.format(x, x**2, x**3))
"""
format(...)
S.format(*args, **kwargs) -> str
Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
括号及其里面的字符(称作格式化字段)将会被format()中的参数替换
"""
print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
print('{}网址: "{}!"'.format('菜鸟教程', 'www.runoob.com'))
#在括号中的数字用于指向传入对象在format()中的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
#如果在format()中使用了关键字参数，那么他们的值会指向使用该名字的参数
print('{name}网址: {site}'.format(name='菜鸟教程', site='www.runoob.com'))
#位置和关键字参数可以任意的结合
print('站点列表 {0}, {1}, {other}'.format('Google', 'Runoob', other = 'Taobao'))
'''
ascii(obj, /)
Return an ASCII-only representation of an object.
As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \\x, \\u or \\U escapes.
'''
#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('{!a}'.format("hello, 欢迎来到菜鸟教程"))
#可选项':'和格式标识符可以跟着字段名。这就允许对值进行更好的格式化
import math
print("常量PI的值近似为 {0:.3f}。".format(math.pi))
#在':'后传入一个整数，可以保证該域至少有这么多的宽度，用于美化表格时很有用
table = {'Google' : 1, 'Runoob' : 2, 'Taobao' : 3}
for name, number in table.items():
	print('{0:10} ==> {1:10d}'.format(name, number))
#如果你有一个很长的格式化字符串，而你不想将它们分开，那么在格式化时通过变量名而非位置会是很好的事情
#最简单的就是传入一个字典，然后使用方括号来访问键值
table = {'Google' : 1, 'Runoob' : 2, 'Taobao' : 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:b}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:b}'.format(**table))
#第一个参数为要打开的文件名
#第二个参数描述文件如何使用的字符。
#mode可以是'r'如果文件只读，'w'只用于写(如果存在同名文件将被删除)，
#'a'用于追加文件内容，所写的任何数据都会被自动增加到末尾，'r+'同时用于读写。
#mode参数是可选的，'r'将是默认值
#fw.write(string)将string写入到文件中，然后返回写入的字符数
#如果要写入一些不是字符串的东西，那么将需要先进行转换
fw = open('foo.txt', 'w')
value = ('www.runoob.com', 14)
s = str(value)
fw.write(s)
fw.close()
fw = open("foo.txt", 'w')
print(type(fw))
num = fw.write("Python是一个非常好的语言。\n是的，的确非常好!!\n")
print(num, "个字符")
fw.close()
#为了读取一个文件的内容，调用fr.read(size),这将读取一定数目的数据，然后作为字符串或字节对象返回
#size是一个可选的数字类型的参数。当size被忽略了或者为负数，那么该文件的所有内容读将被读取并且返回
fr = open("foo.txt", 'r')
print(type(fr))
content = fr.read()
print(content)
fr.close()
#f.readline()会从文件中读取单独的一行，换行符为'\n'。f.readline()如果返回一个空字符串，说明已经读取到最后一行
frl = open('foo.txt', 'r')
#f.tell()返回文件对象当前所处的位置，他是从文件开头开始算起的字节数
line = frl.readline()
print("文件对象当前所处的位置: ", frl.tell())
print(line)
frl.close()
#f.readlines()将返回该文件中包含的所有行
#如果设置可选参数sizehint,则读取指定长度的字节，并且将这些字节按行分割
frls = open('foo.txt', 'r')
lines = frls.readlines()
print(type(lines))
print(lines)
frls.close()
fi = open('foo.txt', 'r')
for line in fi:
	print(line, end='')
fi.close()
'''
f.seek()
如果想要改变文件当前的位置，可以使用f.seek(offset, from_what)函数
from_what的值，如果是0表示开头，如果是1表示当前位置，2表示文件的结尾，例如:
seek(x, 0): 从起始位置即文件首行首字符开始移动x个字符
seek(x, 1): 表示从当前位置往后移动x个字符
seek(-x, 2): 表示从文件的末尾往前移动x个字符
from_what值默认为0,即文件开头
'''
f = open('seekDemo.txt', 'wb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
print(f.seek(-3, 1))
print(f.read(1))
#当处理完一个文件后，调用f.close()来关闭文件并释放系统恶毒资源，如果尝试再调用该文件，则会跑出异常
#当处理一个文件对象时，使用with关键字是非常好的方式。在结束后，他会帮你正确的关闭文件，而且写起来也比try-finally要简短
with open('foo.txt', 'r') as f:
	print(f.read())
print('f has been closed? ', f.closed)
'''
python的pickle模块实现了基本的数据序列和反序列化
通过pickle模块的序列化操作我们能够将程序中的运行信息保存到文件中去，永久存储
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
基本接口:
pickle.dump(obj, file, [,protocol])
x = pickle.load(file)
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
dump(obj, file, protocol=None, *, fix_imports=True)
Write a pickled representation of obj to the open file object file.
This is equivalent to ``Pickler(file, protocol).dump(obj)``, but may be more efficient.
The optional *protocol* argument tells the pickler to use the given protocol supported protocols are 0, 1, 2, 3 and 4.  The default protocol is 3; a backward-incompatible protocol designed for Python 3.
Specifying a negative protocol version selects the highest protocol version supported.  The higher the protocol used, the more recent the version of Python needed to read the pickle produced.
The *file* argument must have a write() method that accepts a single bytes argument.  It can thus be a file object opened for binary writing, an io.BytesIO instance, or any other custom object that meets this interface.
If *fix_imports* is True and protocol is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
load(file, *, fix_imports=True, encoding='ASCII', errors='strict')
Read and return an object from the pickle data stored in a file.
This is equivalent to ``Unpickler(file).load()``, but may be more efficient.
The protocol version of the pickle is detected automatically, so no protocol argument is needed.  Bytes past the pickled object's representation are ignored.
The argument *file* must have two methods, a read() method that takes an integer argument, and a readline() method that requires no arguments.  Both methods should return bytes.  Thus *file* can be a binary file object opened for reading, an io.BytesIO object, or any other custom object that meets this interface.
Optional keyword arguments are *fix_imports*, *encoding* and *errors*, which are used to control compatibility support for pickle stream generated by Python 2.  If *fix_imports* is True, pickle will try to map the old Python 2 names to the new names used in Python 3.  The *encoding* and *errors* tell pickle how to decode 8-bit string instances pickled by Python 2; these default to 'ASCII' and 'strict', respectively.  The *encoding* can be 'bytes' to read these 8-bit string instances as bytes objects.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False)
Pretty-print a Python object to a stream [default is sys.stdout].
'''
import pickle
import pprint
dictDemo = {'a' : [1, 2.0, 3, 4+6j],
	'b' : ('string',u'Unicode string'),
	'c' : None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
pickle.dump(dictDemo, output)
pickle.dump(selfref_list, output)
output.close()
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
