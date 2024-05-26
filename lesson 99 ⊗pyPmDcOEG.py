# 1
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}

print(dct.get(4)) # w

# 2
dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd'
}

print(dct.get('3')) # None, нет такого ключа

# 3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.get('w', '!')
print(res) # ! 

