# 1.Сделайте функцию, которая параметром будет принимать число, а выводить квадрат этого числа.
def func(num):
    print(num**2)
func(3) #9

# 2.Сделайте функцию, которая параметрами будет принимать два числа и выводить их произведение.
def func(num1, num2):
    print(num1* num2)
func(2, 6)

# 3.Сделайте функцию, которая параметром будет принимать число и проверять, четное оно или нет.
def func(num):
    if num%2==0:
        print('czetnoe')
    else:
        print('neczetnoe')
func(3) # neczetnoe

# 4.Сделайте функцию, которая параметром будет принимать список с числами, а возвращать сумму квадратов элементов списка.
def func(lst):
    res = sum(num ** 2 for num in lst)
    print(res)
func([1, 2, 3]) # 14