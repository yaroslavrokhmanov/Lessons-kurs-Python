# 1.Дан список:

lst = ['a', 'b', 'c', 'd', 'e']
# С помощью этого списка создайте словарь, в котором ключами будут элементы нашего списка, а значениями - их порядковые номера:

# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
res = {lst[i]: i + 1 for i in range(len(lst))}
print(res) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 2.Даны два списка:

lst1 = ['name1', 'name2', 'name3', 'name4']
lst2 = ['john', 'kate', 'alex', 'mary']
# С помощью них создайте словарь, в котором ключами будут элементы первого списка, а значениями - второго списка:

{'name1': 'john', 'name2': 'kate', 'name3': 'alex', 'name4': 'mary'}

res = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(res) # {'name1': 'john', 'name2': 'kate', 'name3': 'alex', 'name4': 'mary'}