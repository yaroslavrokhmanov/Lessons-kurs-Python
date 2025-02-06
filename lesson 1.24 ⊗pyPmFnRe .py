# 1.Выведите все числовые элементы словаря произвольного уровня вложенности:
elems = {
	'a': {
		'b': 1,
		'c': 2,
		'd': {
			'e': 3,
			'f': 4
		}
	},
	'j': {
		'h': 5,
		'k': 6,
	},
	'l': 7
}

def func(elem):
    res = []
    for key, value in elem.items():
        if isinstance(value, dict):
            res.extend(func(value))
        else: 
            if isinstance(value, (int)):
                res.append(value)
    return res

print(func(elems)) #[1, 2, 3, 4, 5, 6, 7]

# 2.Найдите сумму элементов словаря из предыдущей задачи.
elems = {
	'a': {
		'b': 1,
		'c': 2,
		'd': {
			'e': 3,
			'f': 4
		}
	},
	'j': {
		'h': 5,
		'k': 6,
	},
	'l': 7
}

def sum_elems(num):
    res = 0
    for key, value in num.items():
        if isinstance(value, dict):
            res += sum_elems(value)
        elif isinstance(value, int):
            res += value
    return res
print(sum_elems(elems)) # 28

# 3.Получите список примитивных элементов словаря из предыдущей задачи.
elems = {
	'a': {
		'b': 1,
		'c': 2,
		'd': {
			'e': 3,
			'f': 4
		}
	},
	'j': {
		'h': 5,
		'k': 6,
	},
	'l': 7
}

def primitiv_elems(el):
    res = []
    for key, value in el.items():
        if isinstance(value, (int, float, str, bool, type(None))):
            res.append(value)
        elif isinstance(value, dict):
            res.extend(primitiv_elems(value))
    return res

print(primitiv_elems(elems)) # [1, 2, 3, 4, 5, 6, 7]
