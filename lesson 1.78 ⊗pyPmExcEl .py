# Дан список:

lst = [1, 2, 3]
# Напишите код, чтобы перехватить исключение, связанное с делением на ноль. В случае, если данное исключение не появится, пусть выведется длина списка.
try:
    result = 10 / 2
except ZeroDivisionError:
    print('error - 0')
else:
	print(sum(lst))