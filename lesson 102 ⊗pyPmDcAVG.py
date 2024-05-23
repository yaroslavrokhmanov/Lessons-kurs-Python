# 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.values()
print(res) #([1, 2, 3])

# 2
dct = {
	4: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = dct.values()
print(res) #(['w', 'y', 'z'])

# 3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = list(dct.values())
print(res) #[1, 2, 3]

# 4
dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	1: 'a',
	2: 'b',
	3: 'c'
}

dct2.update(dct1)
print(list(dct2)) #[1, 2, 3, 'a', 'b', 'c']