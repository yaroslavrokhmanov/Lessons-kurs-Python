# 1.Дана строка:
txt = 'Abcde'
# Проверьте, что она начинается с заглавной буквы.
print(txt.istitle()) # True

# 2. Дан список:
lst = ['User1', 'User2', 'user3', 'User4']
# Проверьте, начинается ли каждый его элемент с заглавной буквы.
res= [el[0].isupper() for el in lst]
print(res) # [True, True, False, True]

# 3. Дана строка:
txt = 'ABCDE' # True
# Проверьте, что все ее буквы находятся в верхнем регистре.
print(txt.isupper()) # True

# 4. Дана строка:
txt = 'abcde'
# Проверьте, что все ее буквы находятся в нижнем регистре.
print(txt.islower()) # True

# 5. Дана строка:
txt = 'abcde'
# Проверьте, что она состоит только из букв.
print(txt.isalpha()) # True

# 6. Дана строка:
txt = '12345'
# Проверьте, что она состоит только из цифр.
print(txt.isdigit()) # True

# 7.Дана строка:
txt = 'Ⅷ'
# Проверьте, что она состоит только из цифр.
print(txt.isnumeric()) # True

# 8.Дана строка:
txt = '12345abc'
# Проверьте, что она состоит только из букв и цифр.
print(txt.isalnum()) # True

# 9.Дана строка:
# txt = 'a1b2c3d '
# Проверьте, что она состоит только из букв и цифр.
print(txt.isalnum()) # True

# 10.Дана строка:
txt = ' '
# Проверьте, состоит ли она только из пробелов.
print(txt.isspace()) # True

# 11.Дан список:
lst = ['a', 'b', ' ', 'c', '']
# Проверьте, есть ли в нем элементы, содержащие только пробелы.
res = [el.isspace() for el in lst ] 
print(res) # [False, False, True, False, False]