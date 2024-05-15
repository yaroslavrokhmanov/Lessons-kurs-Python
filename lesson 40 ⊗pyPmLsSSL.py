#1 
txt = 'a,b,c,d,e'
print(txt.split(',')) # ['a', 'b', 'c', 'd', 'e']

# 2
txt = 'a_bc_de'
print(txt.split('_')) # ['a', 'bc', 'de']

# 3
txt = 'ab 12 cd'
print(txt.split('')) # Ошибка. Не вписали разделитель

# 4
txt = '1 23 45'
print(txt.split(' ')) # ['1', '23', '45']

# 5
txt = '123_45'
print(txt.split()) # ['123_45'] Нет разделителя. Выведется одной строкой
