import re

# 1.Дана строка:
# '''
# 	abc
# 	def
# 	ghi
# 	jkl
# '''
# Напишите регулярку, которая сделает из этой строки следующую:
# '''
# 	abc!
# 	def!
# 	ghi!
# 	jkl!
# '''
txt =  '''
	abc
	def
	ghi
	jkl
'''
res = re.sub('\n', '!\n' , txt)
print(res) 

# 2.Дана строка:
# '''
# 	abc
# 	def
# 	ghi
# 	jkl
# '''
# Напишите регулярку, которая сделает из этой строки следующую:
# '''
# !	abc
# !	def
# !	ghi
# !	jkl

txt = '''
	abc
	def
	ghi
	jkl
'''
res = re.sub('\t', '!', txt)
print(res) 

# 3.Дана строка:
# '''
# 	abc
# 	def
# 	ghi
# 	jkl
# '''
# Напишите регулярку, которая сделает из этой строки следующую:
# '''!
# 	abc
# 	def
# 	ghi
# 	jkl
# !'''

txt = '''
	abc
	def
	ghi
	jkl
'''
res = re.sub('^|$', '!', txt)
print(res) 

# 4.Дана строка:
# '''
# 	abc
# 	def
# 	ghi
# 	jkl
# '''
# Напишите регулярку, которая сделает из этой строки следующую:
# '''!
# !	abc
# !	def
# !	ghi
# !	jkl
# !'''

txt = '''
	abc
	def
	ghi
	jkl
'''
# res = re.sub('^|$|\t', '!', txt)
res = re.sub('\n|^\s*|\s*$', '!', txt)
print(res) 

# 5.Дана строка:
# '''
# 	abc
# 	def
# 	ghi
# 	jkl
# '''
# Напишите регулярку, которая сделает из этой строки следующую:
# '''!
# 	abc!
# 	def!
# 	ghi!
# 	jkl!
# !'''

txt = '''
	abc
	def
	ghi
	jkl
'''
res = re.sub('\n', '!\n',  txt)
print(res) 

# 6.Дана строка:
# '''
# 	abc
# 	def
# 	ghi
# 	jkl
# '''
# Напишите регулярку, которая сделает из этой строки следующую:
# '''
# 	!abc
# 	!def
# 	!ghi
# 	!jkl
# '''

txt = '''
	abc
	def
	ghi
	jkl
'''

res = re.sub('\n', '!',  txt)
print(res) 