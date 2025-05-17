from custom_math import get_divide, get_cube
from user import name, email

# 1.Создайте модуль custom_math, в котором будут находиться следующие функции: get_sum для сложения двух чисел, get_divide для деления двух чисел, get_cube для возведения числа в куб. Импортируйте в рабочий файл только функции get_divide и get_cube.
get_divide(10, 2) #5.0
get_cube(3) # 27

# 2.В модуле user даны следующие переменные:

# name = 'user1'
# email = 'user1@mail.com'
# password = 'qwerty'
# Импортируйте из данного модуля имя и почту пользователя. Выведите их в консоль.
print(name) # user1
print(email)  # user1@mail.com