# 1
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst1.extend(lst2)
print(lst1)

# 2
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst3 = [1, 2, 3]
lst1.extend(lst3)
lst1.extend(lst2)
print(lst1)

