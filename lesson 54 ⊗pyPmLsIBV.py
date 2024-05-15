# 1
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.index('c')) #2

# 2
lst = ['a', 'b', 'c', 'b', 'd']
print(lst.index('b', 2)) #3

# 3
lst = ['ab', 12, 'cd', 34]
tst = 'cd'

print(lst.index(tst)) #2

# 4
lst = [1, 3, 'a', 'b', 3, 6]
tst = 2

print(lst.index(tst)) #ошибка, нет еденицы в списке
