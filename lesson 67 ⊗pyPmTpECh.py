# 1
tpl = ('ab', 'cd', 'ef')
print(tpl[1]) #cd

# 2 
tpl = (4, 6, 8, 10)
res = tpl[-1] + tpl[0]
tpl[1] = res

print(res) #14 нельзя изменять кортеж