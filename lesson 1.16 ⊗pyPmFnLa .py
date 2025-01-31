# 1.Перепишите следующий код через лямбда-функцию:
# def func(num, clb):
# 	return clb(num)
# def clb(num):
# 	return num + 1
# print( func(2, clb) )

def func(num, clb):
	return clb(num)
	
print( func(2, lambda num: num + 1) ) # 3

# 2.Перепишите следующий код через лямбда-функцию:
def func(num, clb1, clb2):
	return (clb1(num), clb2(num))
print( func(2, lambda num: num + 1, lambda num: num - 1) ) # (3, 1)

# 3.Перепишите следующий код через лямбда-функцию:
def func(num1, num2, clb):
	res = clb(num1) + num2
	return res
print(func(2, 6, lambda num: num ** 3)) # 14

