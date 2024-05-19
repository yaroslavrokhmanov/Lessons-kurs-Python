# 1
lst = [1, 2, 3, 4, 5, 6]
del lst[0::2]
print(lst) #[2, 4, 6]

# 2
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst1 = lst[::-1]
print(lst1[::2]) #[8, 6, 4, 2]