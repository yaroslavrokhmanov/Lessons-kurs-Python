# 1
tst = [[1, 'ab'], [2, 'cd'], [3, 'ef']]
dct = dict(tst) #словарь {1: 'ab', 2: 'cd', 3: 'ef'}
print(dct)

# 2
tst = [('x', 2), ('y', 4), ('z', 6)]
dct = dict(tst)
print(dct) # {'x': 2, 'y': 4, 'z': 6}

# 3
tst = ['a', 'b', 'c', 'd']
dct = dict(tst)
print(dct) # ошибка, так как непарные числа

# 4
tst = ('a', 1), ('b', 2), ('c', 3)
dct = dict(tst)
print(dct) # {'a': 1, 'b': 2, 'c': 3}