import datetime
import time

# 1.Выведите из формата epoch текущую дату.
dt = time.time()
res = time.ctime(dt)
print(res) # Wed Jan  1 13:15:19 2025
