import re

# 1. Дана строка:

txt = 'aeeea aeea aea axa axxa axxxa'
# Напишите регулярку, которая найдет строки по шаблону: по краям стоят буквы 'a', а между ними - или буква 'e' любое количество раз или буква 'x' любое количество раз.

# Корректное регулярное выражение
res = re.findall('a(?:e+|x+)*a?', txt) 

print(res) # ['aeeea', 'aeea', 'aea', 'axa', 'axxa', 'axxxa']

# 2.Дана строка:

txt = 'aeeea aeea aea axa axxa axxxa'
# Напишите регулярку, которая найдет строки по шаблону: по краям стоят буквы 'a', а между ними - или буква 'e' два раза или буква 'x' любое количество раз.

res = re.findall('a(?:e{2}|x+)a?', txt)

print(res) # ['aee', 'aeea', 'axa', 'axxa', 'axxxa']

