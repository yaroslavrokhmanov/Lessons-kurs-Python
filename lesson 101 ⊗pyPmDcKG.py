# 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.keys()
print(res) #(['x', 'y', 'z'])

# 2
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = dct.keys()
print(res) #([1, 2, 3, 4])

#3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.keys()
print(list(res)) #['x', 'y', 'z']

# 4
dct = {
	2: 'ab',
	4: 'cd',
	6: 'ef'
}
res = list(dct.keys())

print(res[0] + res[1] + res[2]) #12

# 5
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = list(dct.keys())
res.reverse()
print(res) #[4, 3, 2, 1]
