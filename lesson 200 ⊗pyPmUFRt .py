# 1.Сделайте функцию, которая параметром принимает число, а возвращает куб этого числа. С помощью этой функции найдите куб числа 3 и запишите его в переменную res.

def func(num):
    return num ** 3
res = func(3)
print(res) #27

# 2.С помощью созданной вами функции найдите сумму кубов числа 2 и числа 3 и запишите ее в переменную res.

def func(num):
    return num ** 3
res = func(2) + func(3)
print(res) # 35