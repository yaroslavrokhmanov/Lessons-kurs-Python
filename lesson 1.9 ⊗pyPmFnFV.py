# 1.Каким будет результат выполнения следующего кода:

def func():
	print('hello, user!')

greet = func
print(greet) # <function func at 0x000001A33A6AD080>

# 2.Каким будет результат выполнения следующего кода:

def getSum(num1, num2):
	res = num1 + num2
	return res

func = getSum
print(func(2, 3)) # 5