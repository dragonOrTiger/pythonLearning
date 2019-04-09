#!/usr/bin/python3
from memory_profiler import profile
import datetime
def fibo(n):
    a, b, counter, res = 0, 1, 0, []
    while counter < n:
        res.append(b)
        counter += 1
        a, b = b, a +b
    return res
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while counter < n:
        yield b
        counter += 1
        a, b = b, a +b
@profile
def outFibo():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    fun1 = fibo(10000)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for x in fun1:
        print(x)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
@profile
def outFibonacci():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    fun2 = fibonacci(10000)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for x in fun2:
        print(x)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
if __name__ == "__main__":
    outFibo()
    outFibonacci()
