import re

# 1. Дана строка, содержащая домен:

txt = 'sss domain.ru zzz'
# Найдите этот домен и положите его имя в первый карман, а зону - во второй.

res = re.search('(\w+)\.(\w+)', txt)
print(res[0]) # domain.ru
print(res[1]) # domain
print(res[2]) # ru



# 2. Дана строка, содержащая дату:

txt = '31.12.2025'
# Положите день в первый карман, месяц - во второй, а год - в третий.
# res = re.search('(\d{2})\.(\d{2}).\(\d{4})', txt)
res = re.search('(\d{2})\.(\d{2})\.(\d{4})', txt)
print(res[0]) #31.12.2025
print(res[1]) # 31
print(res[2]) # 12
print(res[3]) # 2024