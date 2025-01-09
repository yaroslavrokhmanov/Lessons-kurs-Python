# 1.Даны три переменные с числами:

tst1 = 2
tst2 = 4
tst3 = 6
# Сделайте функцию, которая в свои параметры будет принимать три числа и находить их сумму. Выведите на экран сумму заданных выше переменных.
def func(num1, num2, num3):
 return num1 + num2 + num3
result = func(tst1, tst2, tst3)
print(result) # 12

# 2.Даны функция func и переменная tst:

def func(lst):
	sum = 0
	
	for el in lst:
		sum += el
	
	return sum

tst = [1, 3, 6]
# С помощью функции найдите сумму элементов из переменной tst.
result = func(tst)
print(result) # 10