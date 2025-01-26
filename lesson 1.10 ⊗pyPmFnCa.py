# 1.Каким будет результат выполнения следующего кода:

def get_Info(txt, func):
	print(func(txt))
	
def func(name):
	return 'user name is ' + name
	
get_Info('john', func) # user name is john