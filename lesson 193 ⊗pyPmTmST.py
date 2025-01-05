import time

# 1.Выведите из struct_time текущий день.
now = time.time()
res = time.localtime(now)
print(res.tm_mday) # 1

# 2.Выведите из struct_time текущий час.
now = time.time()
res = time.localtime(now)
print(res.tm_hour) # 13

# 3.Дана следующая epoch:
dt = 1602314100.0
# Получите из нее struct_time.

res = time.localtime(dt)
print(res) # time.struct_time(tm_year=2020, tm_mon=10, tm_mday=10, tm_hour=9, tm_min=15, tm_sec=0, tm_wday=5, tm_yday=284, tm_isdst=1)