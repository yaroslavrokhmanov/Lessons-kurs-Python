# 1.Каким будет результат выполнения следующего кода:

def func(num1, num2, *args):
	return sum(args) + (num1 * num2)
	
print(func(10, 5, 1, 2, 3)) # 56