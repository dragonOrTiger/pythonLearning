#!/usr/bin/python3
try:
    print("这是try block")
    1 / 0
except ZeroDivisionError as e:
    print(e)
    print("除树不能为0!!!")
finally:
    print("这是finally block")
print("******************************")
try:
    print("这是try block")
    raise AssertionError("Assertion 1 == 2 Error")
except AssertionError as e:
    print(e)
    print("断言失败!!!")
finally:
    print("这是finally block")
print("******************************")
#加入traceback，会打印出详细的错误信息
import traceback
try:
    print("这是try block")
    1 / 0
except ZeroDivisionError as e:
    print(e)
    print("除树不能为0!!!")
    traceback.print_exc()
finally:
    print("这是finally block")
print("******************************")
'''
如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，
异常处理完毕,控制流就通过整个try语句(除非在处理异常时又引发新的异常)
如果在try后的语句里发生了异常，却没有匹配的except子句，
异常将被递交到上层的try，或者到程序的最上层(这样将结束程序，并打印缺省的出错信息)
如果在try子句执行时没有发生异常，python将执行else语句后的语句(如果有else的话)
然后控制流通过整个try语句
'''
try:
    print("这是try block")
    1 / 0
except ZeroDivisionError as e:
    print(e)
    print("除树不能为0!!!")
    traceback.print_exc()
else:
    print('没有异常抛出')
finally:
    print("这是finally block")
print("******************************")
