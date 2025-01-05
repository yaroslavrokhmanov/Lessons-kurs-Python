import datetime

# 1.Выведите в консоль текущее время в формате часы:минуты:секунды.
res = datetime.datetime.now()
res1 = datetime.datetime.strftime(res, '%H:%M:%S')
print(res1) 

# 2.Выведите в консоль текущее время в формате год-месяц-день часы:минуты:секунды.
res = datetime.datetime.now()
print(res) # 2025-01-01 12:48:30.416223
