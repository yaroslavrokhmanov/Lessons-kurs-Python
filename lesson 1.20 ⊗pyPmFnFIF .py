# 1.Напишите внешнюю и внутреннюю функции, совместная работа которых будет выводить каждый строчный элемент списка с заглавной буквы.
def big_later(lst):
    def chage(txt):
        return txt.capitalize()

    res = []
    for el in lst:
        res.append(chage(el))
    return res

print(big_later(["ukraina", "polska", "bialorus"])) # ['Ukraina', 'Polska', 'Bialorus']

# 2.Даны функции:
# def func1(num):
#     if num > 0:
#         num += 2
#     return num

# def func2(iter):
#     res = []
#     for el in iter:
#         res.append(func1(el))
#     return res
# Перепишите код так, чтобы func1 была внутренней функцией для func2.

def func2(iter):
    def func1(num):
        if num > 0:
            num += 2
            return num

    res = []
    for el in iter:
        res.append(func1(el))
    return res
print(func2([1, 3, 47, 92])) # [3, 5, 49, 94]
