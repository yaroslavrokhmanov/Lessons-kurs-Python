# 1
tst1 = 5
tst2 = 8
if tst1 > tst2:
    print('5 больше 8')
elif tst2 > tst1:
    print('8 больше 5') # 8 больше 5
else:
    print('другое')

# 2
# Дана переменная age, в которой лежит возраст пользователя. Напишите условие, когда переменная меньше 18 и больше 10. Затем условие, если число находится в интервале от 18 до 60. Также пропишите сообщение для вывода в консоль, когда число не попадает ни в одно из предыдущих условий.

age = 85
if 18 > age > 10:
    print('')
elif 18 <= age <= 60:
    print('')
else:
    print('число не попадает ни в одно из предыдущих условий') # число не попадает ни в одно из предыдущих условий

# 3
# В переменной day лежит какое-то число из интервала от 1 до 31. Определите в какую декаду месяца попадает это число (в первую, вторую или третью).

day = 11
if 1 <= day <= 10:
    print('1 декада')
elif 11 <= day <= 20:
    print('2 декада') # 2 декада
elif 21 <= day <= 30:
    print('3 декада')
else:
    print('не поддходит')

