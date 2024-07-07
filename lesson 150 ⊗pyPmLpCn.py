# 1
# Дано множество:
# tst = {'a', 'b', 'c', 'd', 'e'}
# Выведите из него все элементы, кроме символа 'd'.

tst = {'a', 'b', 'c', 'd', 'e'}
for el in tst:
	if el == 'd':
		continue
	print(el)

# 2
# Дан список:
# tst = [6, 3, -2, 8, -4, 9]
# Выведите из него все элементы, кроме отрицательных.

tst = [6, 3, -2, 8, -4, 9]
for el in tst:
	if el < 0:
		continue
	print(el)

# 3
# Дан список:
# tst = ['a', 'b', 'c', 'd', 'e']
# Получите из него строку 'acde'.


tst = ['a', 'b', 'c', 'd', 'e']
res = ''
for el in tst:
    if el == 'b':
        continue
    res += el
print(res)
