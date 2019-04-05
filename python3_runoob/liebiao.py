#!/usr/bin/python3
"""
序列都可以进行的操作包括索引，切片，加，乘，检查成员
列表的数据项不需要有相同的类型
"""
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print('list1[0]: ', list1[0])
print('list2[1:5]: ', list2[1:5])
print('list1的第三个元素为: ', list1[2])
list1[2] = 2001
print('list1修改后的第三个元素为: ', list1[2])
print('原始列表: ', list1)
del list1[2]
print('删除第三个元素后list1: ', list1)
print('list2的长度: ', len(list2))
print(list1 + list2)
print(list1 * 4)
print('list1包含元素"Google"?', "Google" in list1)
for x in list1:
    print(x, end=" ")
print()
"""
list(seq)用于将元组或字符串转换为列表
seq: 要转换为列表的元组或字符串
"""
aTuple = (123, 'Google', 'Runoob', 'Taobao')
print(list(aTuple))
str1 = 'Hello World'
print(list(str1))
"""
append(...)
L.append(object) -> None -- append object to end
"""
aList = list(range(1,5))
aList.append([7, 9, 85])
print(aList)
bList = list(range(1,5))
bList.append(7)
print(bList)
"""
count(...)
L.count(value) -> integer -- return number of occurrences of value
"""
cList = [123, 'Google', 'Runoob', 'Taobao', 'Google', 'Runoob']
print(cList.count('Google'))
print(cList.count('Goofle'))
"""
extend(...)
L.extend(iterable) -> None -- extend list by appending elements from the iterable
"""
dList = list(range(1,5))
dList.extend([7, 9, 85])
print(dList)
"""
index(...)
L.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
"""
eList = ['Google', 2019, 3.14]
print(eList.index(2019))
print(eList.index(2019.0))
"""
insert(...)
L.insert(index, object) -- insert object before index
"""
fList = ['Google', 2019, 3.14]
fList.insert(2, [1, 2])
print(fList)
"""
pop(...)
L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.
"""
gList = ['Google', 2019, 3.14]
gList.pop(1)
print(gList)
"""
remove(...)
L.remove(value) -> None -- remove first occurrence of value.
Raises ValueError if the value is not present.
"""
hList = ['Google', 2019, 3.14, 'Google']
hList.remove("Google")
print(hList)
"""
reverse(...)
L.reverse() -- reverse *IN PLACE*
"""
lList = ['Google', 2019, 3.14]
lList.reverse()
print(lList)
"""
sort(...)
L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
"""
mList = ["Google", "Facebook", "Runoob", "Taobao"]
mList.sort()
print(mList)
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key = takeSecond)
print(random)
"""
clear(...)
L.clear() -> None -- remove all items from L
"""
nList = ["Google", "Facebook", "Runoob", "Taobao"]
print(nList)
nList.clear()
print(nList)
"""
copy(...)
L.copy() -> list -- a shallow copy of L
"""
nList = ["Google", "Facebook", "Runoob", "Taobao"]
oList = nList.copy()
print(oList)
