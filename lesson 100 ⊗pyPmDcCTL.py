# 1
dct = {
	1: 'ab',
	2: 'cd',
	3: 'ef'
}
res = list(dct)
print(res) #[1, 2, 3]

# 2
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = list(dct)
res.reverse()
print(res) #['z', 'y', 'x']