# 1.Каким будет результат выполнения следующего кода:

lst1 = [1, 2, 3, 4, 5]

lst2 = lst1
lst2[0] = '!'

print(lst1) # ['!', 2, 3, 4, 5]

# 2.Каким будет результат выполнения следующего кода:

lst1 = [1, 2, 3, 4, 5]

lst2 = lst1
lst2[0] = '!'

print(lst2) #  ['!', 2, 3, 4, 5]

# 3.Каким будет результат выполнения следующего кода:

lst1 = ['a', 'b', 'c', 'd']

lst2 = lst1
lst3 = 'e'
lst2[2] = lst3

print(lst2) # ['a', 'b', 'e', 'd']