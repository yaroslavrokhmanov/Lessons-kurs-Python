# 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
del dct['x']
print(dct) # {'y': 2, 'z': 3}

# 2
dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e'
}
del dct[5]
res = list(dct) 
res.reverse()
print(res) # [4, 3, 2, 1]