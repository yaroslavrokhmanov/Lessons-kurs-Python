# 1
# Выведите в консоль числа от 1 до 10.
for num in range(1, 11):
    print(num)

# 2
# Выведите в консоль числа от 20 до 10.
for num in range(20, 9, -1):
    print(num)

# 3
# Сформируйте список из чисел от 1 до 5.
res = []
for num in range(1, 6):
    res.append(num)
print(res) # [1, 2, 3, 4, 5]

# 4
# Найдите сумму целых чисел от 1 до 100.
res = 0
for num in range(1, 101):
        res = res + num
        print(res) # 5050
    
