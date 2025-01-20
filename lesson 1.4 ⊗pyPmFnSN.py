# 1.Каким будет результат выполнения следующего кода:
tst = '12'

def func():
	tst = 12
	return tst
	
print(tst) # 12

# 2.Каким будет результат выполнения следующего кода:
tst = 'abc'

def func():
	tst = tst.upper()
	return tst 

func()
print(tst) # niczego nie wyweditsa tst nie obyavlena

# 3.Каким будет результат выполнения следующего кода:
# tst = 'abc'

# def func():
# txt = tst.upper()
# return txt
		
# print(func())
# print(tst) # oshibka nie wyweditsa v txt zapisyvaem tst kotoraya nie obyavlena