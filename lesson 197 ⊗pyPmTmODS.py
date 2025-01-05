import time

# 1.Выведите на экран свое имя через 15 секунд.
time.sleep(15)
print('Yarek')

# 2.Дан список:
lst = ['a', 'b', 'c', 'd']
# Выведите все его элементы через каждые 3 секунды.
time.sleep(3)
for el in lst:
    print(el)