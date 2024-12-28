1.# Дана строка:
txt = 'a1bc11de'
# Удалите из строки все единицы, чтобы получить следующий результат:
# ['a', 'b', 'c', 'd']
# print(txt.strip('e'))

result = [elem for elem in txt if elem != '1']
print(result)  # ['a', 'b', 'c', 'd', 'e']

# 2.Дана строка с концевыми пробелами:
txt = ' abcde '
# Удалите пробелы с ее концов:
# 'abcde'
print(txt.strip())

# 3.Дана строка с концевыми пробелами:
txt = ' abcde '
# Удалите пробелы слева:
# 'abcde '
print(txt.lstrip())

# 4.Дана строка с концевыми пробелами:
txt = ' abcde '
# Удалите пробелы справа:
# ' abcde'
print(txt.rstrip())

# 5.Дана строка с концевыми пробелами:
txt = ' abcde '
# Удалите пробелы справа:
# ' abcde'
print(txt.rstrip())

# 6.Даны строка и число:
txt = 'abc {}'
num = 12
# Подставьте в строке вместо фигурных скобок число.
print(txt.format(num)) # abc 12

# 7.Пусть у вас есть строчная переменная, в которой после имени пользователя идут фигурные скобки. Передайте в них с помощью переменной age его возраст.
user = 'Oleg {}'
age = 21
print(user.format(age)) # Oleg 21

# 8.Дана пустая строка:
txt = ''
# Дана переменная:
num = 6
# Запишите в строку столько нулей, какое значение содержится в нашей переменной:
# '000000'
print(txt.zfill(num)) # 000000

# 9.Дана строка:
txt = 'abcde'
# Напишите код, чтобы получить следующий результат:
# 'abcde111'
print(txt.ljust(8, '1')) # abcde111

#10.Дана строка:
txt = '12345'
# Напишите код, чтобы получить следующий результат:
# 'aa12345'
print(txt.rjust(7, 'a')) # aa12345
