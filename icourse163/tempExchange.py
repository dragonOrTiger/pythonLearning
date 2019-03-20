#!/usr/bin/python3
'''
1.eval()评估函数
去掉参数最外侧引号，并执行余下语句的函数
'''
print(eval('1'))
print(eval('1 + 2'))
print(eval('"1 + 2"'))
eval('print("Hello World!")')
'''
2.print()格式化输出
print("转换后的温度是{:.2f}C".format(c))
{}表示槽，后续变量填充到槽中
{:.2f}表示将变量C填充到这个位置时，小数点后取2位
'''
tempStr = input("请输入带有符号的温度值:")
if tempStr[-1] in ['F', 'f']:
	c = (eval(tempStr[0:-1]) - 32) / 1.8
	print("转换后的温度是{:.2f}C".format(c))
elif tempStr[-1] in ['C', 'c']:
	f = 1.8 * eval(tempStr[0:-1]) + 32
	print("转换后的温度是{:.2f}F".format(f))
else:
	print("输入格式错误")
