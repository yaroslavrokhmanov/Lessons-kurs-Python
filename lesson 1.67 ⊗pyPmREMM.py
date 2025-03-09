import re   

# 1. Проверьте, что строка начинается на буквы:

txt = 'abc 123 bbb 456 987'
# Выведите совпадение буквенных символов в начале строки.
res = re.match('\w+',txt)
print(res[0]) # abc

# 2. Дана строка:

txt = 'aaa bbb 123'
# Найдите подстроку, содержащую цифры.
res = re.search('\d+',txt)
if res:
    print(res.group()) # 123
else:
    print('sorry')