# 1.Каким будет результат выполнения следующего кода:

def func(lst):
	lst[0] = '!'
	
lst = [1, 2, 3, 4, 5]
func(lst)

print(lst) # ['!', 2, 3, 4, 5]

# 2.Каким будет результат выполнения следующего кода:

def func(lst):
	lst[0] = '!'
	
lst = [1, 2, 3, 4, 5]
lst = func(lst)

print(lst) # None

# 3.Каким будет результат выполнения следующего кода:

def func(lst):
	lst = '!'

lst = [1, 2, 3, 4, 5]
func(lst[0])

print(lst) # [1, 2, 3, 4, 5]

# 4.Каким будет результат выполнения следующего кода:

def func(dct):
	for key in dct.keys():
		dct[key] += 2
	
dct = {
	'a': 1,
	'b': 2,
	'c': 3,
}

func(dct)
print(dct) # {'a': 3, 'b': 4, 'c': 5}