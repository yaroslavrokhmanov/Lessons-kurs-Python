import re   

# 1. Дана строка, содержащая имена функций:

txt = 'func1() func2() func3()'
# Получите массив имен функций из строки.

res = re.findall('(\w+)(?=\()', txt)

print(res) # ['func1', 'func2', 'func3']


# 2.Дана строка с тегом:

txt = '<a href="" class="eee" id="zzz">'
# Получите массив имен атрибутов этого тега.

res = re.findall('(\w+)(?=\s*=)', txt)

print(res) # ['href', 'class', 'id']


# 3.Дана строка с переменными:

txt = '$aaa $bbb $ccc xxxx'
# Получите подстроки, перед которыми стоит символ доллара.

res = re.findall('(?<=\$)\w+', txt)

print(res) # ['aaa', 'bbb', 'ccc']