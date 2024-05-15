# 1
lst = ['a', 'b', 'c', 'd', 'e']
elem = lst.pop()
print(elem) # 'e'
print(lst)  # ['a', 'b', 'c', 'd']

# 2
lst = ['a', 'b', 'c', 'd', 'e']
elem = lst.pop(0)
print(elem) # 'a'
print(lst)  # ['b', 'c', 'd', 'e']

# 3
lst = ['a', 'b', 'c', 'd', 'e']
elem = lst.pop(1)
print(elem) # 'b'
print(lst)  # ['a', 'c', 'd', 'e']