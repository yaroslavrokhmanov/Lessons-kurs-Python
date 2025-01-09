# 1.Сделайте функцию, которая будет возводить число в квадрат и функцию для получения куба числа. Также с их помощью создайте функцию, чтобы вывести на экран куб квадрата числа.
def square(num):
	return num ** 2
	
def cube(num):
	return num ** 3

def cube_square(num):
	return cube(square(num))

res = cube_square(2)

print(res) # 64

# 2.Сделайте функцию, которая будет проверять тип переменной и если переменная является строкой, то выведет ее с заглавной буквы. Также создайте функцию, которая будет приветствовать пользователя по имени. Вложите в нее первую функцию так, чтобы имя всегда выводилось с заглавной буквы

def func(el):
	if (el, str):
		return el.capitalize()
	else:
		return el

def func1(name):
	name = func(name)
	return 'Hello ' + name

print(func1('oleg')) # Hello Oleg
print(10) # 10