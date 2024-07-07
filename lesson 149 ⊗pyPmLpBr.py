# 1
# Дано множество:
# tst = {1, 3, 6, 7, -9, 12}
# Выведите его элементы до первого отрицательного числа.
tst = {1, 3, 6, 7, -9, 12}
for el in tst:
    print(el)
    if el < 0:
        break
    print(el)


# 2
# Дан список:
# tst = [7, 1, 2, 5, 0, 3, 9]
# Найдите сумму элементов этого списка до первого нуля.

tst = [7, 1, 2, 5, 0, 3, 9]
res = 0
for el in (tst):
    if el == 0:
        break
    res = res + el 
    print(res) # 
 

# 3
# Дано число:
# tst = 897654
# Сформируйте из него список до числа 6.

tst = 897654
res = []
for el in str(tst): 
    if el == '6':
        break
    res.append(int(el))
print(res)
