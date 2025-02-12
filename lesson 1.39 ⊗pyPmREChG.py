import re

# 1.Дана строка:

txt = 'a1a a2a a3a a4a a5a aba aca'
# Напишите регулярку, которая найдет строки, в которых по краям стоят буквы 'a', а между ними одна цифра.
res = re.findall('a\d?a', txt)
print(res) # ['a1a', 'a2a', 'a3a', 'a4a', 'a5a']


# 2.Дана строка:

txt = 'a1a a22a a333a a4444a a55555a aba aca'
# Напишите регулярку, которая найдет строки, в которых по краям стоят буквы 'a', а между ними любое количество цифр.
res = re.findall('a\d+a', txt)
print(res) # ['a1a', 'a22a', 'a333a', 'a4444a', 'a55555a']


# 3.Дана строка:

txt = 'aa a1a a22a a333a a4444a a55555a aba aca'
# Напишите регулярку, которая найдет строки, в которых по краям стоят буквы 'a', а между ними любое количество цифр (в том числе и ноль цифр, то есть строка 'aa').
res = re.findall('a\d*a', txt)
print(res)  # ['aa', 'a1a', 'a22a', 'a333a', 'a4444a', 'a55555a']

# 4.Дана строка:

txt = 'avb a1b a2b a3b a4b a5b abb acb'
# Напишите регулярку, которая найдет строки следующего вида: по краям стоят буквы 'a' и 'b', а между ними - не число и не пробел.
res = re.findall('a[^0-9\s]b', txt)
print(res)  # ['avb', 'abb', 'acb']
 
# 5.Дана строка:

txt = 'ave a#b a2b a$b a4b a5b a-b acb'
# Напишите регулярку, которая найдет строки следующего вида: по краям стоят буквы 'a' и 'b', а между ними - не буква, не цифра и не пробел.
res = re.findall('a\Wb', txt)
print(res)  # ['a#b', 'a$b', 'a-b']

# 6.Дана строка:

txt = 'ave a#a a2a a$a a4a a5a a-a aca'
# Напишите регулярку, которая заменит все пробелы на '!'.
res = re.sub('\s', '!', txt)
print(res)  # ave!a#a!a2a!a$a!a4a!a5a!a-a!aca