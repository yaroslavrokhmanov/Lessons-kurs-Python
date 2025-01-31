
# 1.Создайте функцию, которая будет принимать в параметры числа от 1 до 7. Назовите эти параметры по дням недели и выведите их в виде словаря.

def days(**kwargs):
    return kwargs
result = days(Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5, Saturday=6, Sunday=7)
print(result) # {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}


# 2.Создайте функцию, которая будет принимать возраст пользователей в виде именованных параметров и выводить их в виде словаря.

def args_users(**kwargs):
    return kwargs
result = args_users(Anton=43, Oleg=22, Vasia=70)
print(result) # {'Anton': 43, 'Oleg': 22, 'Vasia': 70}

