# 1.Дан следующий код:
def outer():
	def inner(num):
		return num + 2

	return inner
	
res = outer()(3)
print(res) # 5
# Скажите, что выведется в консоль.


# 2.Дан следующий код:
def outer():
	def inner(txt):
		return 'hello, ' + txt

	return inner
	
res = outer()
print(res) # vividetsa objekt funkcii <function outer.<locals>.inner at 0x000002728429A200>
# Скажите, что выведется в консоль. 