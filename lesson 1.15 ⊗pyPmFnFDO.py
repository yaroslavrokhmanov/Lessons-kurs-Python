
# 1.Создайте функцию, которая будет принимать параметром список названий месяцев и выводить их с заглавной буквы. Опишите суть работы функции в документации и выведите ее в консоль.
def mounth_list(mounth):
    'funkcija prinimaet spisok mesacev i wiwodit ih s zaglavnoj bukwy'
    return [el.capitalize() for el in mounth]

mounth_el = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

res = mounth_list(mounth_el)
print(res)
help(mounth_list)

# 2.Выведите всю документацию о функции sum.
help(sum)

# 3.Выведите только строку с документацией о функции len. 
print(len.__doc__) 