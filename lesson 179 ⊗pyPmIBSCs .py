# 1.Дана строка:
txt = 'ABCDE'
# Сделайте все буквы в ней строчными.
print(txt.lower()) # abcde

# 2.Дана строка:
txt = 'abcde'
# Сделайте заглавными все буквы этой строки.
print(txt.upper()) # ABCDE

# 3.Дана строка:
txt = 'abcde'
# Сделайте заглавной первую букву этой строки.
print(txt.capitalize()) # Abcde

# 4.Дана строка:
txt = 'word1 word2 word3'
# Сделайте заглавными первые буквы каждого слова из этой строки:
# 'Word1 Word2 Word3'
print(txt.title()) # Word1 Word2 Word3

# 5.Дана строка:
txt = 'ABC def'
# Поменяйте регистр символов на противоположный:
# 'abc DEF'
print(txt.swapcase()) # abc DEF

# 6.Дан список:
lst = ['ab', 'Cd', 'eF']
# Пусть каждый его элемент начинается с заглавной буквы.
res = []
for el in lst:
    res.append(el.capitalize())
print(res) # ['Ab', 'Cd', 'Ef']

# 7.Пусть у вас есть словарь, в котором ключами являются имена пользователей, а значениями - их электронная почта. Напишите такой код, чтобы все буквы строк с почтой были строчными.
users = {
    "Pol": "Pol@example.com",
    "Bob": "Bob@example.com",
    "Damian": "damian@example.com"
}
for el in users:
    users[el] = users[el].lower()
print(users) # {'Pol': 'pol@example.com', 'Bob': 'bob@example.com', 'Damian': 'damian@example.com'}