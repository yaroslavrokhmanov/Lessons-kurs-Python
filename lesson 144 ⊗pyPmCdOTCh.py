# 1
# Пусть у вас есть переменная. Проверьте, является ли ее значение целым числом.
tst = 2024
if isinstance(tst, int):
	print('int') #int

# 2
# Узнайте, является ли заданная переменная числом с плавающей точкой.
tst = 9.99
if isinstance(tst, float):
	print('float') #float

# 3
# Проверьте, содержит ли переменная строчное значение.
tst = 'Poland'
if isinstance(tst, str):
	print('str') # str

# 4
# Проверьте, является ли заданная переменная словарем.
tst = {'a': 1, 'b': 2, 'c': 3}
if isinstance(tst, dict):
	print('dict') # dict

# 5
# Проверьте, является ли заданная переменная множеством.
tst = {1, 2, 3, 4, 5}
if isinstance(tst, set):
	print('set') # set

# 6
# Проверьте, является ли заданная переменная кортежем.
tst = (1, 2, 3, 4, 5)
if isinstance(tst, tuple):
	print('tuple') # tuple


# 7
# Проверьте, является ли заданная переменная списком.
tst = [1, 2, 3, 4, 5]
if isinstance(tst, list):
	print('list') # list
