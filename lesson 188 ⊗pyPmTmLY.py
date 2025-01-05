import calendar

# 1.Дан год:
year = 2020
# Определите, високосный ли он.
res = calendar.isleap(year)
print(res) # True

# 2.Дан год:
year = 1910
# Определите, високосный ли он.
res = calendar.isleap(year)
print(res) # False


# 3.Определите, является ли високосным текущий год.
res = calendar.isleap(2025)
print(res) # False