# 1.Дан следующий код:

def outer():
	i = 10

	def inner():
		nonlocal i
		i -= 2
		print(i)
	return inner
	
res1 = outer() 
res1() # 8
res1() # 6

res2 = outer()
res2() # 8
res2() # 6
res2() # 4
# Скажите, что выведется в консоль.


# 2Сделайте функцию, каждый вызов которой будет вызывать следующее число Фибоначчи.

def fibo():
    num1 = 0
    num2 = 1

    def func():
        nonlocal num1, num2
        result = num1
        num1, num2 = num2, num1 + num2
        return result
    return func
res = fibo()
print(res())
print(res())
print(res())
print(res())
print(res())
print(res())
print(res())

