# 1
tpl = ('2', '6', '12')
res = list(tpl)
print(res) #['2', '6', '12']

# 2
tpl1 = ('1', '2', '3')
tpl2 = ('4', '5')
res  = list(tpl1 + tpl2)
print(res) #['1', '2', '3', '4', '5']

# 3
tpl = (1, 2, 3, 4, 5)
res = sorted(tpl, reverse=True)
print(tuple(res)) #(5, 4, 3, 2, 1)