# 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print('w' in dct) #False

# 2
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}

print('x' in dct) #False нет такого ключа, только значение 

#3
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}

print('x' not in dct) #True

# 4
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}

print(3 in dct) #True