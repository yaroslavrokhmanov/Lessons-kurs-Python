
import datetime 

# 1.Даны две даты:
dt1 = '13/10/2018 22:15:45'
dt2 = '15/11/2018 09:47:16'
# Определите сколько времени прошло между ними.
start_time = datetime.datetime.strptime(dt1, '%d/%m/%Y %H:%M:%S')
end_time = datetime.datetime.strptime(dt2, '%d/%m/%Y %H:%M:%S')
result  = end_time - start_time
print(result) # 32 days, 11:31:31

# 2.Даны две даты:
dt1 = '01-12-2025 16:07:5'
dt2 = '31:12:2025 10:32:45'
# Определите сколько времени прошло между ними.
start_time = datetime.datetime.strptime(dt1, '%d-%m-%Y %H:%M:%S')
end_time = datetime.datetime.strptime(dt2, '%d:%m:%Y %H:%M:%S')
result  = end_time - start_time
print(result) # 29 days, 18:25:40