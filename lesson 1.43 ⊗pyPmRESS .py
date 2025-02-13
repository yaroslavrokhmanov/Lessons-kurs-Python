import re

# 1. Дана строка:

txt = 'aba aea aca aza axa a.a a+a a*a'
# Напишите регулярку, которая найдет строки 'a.a', 'a+a', 'a*a', не затронув остальных.
res = re.findall(r'a[\.\+\*]a', txt)
print(res) # ['a.a', 'a+a', 'a*a']


# Дана строка:

txt = 'xaz x.z x3z x@z x$z xrz'
# Напишите регулярку, которая найдет строки по шаблону: буква 'x', затем НЕ точка, НЕ собака, и НЕ доллар, а потом буква 'z'.
res = re.findall('x[^.@$]z', txt)
print(txt) # xaz x.z x3z x@z x$z xrz


