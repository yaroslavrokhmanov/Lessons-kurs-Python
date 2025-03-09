import re   

# 1. Дана строка с датой и временем:

txt = '2025-12-31 12:59:59'
# Разбейте эту строку так, чтобы все год, месяц, день, часы, минуты и секунды находились в одном массиве.

res = re.findall('(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})', txt)
print(res[0]) # ('2025', '12', '31', '12', '59', '59')