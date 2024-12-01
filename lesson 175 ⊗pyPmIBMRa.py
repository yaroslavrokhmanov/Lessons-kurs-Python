import random
# 1.Даны два целых числа:
num1 = 10
num2 = 20
# Сгенерируйте случайное целое число из диапазона, заданного нашими числами.
print(random.randint(num1, num2)) #20

# 2.Даны два целых числа:
num1 = 5
num2 = 30
# Сгенерируйте псевдослучайное целое число из диапазона, заданного нашими числами.
print(random.randint(num1, num2)) #14

# 3.Даны два дробных числа:
num1 = 1.345
num2 = 14.784
# Сгенерируйте псевдослучайное вещественное число из диапазона, заданного нашими числами.
print(random.uniform(num1, num2)) # 13.039669620612191

# 4.Даны два целых числа:
num1 = -2
num2 = 10
# Сгенерируйте случайное вещественное число из диапазона, заданного нашими числами.
print(random.uniform(num1, num2)) # -1.8590464725884357

# 5.Даны три числа:
num1 = 5
num2 = 50
num3 = 4
# Сгенерируйте случайное число из диапазона, заданного первым и вторым числом. Третье число пусть определяет шаг выборки.
print(random.randrange(num1, num2, num3)) #5

# 6.Дан список:
lst = [1, 2, 3, 4, 5]
# Получите случайный элемент из этого списка.
print(random.choice(lst)) # 1

# 7.Дан список:
lst = [1, 2, 3, 4, 5]
# Получите новый список, состоящий из трех случайных элементов исходного списка.
print(random.sample(lst, 3)) #[5, 1, 2]

# 8.Дан список:
lst = [1, 2, 3, 4, 5]
# Перемешайте элементы этого списка в случайном порядке.
random.shuffle(lst)
print(lst) # [1, 4, 5, 3, 2]

# 9.Дан список с дублями:
lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]
# Получите три случайных элемента из списка так, чтобы в выборке элементы не повторялись.
print(random.sample(lst, 3)) # [2, 5, 1]

# 10.Дано число:
num = 7
# Инициализируйте его.
random.seed(num)
print(num) #7

# 11.Дан кортеж:
tlp = (10, 6, 2, 4)
# Получите из него случайное число, а затем инициализируйте его.
random.seed(str(tlp))
print(random.choice(tlp)) #2