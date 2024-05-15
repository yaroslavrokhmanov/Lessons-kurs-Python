# 1
tpl = (2, 4, 6, 10)
res = 8 in tpl
print(res) # False

# 2
tpl = ('abc', 'def')
res = 'd' in tpl
print(res) # False

# 3
tpl = ('1', '2', '3')
res = 1 not in tpl
print(res) #True

# 4
tpl1 = ('ac', '3', 4, 'bd', 5)
tpl2 = (1, 2, 3)

res1 = 4 in tpl1
res2 = 2 not in tpl2
print(res1) #True
print(res2) #False