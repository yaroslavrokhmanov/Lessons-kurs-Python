# # 1
# # Напишите условие, которое будет проверять является ли заданное в переменной число четным или нет.

# num = 10
# if num % 2 == 0:
#     print('четное') # четное
# else:
#     print('не четное')

# # 2
# # Пусть у вас есть переменная со строкой. Если она содержит символ 'a', то пусть он будет заменен на '!'.

# str = 'abcde'
# if 'a' in str:
#     str = str.replace('a', '!') # !bcde
# print(str)

# # 3
# Исправлена ошибка!!!

# # Дана переменная, в которой будет сохраняться электронная почту пользователя. Проверьте содержит ли она символ '@'. Если данного символа нет, то пусть пользователь повторно введет правильную почту.

while True:
    str = input('Введите почту: ')
    if '@' not in str:
        print('Отсутствует "@",  еще раз.')
    else:
        print(str)
        break


# # 4
# # Дана переменная, в которой будет сохраняться имя пользователя. Напишите условие, которое будет проверять длину имени. Если длина меньше 3, то выведется сообщение о том, что имя слишком короткое. Если длина попадает в интервал от 3 до 20 символов, оно является корректным. При превышении 20 символов,, пусть появится сообщение о необходимости сокращения имени.

# name = input('Your name?')
# if < len(name) < 3:
#     print('имя слишком короткое')
# elif 3 <= len(name) <= 20:
#     print('является корректным')
# elif len(name) > 20:
#     print('необходимо сокращения имени')




# # 5
# # Дана переменная, в которой будет хранится пароль для входа на сайт. Напишите проверку на то, чтобы пароль не был пустым. Также проверьте, чтобы его длина была в пределах 6 - 14 символов.
# num = input('введите пароль')
# if len(num) == 0:
#     print('пароль пустой')
# elif 6 <= len(num) <= 14:
#     print('OK')
# else:
#     print('введтите еще раз ')

# # 6
# # Дан следующий код:
# # tst = 'abcdef'
# # if len(tst) > 20:
# # 	print('string is too long')
# # else:
# # 	print('string is too short')
# # Перепишите его с помощью тернарного оператора.

# tst = 'abcdef'
# print('string is too long' if len(tst) > 20  else 'string is too short') # string is too short







    

