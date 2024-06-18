# 1
tst = 15
# Проверьте, что она больше 10 и меньше 20.
if 10 < tst < 20:
    print('+++') # +++
else:
    print('---')

# 2
tst = -5
if (0 > tst > -10) or (-8 < tst < 30):
    print('+++') # +++
else:
    print('---')

# 3
tst = ['a', 'b', 'c', 'd', 'e']
if len(tst) < 6 and len(tst) > 0:
    print('+++') # +++
else:
    print('---')
