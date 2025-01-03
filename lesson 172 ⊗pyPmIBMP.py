# 1.Даны два числа:
num1 = 5
num2 = 4
# Возведите первое число в степень второго.
import math
print(math.pow(num1, num2))

# 2.Дан словарь:
dct = {
	2: 4,
	3: 2,
	5: 4
}
# Возведите каждый ключ в степень значения, чтобы получить следующий результат:
# 16.0
# 9.0
# 625.0

for key in dct:
    print(math.pow(key, dct[key])) #4.0

# 3.Дано число:
num = 16
# Найдите квадратный корень из этого числа.
print(math.sqrt(num))

# 4.Дан список:
lst = [2, 3, 4]
# Найдите квадратный корень из суммы чисел данного списка.
sum_num = sum(lst)
print(math.sqrt(sum_num)) #3.0

