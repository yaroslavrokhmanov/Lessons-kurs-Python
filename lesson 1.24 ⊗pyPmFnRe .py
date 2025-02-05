# 1.Выведите все числовые элементы словаря произвольного уровня вложенности:
{
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
            func(elem)
        else: 
            res.append(value)
    return res