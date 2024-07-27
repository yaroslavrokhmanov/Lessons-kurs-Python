# 1
# Дан список. Проверьте, что все его элементы являются положительными числами.
num = [1, 5, 8, 6, -8, 7]
flag = True
for elem in num:
    if elem < 0:
     flag = False
print(flag) # False

# 2
# Дано целое число. Проверьте, является ли оно простым, то есть делится только на единицу и на само себя.
num = 200
flag = True
if num <= 1:
    flag = False
else:
    for el in range(2, num):
        if num % el == 0:
            flag = False
            break

print(flag) # False