import time

# 1.Дана дата:
dt = '24/07/2015 16:1'
# Найдите количество секунд, прошедшее с текущего момента времени до этой даты.
now = time.time()
dt = time.strptime('24/07/2015 16:10', '%d/%m/%Y %H:%M') 
dt_epoch = time.mktime(dt)
res = now - dt_epoch
print(res) # 298239052.48665404


# 2.Даны две даты:
dt1 = '12/02/23 10:12:54'
dt2 = '31/12/24 19:38:21'
# Найдите количество секунд, прошедшее между второй и первой датами.
now = time.time()
dt1 = time.strptime('12/02/23 10:12:54', '%d/%m/%y %H:%M:%S') 
dt2 = time.strptime('31/12/24 19:38:21', '%d/%m/%y %H:%M:%S') 

t_epoch1 = time.mktime(dt1)
t_epoch2 = time.mktime(dt2)

res = t_epoch2  - t_epoch1
print(res) # 59477127.0

# 3.Модифицируйте решение предыдущей задачи так, чтобы найти количество дней, прошедшее между двумя датами.
dt1 = '12/02/23 10:12:54'
dt2 = '31/12/24 19:38:21'
now = time.time()
dt1 = time.strptime('12/02/23 10:12:54', '%d/%m/%y %H:%M:%S') 
dt2 = time.strptime('31/12/24 19:38:21', '%d/%m/%y %H:%M:%S') 

t_epoch1 = time.mktime(dt1)
t_epoch2 = time.mktime(dt2)

res = t_epoch2  - t_epoch1
print(res/(60*60*24)) # 688.3926736111111