# 1.В следующем коде некоторый программист допустил ошибку:
num = 4
def func():
    global num # nie byla ukazana global dla raboty s niej
    num *= 2
    return num
print(func()) # 8
# Что не так с этим кодом? Найдите и исправьте ошибку автора кода.

# 2.В следующем коде некоторый программист допустил ошибку:
# num = 10
# def func():
# 	num -= 3
# 	return i
# print(func())
# Что не так с этим кодом? Найдите и исправьте ошибку автора кода.

num = 10
def func():
    global num # nie byla ukazana global dla raboty
    num -= 3
    return num

print(func()) # 7