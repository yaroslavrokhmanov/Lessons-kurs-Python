# 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.pop('x')) # 1
print(dct) # {'y': 2, 'z': 3}

# 2
dct = {
	1: '1',
	2: '2',
	3: '3'
}

print(dct.pop('2')) # ошибка, указали не номер ключа 1 а значение '1'

# 3
dct = {
	'surn': 'smith',
	'name': 'john',
	'age': 30
}

dct.pop('surn')
print(dct) #{'name': 'john', 'age': 30}

# 4
dct = {
	1: 'ab',
	2: 'cd',
	3: 'ef'
}
dct.pop(2)
print(list(dct.items())) #[(1, 'ab'), (3, 'ef')]