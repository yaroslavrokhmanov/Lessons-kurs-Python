import datetime

#1.Выведите на экран номер текущего дня недели.
res = datetime.date.today()
print(res.weekday())
print(res.isoweekday()) #1

# 2.Определите, является ли текущий день недели выходным или рабочим днем.
res = datetime.date.today()
print(res.weekday())

if 0 <= res.weekday() <= 4:
    print('work day')
else:
    print('relax day')

# 3.Дата дата '2026-11-2'. Выведите ее день недели для двух случаев - при отсчете понедельника с 0 и при отсчете с 1.
res = datetime.date(2026, 11, 2)
print(res.weekday()) #1
print(res.isoweekday()) #0
