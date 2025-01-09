# 1.Дана функция:

def func1(num1, num2, num3):
	return (num1 + num2) * num3

# Вызовите ее, передав значения через именованные параметры.

result = func1(num1 = 10, num2 = 20, num3 = 30)
print(result) #900

# 2.Дана функция:

def func1(text1, text2):
	return text1 + ' ' + text2
# Вызовите ее, передав строку 'hello' и свое имя через именованные параметры.

result = func1(text1 = 'hello', text2 = 'Yarek')
print(result) # hello Yarek