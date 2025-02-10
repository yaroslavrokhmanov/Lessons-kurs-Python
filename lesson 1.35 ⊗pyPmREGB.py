import re
# 1.Дана строка:

txt = 'ab abab abab abababab abea'
# Напишите регулярку, которая найдет строки по шаблону: строка 'ab' повторяется 1 или более раз.
# res = re.findall('(ab)+', '!', txt)
res = re.findall('(?:ab)+', txt)
print(res) # ['ab', 'abab', 'abab', 'abababab', 'ab']