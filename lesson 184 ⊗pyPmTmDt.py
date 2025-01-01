import datetime

# 1.Задайте переменной birthdate дату рождения пользователя. Затем выведите ее в формате год-месяц-день.
birthdate = datetime.date(1989, 10, 3)
print(birthdate) # 1989-10-03

# 2.Модифицируйте предыдущую задачу так, чтобы вывести только год рождения пользователя.
birthdate = datetime.date(1989, 10, 3)
print(birthdate.year) # 1989

# 3.Выведите из birthdate день, в который родился пользователь.
birthdate = datetime.date(1989, 10, 3)
print(birthdate.day) # 3

# 4.Выведите из birthdate месяц рождения пользователя.
birthdate = datetime.date(1989, 10, 3)
print(birthdate.month) # 10