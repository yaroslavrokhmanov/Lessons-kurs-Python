# 1
tst = ['a', 'b', 'c', 'd']
res = tuple(tst)
print(res) #('a', 'b', 'c', 'd')

# 2
tst = 'abcde'
tpl = tuple(tst)
print(tpl)

# 3
tst = 12345
tst = str(tst)
tpl = tuple(tst)
print(tpl) #('1', '2', '3', '4', '5')