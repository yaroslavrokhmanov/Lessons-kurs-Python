import re

# 1. Дана строка:

txt = 'abc def xyz'

# # Напишите регулярку, которая сделает из этой строки следующую:
# '#abc# #def# #xyz#'
res = re.sub("\\b", '#', txt)
print(res) # #abc# #def# #xyz#


# 2.Дана строка:

txt = 'abc def xyz'

# Напишите регулярку, которая сделает из этой строки следующую:
# 'a+b+c d+e+f x+y+z'
res = re.sub("\\B", '+', txt)
print(res) # a+b+c d+e+f x+y+z