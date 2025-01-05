import time

# 1.Получите часы и минуты из объекта struct_time по UTC. Сравните полученные результаты с работой метода localtime.

tm = time.time()
res = time.gmtime(tm)
res1 = time.localtime(tm)

print(res) # time.struct_time(tm_year=2025, tm_mon=1, tm_mday=1, tm_hour=15, tm_min=5, tm_sec=49, tm_wday=2, tm_yday=1, tm_isdst=0)

print(res1) # time.struct_time(tm_year=2025, tm_mon=1, tm_mday=1, tm_hour=16, tm_min=5, tm_sec=49, tm_wday=2, tm_yday=1, tm_isdst=0)