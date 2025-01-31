# 1.Каким будет результат выполнения следующего кода:
def func(num1, num2, *, num3):
	return (num1 + num2) * num3
	
print(func(2, 4, num3=3)) # 18

# 2.Каким будет результат выполнения следующего кода:
def func(num1, *, num2, num3):
	return (num1 - num2) / num3
	
# print(func(12, 4, num3=5))  # oshibka niet znaczenia num2 = ?

# 3.Каким будет результат выполнения следующего кода:
def func(*, name='user1', age='18'):
	return 'Username is ' + name + ' age is ' + age
	
print(func(name='john')) # Username is john age is 18