import datetime

# 1.Выведите в консоль текущую дату в формате день.месяц.год.
dt = datetime.datetime.now()
res = dt.strftime('%d.%m.%Y')
print(res) # 01.01.2025

# 2.Выведите в консоль текущее время в следующем формате: часы:минуты:секунды год/месяц/день:день недели.
dt = datetime.datetime.now()
res = dt.strftime('%H:%M:%S %Y/%m/%d: /%A')
print(res) # 13:01:32 2025/01/01: /Wednesday