# 1
st1 = {'1', '3', '5'}
st2 = {'6', '8', '1', '3'}
res = st2.difference(st1)
print(res) # {'6', '8'}

# 2
st1 = {'a', 'b', 'c', 'd', 'e'}
st2 = {'d', 'e', 'f', 'g', 'h'}
res = st1.difference(st2)
print(res) # {'a', 'b', 'c'}

# 3
st1 = {1, 2, 4, 5}
st2 = {1, 2, 3, 6}
st3 = {1, 2}
st4 = st1 ^ st2
print(st4) #{3, 4, 5, 6}

# 4
st1 = {1, 3, 6, 8}
st2 = {5, 8, 10, 2}
st3 = {12, 7, 3, 1}
st4 = st1 - st2
st5 = st4.intersection(st3)
print(st4)
print(st5) # {1, 3}