#!/usr/bin/python3
"""
字典是另一种可变容器模型，且可存储任意类型对象
字典的每个键值(key=>value)对用冒号分割，每个对之间用逗号分割，整个字典包括在花括号中
键必须是唯一的
"""
aDict = {'Alice' : '2341', 'Beth' : '9102', 'Cecil' : '3258'}
print(aDict)
bDict = {'Name' : 'Runoob', 'Age' : 7, 'Class' : 'First'}
print('bDict["Name"]: ', bDict["Name"])
print('bDict["Age"]: ', bDict["Age"])
bDict['Age'] = 8
bDict['School'] = '菜鸟教程'
print(bDict)
del bDict['Age']
print(bDict)
"""
clear(...)
D.clear() -> None.  Remove all items from D.
"""
bDict.clear()
print(bDict)
del bDict
"""
字典值可以是任何的python对象，既可以是标准的对象，也可以是用户定义的，但键不行
两个重要的点需要记住:
1. 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2. 键必须不可变，所以用数字，字符串或元组充当，而用列表就不行
"""
cDict = {'Name' : 'Runoob', 'Age' : 7, 'Name' : '小菜鸟'}
print(cDict)
"""
copy(...)
D.copy() -> a shallow copy of D
"""
eDict = {'Name' : 'Runoob', 'Age' : 7, 'Name' : '小菜鸟', 'Score' : [98, 89]}
fDict = eDict.copy()
eDict['Score'][1] = 100
print(eDict)
print(fDict)
"""
fromkeys(iterable, value=None, /) method of builtins.type instance
Returns a new dict with keys from iterable and values equal to value.
"""
gDict = dict.fromkeys(['name', 'age', 'sex'])
print(gDict)
hDict = dict.fromkeys(['name', 'age', 'sex'], 10)
print(hDict)
"""
get(...)
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
setdefault(...)
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
"""
iDict = {'Name' : 'Runoob', 'Age' : 7}
print("Age的值为: %s" % iDict.get('Age'))
print("Sex的值为: %s" % iDict.get('Sex'))
print("Sex的值为: %s" % iDict.get('Sex', 'N/A'))
print("Sex的值为: %s" % iDict.setdefault('Sex', 'male'))
print(iDict)
"""
in操作符用于判断键是否存在于字典中，如果键在字典里返回true，否则返回false
而not in操作符正好相反，如果键在字典dict里返回false，否则返回true
"""
jDict = {'Name' : 'Runoob', 'Age' : 7}
if 'Age' in jDict:
    print('键Age存在')
else:
    print('键Age不存在')
if 'Sex' in jDict:
    print('键Sex存在')
else:
    print('键Sex不存在')
"""
dict.items()
返回可遍历的(key, value)元组数组
keys(...)
D.keys() -> a set-like object providing a view on D's keys
values(...)
D.values() -> an object providing a view on D's values
"""
kDict = {'Name' : 'Runoob', 'Age' : 7}
print(kDict.items())
print(kDict.keys())
print(kDict.values())
"""
update(...)
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]
"""
lDict = {'Name' : 'Runoob'}
print(lDict)
lDict.update(Age = 23, Home = 'Beijing')
print(lDict)
lDict.update({'School' : "NO.14", 'Class' : "NO.3"}, Age = 28, Home = 'Tianjing')
print(lDict)
lDict.update([('Fav', "football"), ('Sex', 'male')], Home = 'Nanjing')
print(lDict)
lDict.update((('height', 185), ('weight', "70kg")), Sex = 'female')
print(lDict)
"""
pop(...)
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised
popitem(...)随机删除
D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.
"""
mDict = {'Name' : 'Runoob', 'Age' : 25}
print(mDict.pop('Sex', 'Male'))
print(mDict.pop('Age', 23))
print(mDict)
nDict = {'Home': 'Nanjing', 'Sex': 'female', 'Name': 'Runoob', 'Age': 28}
print(nDict)
print(nDict.popitem())
print(nDict)
