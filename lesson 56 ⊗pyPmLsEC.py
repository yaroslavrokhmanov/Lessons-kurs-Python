# 1
lst = ['a', 'b', 'c', 'd']
print(lst.count('c')) #1

# 2
lst = ['1', 'b', '2', 'd']
print(lst.count(1)) #0  нет цифры 1, есть строка '1'

# 3
lst = ['ab', '12', 2, 'cd', 1, 2]
print(lst.count(2)) #2