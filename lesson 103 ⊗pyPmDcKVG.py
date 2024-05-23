# 1
dct = {
	'x': 3,
	'y': 2,
	'z': 1
}
res = dct.items()
print(res) #([('x', 3), ('y', 2), ('z', 1)])

# 2
dct = {
	'a': [2, 4],
	'b': [3, 5]
}
res = dct.items()
print(res) #([('a', [2, 4]), ('b', [3, 5])])

# 3
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = list(dct.items())
print(res) #[(1, 'x'), (2, 'y'), (3, 'z'), (4, 'w')]

# 4
dct = {
	'a': 12,
	'b': 34,
	'c': 56
}
res = list(dct.keys())
res1 = list(dct.values())
sl=list(dct.items())
print(res) #['a', 'b', 'c']
print(res1) #[12, 34, 56]
print(list(dct.items())) #[('a', 12), ('b', 34), ('c', 56)]
print(dict(sl)) #{'a': 12, 'b': 34, 'c': 56}

### !!!!!Получите все его элементы в следующем виде:
# ['a', 12, 'b', 34, 'c', 56]
# Не смог получить в таком выиде. Если исходя из того что учили не пойму что применить.

