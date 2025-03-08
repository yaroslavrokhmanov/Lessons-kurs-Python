import re

# 1.Дана строка со временем:

txt = '12:59:59'
# Положите часы, минуты и секунды в отдельные именованные карманы.

res = re.search('(?P<elem1>\d{2})\:(?P<elem2>\d{2})\:(?P<elem3>\d{2})', txt)
print(res.groupdict()) # {'elem1': '12', 'elem2': '59', 'elem3': '59'}

# 2.Дана строка:

txt = 'aaa bbb 123 456'
# Положите подстроки 'aaa' и 'bbb' в отдельные именованные карманы.

res = re.search('(?P<elem1>[a-zA-Z]{3}) (?P<elem2>[a-zA-Z]{3}) (?P<elem3>\d{3})', txt)
print(res.groupdict()) # {'elem1': 'aaa', 'elem2': 'bbb', 'elem3': '123'}

# 3.Дана строка:

txt = 'alex23'
# Положите имя и возраст пользователя в отдельные именованные карманы.

res = re.search('(?P<name>[a-zA-Z]+)(?P<age>\d{2})', txt)
print(res.groupdict()) # {'name': 'alex', 'age': '23'}