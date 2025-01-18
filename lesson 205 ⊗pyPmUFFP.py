# 1.Дан следующий код:

num1 = 2
num2 = 3
def func(num1, num2):
    pass # чтобы избежать вывода ошибки
res = func(num1, num2)
print(res)
# Перепишите его, чтобы избежать вывода ошибки.

# 2.Дан следующий код:

tst1 = 'abc'
tst2 = 'def'

def func1(txt):
	return txt.upper()
	
def func2(txt1, txt2):
    pass # чтобы избежать вывода ошибки
res = func2(func1(tst1), tst2)
print(res)
# Перепишите его, чтобы избежать вывода ошибки.