# 1.Дан двухмерный список:

lst = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
# С помощью цикла выведите все элементы списка в консоль.

for el1 in lst:
    for elem in el1:
     
                print(elem) #123456789
                

# 2. Дан двухмерный список:

lst = [
	[2, 4, 6],
	[3, 5, 7],
	[9, 12, 15]
]
# С помощью цикла найдите сумму элементов этого списка.
res = 0
for el1 in lst:
    for elem in el1:
					res += elem
print(res) #63

# 3.Дан двухмерный список:

lst = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]
# С помощью цикла слейте все элементы списка в строку.

res = ''
for el1 in lst:
    for elem in el1:
					res += elem
print(res) # abcdefghi
print(type(res)) # <class 'str'>