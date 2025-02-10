import re

# 1.Дана строка:

txt = 'aa aba abba abbba abbbba abbbbba'
# Напишите регулярку, которая найдет строки 'abba', 'abbba', 'abbbba' и только их.
res = re.findall('ab{2,4}a+', txt)
print(res) # ['abba', 'abbba', 'abbbba']


# 2.Дана строка:

txt = 'aa aba abba abbba abbbba abbbbba'
# Напишите регулярку, которая найдет строки вида 'aba', в которых 'b' встречается менее 3-х раз (включительно).
res = re.findall('ab{1,3}a', txt)
print(res) # ['aba', 'abba', 'abbba']


# 3.Дана строка:

txt = 'aa aba abba abbba abbbba abbbbba'
# Напишите регулярку, которая найдет строки вида 'aba', в которых 'b' встречается более 4-х раз (включительно).
res = re.findall('ab{4,}a', txt)
print(res) # ['abbbba', 'abbbbba']