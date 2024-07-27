# 1	
# Дан список. Проверьте, все ли его элементы являются четными числами.
lst = [1, 2, 3, 4, 5, 6]
flag = True
for el in lst:
    if el % 2 != 0:
        flag = False
if flag:
     print('+++')
else:
     print('---') # ---


# 2
# Дана строка:
# tst = 'abcdef'
# Проверьте, входит ли в нее символ 'd'.
tst = 'abcdef'
for el in tst:
     if 'd' in tst:
          print('+++')
     else:
          print('---')
