import re

# 1.Дана строка:
txt = 'ahb acb aeb aeeb adcb axeb'
# Напишите регулярку, которая найдет строки 'ahb', 'acb', 'aeb' по шаблону: буква 'a', любой символ, буква 'b'.

res = re.findall('a.b', txt)
print(res) # ['ahb', 'acb', 'aeb']

# 2.Дана строка:
txt = 'aba aca aea abba adca abea'
# Напишите регулярку, которая найдет строки 'abba', 'adca', 'abea' по шаблону: буква 'a', 2 любых символа, буква 'a'.

res = re.findall('a..a', txt)
print(res) # ['abba', 'adca', 'abea']

# 3.Дана строка:
txt = 'aba aca aea abba adca abea'
# Напишите регулярку, которая найдет строки 'abba' и 'abea', не захватив 'adca'.
res = re.findall('ab.a', txt)
print(res) # ['abba', 'abea']