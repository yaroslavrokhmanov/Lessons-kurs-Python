# 1.В следующем коде некоторый программист допустил ошибку:
# num = 10
# def outer():
# 	num = 5
# 	def inner():
# 		num -= 2
# 	inner()
# 	return num
# print(outer())
# Что не так с этим кодом? Найдите и исправьте ошибку автора кода.

num = 10
def outer():
  num = 5
  def inner():
    nonlocal num # nie objavlena nonlocal dla raboty vnutri funkcii
  num -= 2
  inner()
  return num
print(outer()) # 3

# 2.В следующем коде некоторый программист допустил ошибку:
# num = 3
# def outer():
# 	num += 1
# 	tst = num

# 	def inner():
# 		tst = tst ** 3
# 	inner()
# 	return tst
# print(outer())
# Что не так с этим кодом? Найдите и исправьте ошибку автора кода.

num = 3
def outer():
    global num # global dla raboty i izmememia num
    num += 1 
    tst = num
    return inner(tst)
def inner(tst):
    tst = tst ** 3
    return tst 

print(outer())# 64



