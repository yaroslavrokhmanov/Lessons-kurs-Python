# 1.Каким будет результат выполнения следующего кода:

def func(txt):
	txt = 'user2'
	return txt

name = 'user1'

res = func(name)
print(res) # user2
print(name) # user1

# 2.Каким будет результат выполнения следующего кода:

def func(tst1, tst2):
	tst1 += 1
	tst2 *= 2
	return tst1 + tst2

num1 = 0
num2 = 2

res = func(num1, num2)
print(num1 + num2) # 2
print(res) # 5