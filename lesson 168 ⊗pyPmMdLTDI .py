# 1.Дан трехмерный список:

lst = [
	[
		['q', 'w', 'e'],
		['r', 't', 'y'],
		['u', 'i', 'o'],
	],
	[
		['p', 'a', 's'],
		['d', 'f', 'g'],
		['h', 'j', 'k'],
	],
	[
		['l', 'z', 'x'],
		['c', 'v', 'b'],
		['n', 'm', 'q'],
	],
]
# С помощью цикла выведите все элементы списка в консоль.

for elem in lst:
    for elem1 in elem:
        for elem2 in elem1:
            print(elem2) # qwertyuiopasghjklzxcvbnmq


# 2.Дан трехмерный список:

lst = [
	[
		[1, 3],
		[5, 7],
	],
	[
		[2, 4],
		[6, 8],
	],
]
# С помощью цикла получите сумму всех элементов списка.

res = 0
for elem in lst:
    for elem1 in elem:
        for elem2 in elem1:
            res += elem2
            print(res) #36
