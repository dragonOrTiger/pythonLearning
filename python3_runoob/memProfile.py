#!/usr/bin/python3
"""
memory_profiler是监控python进程的神器，它可以分析出每一行代码所增减的内存状况。
它的原理是在代码运行过程中每0.1S统计一次内存，并生成统计图。
前提: 安装memory_profiler和psutil(psutil主要用于提高memory_profiler的性能，建议安装)(可使用pip直接安装)
具体运行方式如下: (在待检测代码所在目录中打开命令行运行如下代码)
mprof run xxx.py
结果会生成一个.dat文件
mprof plot
使用该命令以图片的形式展示出来

另外，还可以执行以下命令来检测:
python -m memory_profiler xxx.py
"""
from memory_profiler import profile
import datetime

def listN(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums
@profile
def listSum():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    a = listN(20000000)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    suma = sum(a)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(suma)

def seriesGenerator(n):
    num = 0
    while num < n:
        yield num
        num += 1
    
@profile
def generatorSum():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    func = seriesGenerator(20000000)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    suma = sum(func)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(suma)

class naturalInt(object):
    def __init__(self, n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()
@profile
def naturalIntSum():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    a = naturalInt(20000000)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    suma = sum(a)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(suma)
    
if __name__ == "__main__":
    generatorSum()
    listSum()
    naturalIntSum()
