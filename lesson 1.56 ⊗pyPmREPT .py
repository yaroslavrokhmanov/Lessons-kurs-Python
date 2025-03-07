import re

# Дана строка, содержащая домен:

txt = 'http://domain.ru'
# Получите кортеж, состоящий из протокола, имени домена и доменной зоны.
res = re.search('(\w+)://(\w+)\.(\w+)', txt)
print(res.groups()) # ('http', 'domain', 'ru')