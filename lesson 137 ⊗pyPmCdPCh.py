# 1
tst = 'x'
lst = ['x', 'y', 'z', 'w']
if tst in lst:
    print('+++') # +++
else:
    print('---')

# 2
tst = '1'
st = {1, 2, 3, 4, 5}
if tst not in st:
    print('+++') # +++
else:
    print('---')

# 3
tst = '3'
txt = '123456'
if tst in txt:
    print('+++') # +++
else:
    print('---')

# 4
tst = 3
lst = ['a', 'b', 'c', 'd', 'e']
res = lst[tst]
tlp = ('a', 'b', 'c')

if res in tlp:
	print('+++')
else:
	print('---') # ---