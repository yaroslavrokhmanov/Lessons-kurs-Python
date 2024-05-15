# 1
lst = ['a', 'b', 'c', 'd', 'e']
res = '-'.join(lst)
print(res) #a-b-c-d-e

# 2
lst = ['a', '1', 'b', '2']
res = ''.join(lst)
print(res) #a1b2 не укзали роделитель

# 3
lst = ['1', '2', 3, '4']
res = '/'.join(lst)
print(res) #ошибка, так как работать можем только со строками

#4
lst = ['4', '3', '2', '1']
lst.reverse()
res = ''.join(lst)
print(res) #'1234'