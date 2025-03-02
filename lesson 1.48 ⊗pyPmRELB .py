import re

# 1.Дана строка:
txt = 'abc def xyz'
# Напишите регулярку, которая найдет первую подстроку из букв.
res = re.findall('^\w+', txt) 

print(res) # # ['abc']

# 2.Дана строка:
txt = 'abc def xyz'
# Напишите регулярку, которая найдет последнюю подстроку из букв
res = re.findall('\w+$', txt) 

print(res) # ['xyz']