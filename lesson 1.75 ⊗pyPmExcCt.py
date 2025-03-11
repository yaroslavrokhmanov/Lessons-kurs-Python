import math


# 1.Спросите у пользователя два числа. Поделите одно на другое. Поймайте исключительную ситуацию деления на ноль.
elem1 = float(input('Write first number:'))
elem2 = float(input('Write second number:'))
try:
    res = elem1 / elem2
    print('Result:', res)
except ZeroDivisionError:
    print('error!!! you write zero')

# 2.Спросите у пользователя число. Найдите квадратный корень из этого числа. Поймайте исключительную ситуацию извлечения корня из отрицательного числа.
elem = float(input('Write number:'))
try:
    res =  math.sqrt(elem)
    print('Result:', res)
except:
    print('error!!!')

# 3.Дан список. Спросите у пользователя целое число. Получите элемент списка, номер которого ввел пользователь. Поймайте исключительную ситуацию, которая случится, если пользователь ввел число вне диапазона списка.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    elem = int(input('Write number:'))
    print('Result:', numbers[elem])
except IndexError:
    print('error!!! dont have this number')

# 4.Дан следующий код:
# num = '5'
# res = num + 2
# print(res)
# Что не так с этим кодом? Исправьте его недостатки.

num = 5
res = num + 2
print(res) # 7 nedostatok w tom czto w num = '5' stroka str a w rezultate pribawlaem int cifra. Nugno slogit ili drwe stroki togda res = '5' + '2' = 52 ili dwa czisla 5 + 2 = 7. Izmenil na czisla tak logiczniej

# 5.Дан следующий код:
# lst = [1, 2, 3, 4]
# def getElem(iter):
# 	print(iter[4])
# getElem(lst)
# Что не так с этим кодом? Исправьте его недостатки.
lst = [1, 2, 3, 4]
def getElem(iter):
    print(iter[-1]) # 4 indeks naczinaetsa s 0. poslednij element 3. Czto by poluczit poslednij ispolzowal -1 rawen 4
getElem(lst)
   