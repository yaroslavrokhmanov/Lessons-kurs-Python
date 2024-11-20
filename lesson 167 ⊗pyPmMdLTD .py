# 1.Дан следующий список:
# lst = [
# 	[
# 		['a', 'b'],
# 		['c', 'd'],
# 	],
# 	[
# 		['e', 'f'],
# 		['g', 'h'],
# 	]
# ]
# Выведите из него строку 'acfg'.

lst = [
	[
		['a', 'b'],
		['c', 'd'],
	],
	[
		['e', 'f'],
		['g', 'h'],
	]
]

elem1 = lst[0][0][0]
elem2 = lst[0][1][0]
elem3 = lst[1][0][1]
elem4 = lst[1][1][0]
print(elem1 + elem2 + elem3 + elem4) #acfg

# 2.Дан следующий список:
# lst = [
# 	[
# 		[1, 2],
# 		[3, 4],
# 	],
# 	[
# 		[5, 6],
# 		[7, 8],
# 	],
# ]
# Найдите сумму всех элементов приведенного списка.


lst = [
	[
		[1, 2],
		[3, 4],
	],
	[
		[5, 6],
		[7, 8],
	],
]

# 1
elem1 = lst[0][0][0] + lst[0][0][1]
elem2 = lst[0][1][0] + lst[0][1][1]
elem3 = lst[1][0][0] + lst[1][0][1]
elem4 = lst[1][1][0] + lst[1][1][1]
print(elem1 +  elem2 + elem3 + elem4) #36

# 2
res = 0
for elems in lst:
    for elems1 in elems:
        for num in elems1:
            res += num
            print(res) #36



