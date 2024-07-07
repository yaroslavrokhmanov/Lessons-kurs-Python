# 1
# Дан список:
# tst = [8, 6, -4, 2, -1]
# Выведите в консоль значения элементов и их индексы до первого отрицательного числа.
tst = [8, 6, -4, 2, -1]
for key, value in enumerate(tst):
    if value < 0:
        break
    print(key, value)

# 2
# Дан список:
# tst = ['a', 'b', 'c', 'd', 'e']
# Выведите в консоль значения элементов и их индексы:
# 'a1'
# 'b2'
# 'c3'
# 'd4'
# 'e5'
tst = ['a', 'b', 'c', 'd', 'e']
for key, value in enumerate(tst):
    print(key, value)

# 3
# Дан список:
# tst = [1, 2, 3, 4, 5]
# Элементы, стоящие на четных позициях возведите в квадрат, а нечетных - в куб.
tst = [1, 2, 3, 4, 5]
res = []
for key, value in enumerate(tst):
    if value % 2 == 0:
        res.append(value ** 2)
    else:
        res.append(value ** 3)

print(res) # [1, 4, 27, 16, 125]




