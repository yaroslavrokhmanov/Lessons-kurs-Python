# 1
# Пусть в переменной num хранится одно из чисел: 1, 2, 3 или 4, содержащее номер поры года. Выведите название поры года, содержащееся в числе.
num = 3
match num:
    case 12 | 1 | 2:
        print('Зима')
    case 3 | 4 | 5:
        print('Весна')# Весна
    case 6 | 7 | 8:
        print('Лето')
    case 9 | 10 | 11:
        print('Осень')
    case _:
        print('Другое значение')

# 2
# Пусть в переменной num хранится номер месяца от 1 до 12. Выведите название поры года, соответствующее этому месяцу.
num = 11
match num:
    case 12 | 1 | 2:
        print('Зима')
    case 3 | 4 | 5:
        print('Весна')
    case 6 | 7 | 8:
        print('Лето')
    case 9 | 10 | 11:
        print('Осень') # Осень
    case _:
        print('Другое значение')

# 3
# Пусть в переменной tst хранится какой-либо тип данных. Напишите вариант, если переменная является строкой. Если она относится к целому числу или числу плавающей точкой, то выведите одно сообщение 'tst is number'.
tst = 'Python'
if isinstance(tst, str):
    print('tst is text') # tst is text
elif isinstance(tst, int) or isinstance(tst, float):
    print('tst is number')
else:
    print('tst is another type')
