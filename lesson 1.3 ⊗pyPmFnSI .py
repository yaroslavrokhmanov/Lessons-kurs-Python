# 1.Каким будет результат выполнения следующего кода:

num = 10

def func():
	num = 5
	return num

func()
print(num) # 10

# 2.Каким будет результат выполнения следующего кода:

num = 3

def func():
	num = 4
	return num

num = func()
print(num) # 4

# 3.Каким будет результат выполнения следующего кода:

num = 1

def func():
	num = 2
	return 1

num = func()
print(num) # 1

# 4.Каким будет результат выполнения следующего кода:

num1 = 1

def func():
	num2 = 2

func()
print(num1) # 1

# 5 Каким будет результат выполнения следующего кода:

num1 = 1

def func():
	num2 = 2

func()
# print(num2) # oshibka, nie zadano znachenie

# 6.Каким будет результат выполнения следующего кода:

num1 = 1

def func():
	num2 = 2

func()
num2 = 3
print(num2) # 3

# 7.Каким будет результат выполнения следующего кода:

num1 = 1
num2 = 2

def func():
	num2 = 3

func()
print(num2) # 2

# 8.Каким будет результат выполнения следующего кода:

num1 = 1

def func():
	num1 = 2

print(num1) # 1