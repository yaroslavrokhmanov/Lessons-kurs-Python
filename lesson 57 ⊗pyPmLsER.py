# 1
lst = ['a', 'b', 'c', 'd']
lst.reverse()

print(lst) #['d', 'c', 'b', 'a']

# 2
lst = [10, 4, 8, 2]
lst.reverse()

print(lst) #[2, 8, 4, 10]

# 3
lst1 = [1, 2, 3, 4]
del lst1[2]
lst2 = [7, 6, 5]
del lst2[1]
lst2.reverse()
res = lst1 + lst2
res.insert(3, 6)
res.insert(4, 3)
print(res) #[1, 2, 4, 6, 3, 5, 7]