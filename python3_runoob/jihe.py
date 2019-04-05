#!/usr/bin/python3
"""
集合(set)是一个无序的不重复元素序列
可以使用大括号或者set()函数创建集合
注意: 创建一个空集合必须用set()而不是{}, 因为{}是用来创建一个空字典。
"""
aSet = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(aSet)
print("'apple' in aSet?", 'apple' in aSet)
"""
两个集合间的运算
a - b   集合a中包含而集合b中不包含的元素
a | b   集合a与集合b的并集
a & b   集合a与集合b的交集
a ^ b   不同时包含于a和b的元素
"""
bSet = set('abracadabra')
cSet = set('alacazm')
print(bSet)
print(cSet)
print("bSet - cSet = ", bSet - cSet)
print("cSet - bSet = ", cSet - bSet)
print("bSet和cSet的交集 = ", bSet & cSet)
print("bSet和cSet的并集 = ", bSet | cSet)
print("bSet ^ cSet = ", bSet ^ cSet)
dSet = {x for x in 'abracadabra' if x not in 'abc'}
print(dSet)
"""
add(...)
Add an element to a set.
This has no effect if the element is already present.
"""
fSet = {'Google', 'Runoob', 'Taobao'}
fSet.add('Facebook')
print(fSet)
"""
update(...)
Update a set with the union of itself and others.
参数可以是列表，元组，字典等
"""
gSet = {'Google', 'Runoob', 'Taobao'}
print(gSet)
gSet.update({3, 2}, [54, 78])
print(gSet)
gSet.update({3, 2}, [54, 78], {'Name' : 'XiaoMing'})
print(gSet)
"""
remove(...)
Remove an element from a set; it must be a member.
If the element is not a member, raise a KeyError.
discard(...)
Remove an element from a set if it is a member.
If the element is not a member, do nothing.
pop(...)
Remove and return an arbitrary set element.
Raises KeyError if the set is empty.
"""
hSet = {'Google', 'Runoob', 'Taobao'}
print(hSet)
hSet.remove('Google')
print(hSet)
hSet.discard('Facebook')
print(hSet)
hSet.discard('Runoob')
print(hSet)
iSet = {'Google', 'Runoob', 'Taobao'}
print(iSet)
iSet.pop()
print(iSet)
print(len(iSet))
iSet.clear()
print(iSet)
jSet = set(("Google", "Runoob", "Taobao"))
print("'Google' in jSet?", 'Google' in jSet)
print("'Facebook' in jSet?", 'Facebook' in jSet)
"""
copy(...)
Return a shallow copy of a set.
集合中的元素必须是可hash的，即不可变的数据类型
"""
kSet = jSet.copy();
print(kSet)
"""
difference(...)
Return the difference of two or more sets as a new set.
(i.e. all elements that are in this set but not the others.)
difference_update(...)
Remove all elements of another set from this set.
"""
print(set("Google").difference(set("Facebook")))
print(set("Google").difference(set("Facebook"), set("hello")))
lSet = set("Google")
lSet.difference_update(set("Facebook"), set("hello"))
print(lSet)
"""
intersection(...)
Return the intersection of two sets as a new set.
(i.e. all elements that are in both sets.)
intersection_update(...)
Update a set with the intersection of itself and another
"""
print(set("Google").intersection("Runoob"))
print(set("Google").intersection(set("adghaio"), set("Runoob")))
mSet = set("Google")
print(mSet.intersection_update("Runoob"))
print(mSet)
"""
isdisjoint(...)
Return True if two sets have a null intersection.
"""
print(set("Google").isdisjoint(set("Runoob")))
print(set("Google").isdisjoint(set("banana")))
"""
issubset(...)
Report whether another set contains this set.
issuperset(...)
Report whether this set contains another set.
"""
print(set("Google").issubset(set("Hello, Gao gao")))
print(set("Google").issubset(set("Hello, World")))
print(set("Hello, Gao gao").issuperset(set("Google")))
print(set("Hello, World").issuperset(set("Google")))
"""
symmetric_difference(...)
Return the symmetric difference of two sets as a new set.
(i.e. all elements that are in exactly one of the sets.)
symmetric_difference_update(...)
Update a set with the symmetric difference of itself and another.
"""
print(set("Google").symmetric_difference(set("Hello World")))
nSet = set('Google')
nSet.symmetric_difference_update(set("Hello World"))
print(nSet)
"""
union(...)
Return the union of sets as a new set.
(i.e. all elements that are in either set.)
"""
print(set("Google").union(set("adghaio"), set("Runoob")))
