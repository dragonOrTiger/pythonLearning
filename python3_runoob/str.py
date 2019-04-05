#!/usr/bin/python3
#%c 格式化字符及其ASCII码
#%S 格式化字符串
print('字符%c\t字符串%s' % ('a', 'Hello'))
print('字符%c\t字符串%s' % (98, 'Hello'))
# %d 格式化整数
# %u 格式化无符号整数
# %o 格式化无符号八进制数
# %x 格式化无符号十六进制数
# %X 格式化无符号十六进制数
print('整数%d\t无符号整型%u\t无符号八进制数%o\t无符号十六进制数%x\t无符号十六进制数%X' % (25, 56, 0o57, 0xA5, 0xB9))
print('整数%d\t无符号整型%u\t无符号八进制数%o\t无符号十六进制数%x\t无符号十六进制数%X' % (25, 56, 0o57, 0xA5, 45))
print('整数%d\t无符号整型%u\t无符号八进制数%o\t无符号十六进制数%x\t无符号十六进制数%X' % (25, 56, 0o57, 0xA5, -45))

# %f 格式化浮点数
# %e 用科学计数法格式化浮点数
# %E 用科学计数法格式化浮点数
print('浮点数%f\t科学计数法%e\t科学计数法%E' % (2136, 2136.5, 2136.5))
# *定义宽度或者小数点精度
print("a%8db" % 45)
# -用作左对齐
print("a%-8db" % 45)
# 在正数前面显示空格
print("a% db" % 45)
# 在八进制数前面显示'0',在十六进制前面显示'0x'或'0X'
print("a%#ob" % 45)
print("a%#xb" % 45)
# + 在正数前面显示正号 +
print("a%+db" % 45)
# 0 显示的数字前面填充'0'而不是默认的空格
print("a%08db" % 45)
# % '%%'输出一个单一的%
print("a%d%%b" % 45)
print("a%8fb" % 4.5)
# m.n m是显示的最小总宽度， n是小数点后的位数
print("a%9.5fb" % 4.5)

