import re

# 1.Дана строка:

txt = 'ab cd ef'
# Поменяйте местами буквы во всех двухзначных подстроках.

res = re.sub('(\w)(\w) (\w)(\w) (\w)(\w)', r'\2\1 \4\3 \6\5', txt)
print(res) # ba dc fe

# 2.Дана строка с датой:

txt = '2025:12:31'
# Преобразуйте эту дату в '31-12-2025'.

res = re.sub('(\d{4}):(\d{2}):(\d{2})', r'\3-\2-\1', txt)
print(res) # 31-12-2025