# 1
st1 = {'x', '1', 'y', '2', 'z'}
st2 = {1, 2, 3, 4, 5, 6}
res1 = len(st1)
res2 = len(st2)
print(res1) # 5
print(res2) # 6
if res1 > res2:
    print('st1' + ' Больше ' + 'st2')

if res2 > res1:
  print('st2' + ' Больше ' + 'st1') # st2 Больше st1

#2
num1 = 12345
num2 = 12321
set1 = set(str(num1))
set2 = set(str(num2))
res = set1 & set2
print(set1)
print(set2)
print(res) # общие числа {'2', '3', '1'}

# 3
tst1 = 34
tst2 = [1, 2, 5]
tst3 = (6, 7, 8)
st1 = set(str(tst1))
st2 = set(tst2)
st3 = set(tst3)
print(st1) # {'4', '3'}
print(st2) # {1, 2, 5}
print(st3) # {8, 6, 7}

# 4
st = {'18', '24', '34', '47', '81', '63'}
tst1 = '34'
tst2 = ('81', '12', '46')
st1 = {tst1}
st2 = set(tst2)
res1 = st.intersection(st1)
res2 = st.intersection(st2)
print(res1) # {'34'}
print(res2) # {'81'}

#5
num1 = 12345
num2 = 45123
st1 = set(str(num1))
st2 = set(str(num2))
res = st1 == st2
print(res) # True

# 6
num1 = 12345
num2 = 45678
st1 = set(str(num1))
st2 = set(str(num2))
res  = st1 & st2
print(res) # {'4', '5'}

# 7
st1 = {'ab', 'b', 'ce', 'de', 'd'}
st2 = {'ef', 'd', 'ab', 'bc'}
st3 = {'a', 'g', 'b', 'c'}
res  = st1 & st2
res1 = res | st3 
print(res) # {'d', 'ab'}
print(res1) # {'d', 'ab', 'a', 'c', 'g', 'b'}

# Найдите общие элементы для первых двух множеств. А затем объедините полученное множество с st3.




