import re

txt = 'aeeex zzz x kkk'
res = re.findall('a.+?x', txt)
print(res)

# 1.Дана строка:

txt = 'aba accca azzza wwwwa'
# Напишите регулярку, которая найдет все строки по краям которых стоят буквы 'a', и заменит каждую из них на '!'. Между буквами 'a' может быть любой символ (кроме 'a').
res = re.sub('a.*?a', '!', txt) # perwuj podchod
res2 = re.sub('a[^a]*a', '!', txt) # wtoroj podchod, iszet lubyje simvoly kromr a
print(res2)
print(res) # ! ! ! wwwwa