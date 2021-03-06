#!/usr/bin/python3
import sys
print('命令行参数如下: ')
#sys.argv是一个包含命令行参数的列表
for i in sys.argv:
    print(i)
#sys.path包含了一个Python解释器自动查找所需模块的路径的列表
print('\nPython的路径为: ', sys.path)
#想使用python源文件，只需在另一个源文件里执行import语句
#当解释器遇到import语句，如果模块在当前的搜索路径就会被导入
#搜索路径是一个解释器会先进行搜索的所有目录的列表
#一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块一遍又一遍地执行
#当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
#这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块
#这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径
#搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量
#若在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉
#了解了搜索路径的概念，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块
import support
support.print_func("Runoob")
import fibo
fibo.fib(1000)
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
print(fibo.fib2(100))
print("fibo.__name__ = ", fibo.__name__)
print("fibo.__doc__ = ", fibo.__doc__)
print("fibo.__file__ = ", fibo.__file__)
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
#如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
fib = fibo.fib
fib(500)
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
#Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
#这个声明不会把整个fibo模块导入到当前的命名空间中，她只会将fibo里的fib2函数引入进来
#把一个模块的所有内容全部导入到当前的命名空间中也是可行的，只需使用如下声明:
#from fibo import *
from fibo import fib2
print(fib2(5000))
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
#内置的函数dir()可以找到模块内定义的所有名称。以一个字符串列表的形式返回
print(dir(fibo))
print(dir(sys))
#如果没有给定参数，那么dir()函数会罗列出当前定义的所有名称
print(dir())
#模块sys，他内置在每一个Python解析器中。变脸sys.ps1和sys.ps2定义了主提示符和副提示符所对应的字符串
"""
包是一种管理python模块命名空间的形式，采用"点模块名称"
比如一个模块的名称是A.B，那么他表示一个包A中的子模块B
就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况
这样不同的作者都可以提供Numpy模块，或者是Python图形库
在导入一个包的时候，Python会根据sys.path中的目录来寻找这个包中包含的子目录
目录只有包含一个叫做__ini__.py的文件才会被认为是一个包
最简单的情况，放一个空的__init__.py就可以了。当然这个文件也可以包含一些初始化代码或者为__all__变量赋值
当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块(子包)，或者包里面定义的其他名称，比如函数，类，或者变量
当使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字
"""
