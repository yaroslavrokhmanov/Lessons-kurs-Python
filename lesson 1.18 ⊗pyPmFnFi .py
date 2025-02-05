# lst = [1, 2, 3, 4, 5, 6]
# res = filter(lambda num: num % 2 == 0, lst)
# print(list(res))

# 1.Дан список с числами:

lst = [1, 2, 3, 4, 5]
# Запишите в новый список только нечетные числа из этого списка.
res = filter(lambda num: num % 2 != 0, lst)
print(list(res)) # [1, 3, 5]


# 2.Дан список со строками:
lst = ['abcd', 'ab', 'c', 'de', 'bc']
# Запишите в новый список только строки, длина которых равна 2.
res = filter(lambda num: len(num) == 2, lst)
print(list(res)) # ['ab', 'de', 'bc']
