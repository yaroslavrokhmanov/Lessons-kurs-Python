# 1
txt1 = '1234'
txt2 = '5678'
st1 = set(txt1)
st2 = set(txt2)
print(st1 | st2) # {'8', '2', '4', '1', '5', '3', '7', '6'}

# 2
tlp = ('a', 'b', 'c', 'd')
st = set(tlp) 
print(st) # {'d', 'a', 'c', 'b'}

# 3
dct = {
	1: 'ab',
	2: 'cd',
	3: 'ef',
	4: 'jh'
}
st1 = set(dct)
st2 = dct.values()
print(st1) # {1, 2, 3, 4}
print(set(st2)) # {'cd', 'ab', 'ef', 'jh'}

