import re            

# 1. Дана строка:

txt = '12 aaa 34 bbb 56 ccc'
# Выведите из нее все числа с помощью цикла.

res = re.finditer('\d', txt)

for el in res:

    print(el[0]) # 123456
