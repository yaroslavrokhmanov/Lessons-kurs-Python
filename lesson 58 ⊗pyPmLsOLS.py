# 1
lst = [4, 2, 5, 1, 3]
lst.sort()
print(lst) #[1, 2, 3, 4, 5]

# 2
lst = [4, 2, 5, 1, 3]
lst.sort(reverse=True)
print(lst) #[5, 4, 3, 2, 1]

# 3
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst) #[5, 4, 3, 2, 1]

# 4
lst1 = ['a', 'b', 'c']
lst1.sort(reverse=True)
lst2 = [3, 2, 1]
lst2.sort()
res = lst2 + lst1
print(res) #[1, 2, 3, 'c', 'b', 'a']