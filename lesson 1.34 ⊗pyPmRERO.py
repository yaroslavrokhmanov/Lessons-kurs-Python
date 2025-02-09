import re
# 1.Дана строка:

txt = 'aa aba abba abbba abca abea'
# Напишите регулярку, которая найдет строки 'aba', 'abba', 'abbba' по шаблону: буква 'a', буква 'b' любое количество раз, буква 'a'.
res = re.findall('ab+a', txt)
print(res) # ['aba', 'abba', 'abbba']


# 2.Дана строка:

txt = 'aa aba abba abbba abca abea'
# Напишите регулярку, которая найдет строки 'aa', 'aba', 'abba', 'abbba' по шаблону: буква 'a', буква 'b' любое количество раз (в том числе ни одного раза), буква 'a'.
res = re.findall('ab*a', txt)
print(res) # ['aa', 'aba', 'abba', 'abbba']


# 3.Дана строка:

txt = 'aa aba abba abbba abca abea'
# Напишите регулярку, которая найдет строки 'aa', 'aba' по шаблону: буква 'a', буква 'b' один раз или ни одного, буква 'a'.
res = re.findall('ab?a', txt)
print(res) # ['aa', 'aba']


# 4.Дана строка:

txt = 'aa aba abba abbba abca abea'
# Напишите регулярку, которая найдет строки 'aa', 'aba', 'abba', 'abbba', не захватив 'abca' и 'abea'.
res = re.findall('ab*a', txt)
print(res) # ['aa', 'aba', 'abba', 'abbba']