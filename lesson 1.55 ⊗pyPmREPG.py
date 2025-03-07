import re

# 1.Дана строка:

txt = 'username:john'
# Положите 'username:' в первый карман, а 'john' - во второй. Выведите все карманы в консоль.
res = re.search('(\w+):(\w+)', txt)
print(res.group(0)) # username:john
print(res.group(1)) # username
print(res.group(2)) # john


# 2.Дана строка:

txt = '123 aaabbbccc'
# Разложите все буквенные символы по трем карманам так, чтобы подстрока, состоящая из буквы 'a' попала в первый карман, 'b' - во второй, 'c' - в третий. Выведите все карманы в консоль.
res = re.search('(\d+)\s(\w+)', txt)
print(res.group(0)) # 123 aaabbbccc
print(res.group(1)) # 123
print(res.group(2)) # aaabbbccc