# 1
dct1 = {
	'z': 2,
	'w': 8,
	'f': 10
}

dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}

dct1.update(dct2)
print(dct1) # {'z': 6, 'w': 8, 'f': 10, 'x': 4, 'y': 5}

dct1 = {
	2: 'a',
	4: 'b',
	6: 'c'
}

dct2 = {
	1: 'd',
	3: 'e',
	4: 'f',
	7: 'j'
}

dct2.update(dct1)
print(dct2) #{1: 'd', 3: 'e', 4: 'b', 7: 'j', 2: 'a', 6: 'c'}