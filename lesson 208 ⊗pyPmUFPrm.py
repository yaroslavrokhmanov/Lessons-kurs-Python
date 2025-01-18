# 1.Пусть у вас есть переменные, принимающие имя и фамилию студента, номер его курса. Создайте функцию, которая выведет на экран значения этих переменных. При этом пусть фамилия выводится в верхнем регистре, а имя - только с заглавной буквы.
def student(name, surname, number_course):
    return name.capitalize(), surname.upper(), number_course

result = student('jarek', 'jarecki', 2)
print(result) # ('Jarek', 'JARECKI', 2)

# 2.Сделайте функцию, которая будет выводить площадь прямоугольника.
def ploszadz_treugolnika(a, b):
    return a * b
print(ploszadz_treugolnika(5, 4)) # 20


# 3.Сделайте функцию, которая параметром будет принимать строку и возвращать кортеж ее символов.
def chenge(elem):
    return tuple(elem)

res = chenge('super')
print(res) # ('s', 'u', 'p', 'e', 'r')


# 4.Создайте функцию, которая будет проверять два числа. Пусть она выводит сообщения о том, какое из них больше другое или если они равны друг другу по значению.
def check(num1, num2):
    if num1 > num2:
        print( str(num1) + ' bolsze ' + str(num2))
    elif num1 < num2:
        print( str(num2) + ' bolsze ' + str(num1))
    else:
        print( str(num1) + ' rawno ' + str(num2))
                    
check(200, 100) # 200 bolsze 100


# 5.Сделайте функцию, которая будет проверять тип переменной и если она является числом, то преобразует ее в строку.
def check_def(elem):
    if isinstance(elem, int):
        elem = str(elem)
    print(elem)
    
check_def(845857) # 845857
check_def('hello') # hello


# 6.Сделайте функцию, заполняющую список четными числами от 1 до заданного.
def numbers(num):
    start = []
    for el in range(2, num+1, 2):
        start.append(el)
    return start

print(numbers(10)) # 2, 4, 6, 8, 10]


# 7.Пусть у вас есть словарь, в котором в качестве ключей хранятся имена пользователей, а в качестве значений - их возраст. Создайте функцию, которая выведет все пары ключ-значение в виде кортежа.
users = {
'Jan': 21,
'Polina': 48,
'Gregor': 61,
'Oleg': 10
}

def new_users(el):
    return list(el.items())
print(new_users(users)) # [('Jan', 21), ('Polina', 48), ('Gregor', 61), ('Oleg', 10)]

# 8.Сделайте функцию, которая параметром будет принимать число, а возвращать строку с соответствующим днем недели.
days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }

def search(day):
         return days.get(day) 
print(search(5)) 

