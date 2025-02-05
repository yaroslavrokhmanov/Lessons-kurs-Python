# 1.Перепишите следующий код через лямбда-функцию:
# def func(num):
# 	return num + 1
# lst = [1, 2, 3, 4, 5]
# res = map(func, lst)
# print(list(res))

lst = [1, 2, 3, 4, 5]
res = map(lambda num: num + 1, lst)
print(list(res)) # [2, 3, 4, 5, 6]


# 2.Перепишите следующий код через лямбда-функцию:
# def func(txt):
# 	return txt[::-1]
# lst = ['123', '456', '789']
# res = map(func, lst)
# print(list(res))

lst = ['123', '456', '789']
res = map(lambda txt: txt[::-1], lst)
print(list(res)) # ['321', '654', '987']



