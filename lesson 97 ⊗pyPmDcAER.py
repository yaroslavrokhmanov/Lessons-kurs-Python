# 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
dct.clear()
print(dct) #{}

# 2
dct = {
	1: 'text1',
	2: 'text2',
	3: 'text3'
}

dct.clear()
dct[4] = 'text4'
print(dct) #{4: 'text4'}