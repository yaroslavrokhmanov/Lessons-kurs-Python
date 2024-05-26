# 1
dct = {
	'x': '1',
	'y': '2',
	'z': '3'
}
res = (int(dct['x']) ** 2) + (int(dct['y']) ** 2) + (int(dct['z']) ** 2)
print(res) #14

# 2
dct1 = {
	'1': 12,
	'2': 24,
	'3': 36
}

dct2 = {
	'a': '3',
	'b': '6',
	'c': '9'
}
res_dct1 = dct1['1'] + dct1['2'] + dct1['3']
res_dct2 = int(dct2['a']) + int(dct2['b']) + int(dct2['c'])
print(res_dct1 - res_dct2) # 54

# 3
dct = {
	1: '4',
	2: '5',
	3: '6'
}
res1 = []
for key in dct.keys():
    res1.append(str(key))
print(res1) # ['1', '2', '3']
print(list(dct.values())) # ['4', '5', '6']

# 4
dct = {
    'x': '1',
    'y': '2',
    'z': '3'
}
dct['x'] = str(2 * (dct['x']))
dct['y'] = str(3 * (dct['y']))
dct['z'] = str(4 * (dct['z']))
print([dct['x'], dct['y'], dct['z']]) # ['11', '222', '3333']

# 5
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(str(dct['x']) + str(dct['y']) + str(dct['z'])) #123

# 6
dct = {
	'a': 7,
	'b': 6,
	'c': 5
}
res1 = str(dct['a'])
res2 = str(dct['b'])
res3 = str(dct['c'])
ress = list(res1 + res2 + res3)
ress.reverse()
print('/'.join(ress)) # 5/6/7 

# 7
dct = {
	'y': 2025,
	'm': 12,
	'd': 31
}
res1 = str(dct['y'])
res2 = str(dct['m'])
res3 = str(dct['d'])
print(res1 + '-' + res2 +  '-' + res3) #2025-12-31


 