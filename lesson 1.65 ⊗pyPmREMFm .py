import re      

# 1. Проверьте, что следующая строка состоит только из букв:

txt = 'abcde'

res = re.fullmatch('\w+', txt)
print(res[0]) # abcde

# 2. Проверьте, что следующая строка состоит только из цифр:

txt = '12345'
res = re.fullmatch('\d+', txt)
print(res[0]) # 12345