"""
格式化字符串的函数str.format(), 它增强了字符串格式化的功能
基本语法是通过{}和:来代替以前的%
"""
#不设置指定位置，按照默认顺序
print("{} {}".format("hello", "world"))
#设置指定位置
print("{0} {1}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
#通过字典设置参数
site = {'name':"菜鸟教程", 'url':"www.runoob.com"}
print("网站名: {name}，地址: {url}".format(**site))
#通过列表索引设置参数
my_list = ["菜鸟教程", 'www.runoob.com']
print("网站名: {0[0]}，地址: {0[1]}".format(my_list))
#也可以向str.format()传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value为: {0.value}'.format(my_value)) #'0'是可选的

"""
str.format()格式化数字的多种方法
"""
import math
#保留小数点后2位
print('start{:.2f}end'.format(math.pi))
#带符号保留小数点后2位
print('start{:+.2f}end'.format(math.pi))
print('start{:+.2f}end'.format(-math.pi))
#不带小数，四舍五入
print('start{:.0f}end'.format(math.pi))
print('start{:.0f}end'.format(math.e))
#数字补零(填充左边，宽度为2)
print('start{:0>2d}end'.format(5))
#数字补零(填充右边，宽度为4)
print('start{:x<4d}end'.format(10))
#以逗号分隔的数字格式
print('start{:,}end'.format(100000000))
#百分比格式
print('start{:.2%}end'.format(0.25))
#指数记法
print('start{:.2e}end'.format(100000000))
#右对齐(默认，宽度为10)
#:后面带填充的字符，只能是一个字符，不指定则默认用空格填充
print('start{:10d}end'.format(13))
#左对齐(宽度为10)
print('start{:<10d}end'.format(13))
#剧中对齐(宽度为10)
print('start{:^10d}end'.format(13))
#b: 二进制；o: 八进制；d：十进制；x：十六进制
print('start{:b}end'.format(11))
print('start{:o}end'.format(11))
print('start{:x}end'.format(11))
print('start{:d}end'.format(0x11))
print('start{:#x}end'.format(11))
print('start{:#X}end'.format(11))
#我们可以使用大括号{}来转义大括号
print('{} 对应的位置是{{0}}'.format("runoob"))

"""
python三引号
三引号允许一个字符串跨多行，字符串中可以包含换行符，制表符，以及其他特殊字符
三引号让程序员从引号和特殊字符串的泥潭里解脱出来，自始至终保持一小块字符串的格式是所谓的所见即所得的格式
一个典型的用例是，当你需要一块HTML或SQL时，这时用字符串组合，特殊字符串的转义会非常的繁琐
"""
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

"""
python的字符串内建函数
1. S.capitalize() -> str
   Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.
2. S.lower() -> str
   Return a copy of the string S converted to lowercase.
3. S.upper() -> str
   Return a copy of S converted to uppercase.
4. S.swapcase() -> str
   Return a copy of S with uppercase characters converted to lowercase and vice versa
5. S.center(width[, fillchar]) -> str
   Return S centered in a string of length width. Padding is done using the specified fill character (default is a space)
6. S.count(sub[, start[, end]]) -> int
   Return the number of non-overlapping occurrences of substring sub in string S[start:end].  Optional arguments start and end are interpreted as in slice notation.
7. S.encode(encoding='utf-8', errors='strict') -> bytes
   Encode S using the codec registered for encoding. Default encoding is 'utf-8'. errors may be given to set a different error handling scheme. Default is 'strict' meaning that encoding errors raise a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.
8. decode(self, /, encoding='utf-8', errors='strict')
   Decode the bytes using the codec registered for encoding.
   encoding: The encoding with which to decode the bytes.
   errors: The error handling scheme to use for the handling of decoding errors. The default is 'strict' meaning that decoding errors raise a Other possible values are 'ignore' and 'replace' as well as any other name registered with codecs.register_error that can handle UnicodeDecodeErrors.
9. S.startswith(prefix[, start[, end]]) -> bool
   Return True if S starts with the specified prefix, False otherwise.
   With optional start, test S beginning at that position.
   With optional end, stop comparing S at that position.
   prefix can also be a tuple of strings to try.
10. S.endswith(suffix[, start[, end]]) -> bool
    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.
11. S.expandtabs(tabsize=8) -> str
    Return a copy of S where all tab characters are expanded using spaces.
    If tabsize is not given, a tab size of 8 characters is assumed.
12. S.find(sub[, start[, end]]) -> int
    Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
13. S.index(sub[, start[, end]]) -> int
    Like S.find() but raise ValueError when the substring is not found.
14. S.rfind(sub[, start[, end]]) -> int
    Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
    Optional arguments start and end are interpreted as in slice notation.
    Return -1 on failure.
15. S.rindex(sub[, start[, end]]) -> int
    Like S.rfind() but raise ValueError when the substring is not found.
16. S.isalnum() -> bool
    Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.
17. S.isalpha() -> bool
    Return True if all characters in S are alphabetic and there is at least one character in S, False otherwise.
18. S.isnumeric() -> bool
    Return True if there are only numeric characters in S, Return True if there are only numeric characters in S,
19. S.isdigit() -> bool
    Return True if all characters in S are digits and there is at least one character in S, False otherwise.
20. S.isdecimal() -> bool
    Return True if there are only decimal characters in S, False otherwise.
####isnumeric():
####    True: unicode数字，全角数字(双字节)， 罗马数字(Ⅷ), 汉字数字
####    False:无
####    Error:byte数字(单字节)
####
####isdigit():
####    True: unicode数字，全角数字(双字节), byte数字(单字节)
####    False:罗马数字(Ⅷ)， 汉字数字
####    Error:无
####
####isdecimal():
####    True: unicode数字，全角数字(双字节)
####    False:罗马数字(Ⅷ)， 汉字数字
####    Error:byte数字(单字节)
21. S.islower() -> bool
    Return True if all cased characters in S are lowercase and there is at least one cased character in S, False otherwise.
22. S.isupper() -> bool
    Return True if all cased characters in S are uppercase and there is at least one cased character in S, False otherwise.
23. S.isspace() -> bool
    Return True if all characters in S are whitespace and there is at least one character in S, False otherwise.
24. S.title() -> str
    Return a titlecased version of S, i.e. words start with title case characters, all remaining cased characters have lower case.
25. S.istitle() -> bool
    Return True if S is a titlecased string and there is at least one character in S, i.e. upper- and titlecase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.
26. S.join(iterable) -> str
    Return a string which is the concatenation of the strings in the iterable.  The separator between elements is S.
27. len(obj, /)
    Return the number of items in a container.
28. S.ljust(width[, fillchar]) -> str
    Return S left-justified in a Unicode string of length width. Padding is done using the specified fill character (default is a space).
29. S.rjust(width[, fillchar]) -> str
    Return S right-justified in a string of length width. Padding is Return S right-justified in a string of length width. done using the specified fill character (default is a space).
30. S.lstrip([chars]) -> str
    Return a copy of the string S with leading whitespace removed. If chars is given and not None, remove characters in chars instead.
31. S.rstrip([chars]) -> str
    Return a copy of the string S with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.
32. S.strip([chars]) -> str
    Return a copy of the string S with leading and trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.
33. maketrans(x, y=None, z=None, /)
    Return a translation table usable for str.translate().
    If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None.Character keys will be then converted to ordinals.
    If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y.
    If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
34. S.translate(table) -> str
    Return a copy of the string S in which each character has been mapped through the given translation table.
    The table must implement lookup/indexing via __getitem__, for instance a dictionary or list, mapping Unicode ordinals to Unicode ordinals, strings, or None. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.
35. max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    With a single iterable argument, return its biggest item.
    The default keyword-only argument specifies an object to return if the provided iterable is empty.
    With two or more arguments, return the largest argument.
36. min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
    With a single iterable argument, return its smallest item.
    The default keyword-only argument specifies an object to return if the provided iterable is empty.
    With two or more arguments, return the smallest argument.
37. S.replace(old, new[, count]) -> str
    Return a copy of S with all occurrences of substring old replaced by new.
    If the optional argument count is given, only the first count occurrences are replaced.
38. S.split(sep=None, maxsplit=-1) -> list of strings
    Return a list of the words in S, using sep as the delimiter string.
    If maxsplit is given, at most maxsplit splits are done.
    If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result.
39. S.splitlines([keepends]) -> list of strings
    Return a list of the lines in S, breaking at line boundaries.
    Line breaks are not included in the resulting list unless keepends is given and true.
40. S.zfill(width) -> str
    Pad a numeric string S with zeros on the left, to fill a field of the specified width. The string S is never truncated.
"""
print("this is string example from runoob....wow!!!".capitalize())
print("HELLO RUNOOB".lower())
print("hello runoob".upper())
print("Hello Runoob".swapcase())
print("Hello Runoob".center(50))
print("Hello Runoob".center(50, '|'))
print("ababa".count('ab', 1, 3))
print("ababa".count('ab'))
print("ababa".count('aba'))
print("菜鸟教程UTF-8编码为: ", "菜鸟教程".encode())
print("菜鸟教程GBK编码为: ", "菜鸟教程".encode('GBK'))
print("菜鸟教程UTF-8编码再经过UTF-8解码为: ", "菜鸟教程".encode().decode())
print("菜鸟教程GBK编码再经过GBK解码为: ", "菜鸟教程".encode('GBK').decode('GBK'))
print("abdfefghijklmn".startswith('a'))
print("abdfefghijklmn".startswith('d',2))
print("abdfefghijklmn".startswith(('c', 'd'),2))
print("abdfefghijklmn".endswith('n'))
print("abdfefghijklmn".endswith('d',0, 3))
print("abdfefghijklmn".endswith(('c', 'd'),0, 3))
print("abdfefghijklmnopqrstuvwxyz")
print("\tabcdefgh\tdf".expandtabs())
print("\tabcdefgh\tdf".expandtabs(2))
print("ababab".find('ab', 1))
print("ababab".find('abd', 1))
print("ababab".index('ab', 1))
print("a2b3１cIVX四五".isalnum())
print("a2b3１cIVX四五^".isalnum())
print("abcIVX".isalpha())
print("a2b3cIVX".isalpha())
print("Ⅷ１23四十五".isnumeric())
print("１23".isdigit())
print("23".isdecimal())
print("a2b3cIVX".isdecimal())
print("hello".islower())
print("HELLO".islower())
print("HELLO".isupper())
print("hello".isupper())
print(" \t \r \n".isspace())
print("hello runoob".title())
print("Hello Runoob".istitle())
print(" ".join(["Hello", "Runoob"]))
print(len("asdfghjklqwertyuiopzxcvbnm"))
print("asdfgh".ljust(26, "$"))
print("asdfgh".rjust(26, "^"))
print("asasasasdfgh".lstrip("as"))
print("    fgh".lstrip())
print("dfghasasasas".rstrip("as"))
print("fgh    ".rstrip())
table = str.maketrans({65 : '大写A', 66 : 98, 68 : None})
print("ABD".translate(table))
table = str.maketrans({'A' : '大写A', 'B' : 98, 'D' : None})
print("ABD".translate(table))
table = str.maketrans('AB', 'ab')
print("ABD".translate(table))
table = str.maketrans('AB', 'ab', 'D')
print("ABD".translate(table))
print(max("1qaz@WSX"))
print(max(['a', 'B']))
print(max(('a', 'B')))
print(max('a', 'B', 'C', 'E'))
print(min("1qaz@WSX"))
print(min(['a', 'B']))
print(min(('a', 'B')))
print(min('a', 'B', 'C', 'E'))
