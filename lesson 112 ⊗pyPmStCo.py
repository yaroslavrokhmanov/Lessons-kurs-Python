# 1
st1 = {'a', 'b', 'c', 'd', 'e'}
st2 = {'d', 'e', 'f', 'g', 'h'}
st1.update(st2)
print(st1) # {'g', 'a', 'b', 'h', 'e', 'f', 'c', 'd'}

# 2
st1 = {'2', '4', '6'}
st2 = {7, 8, 9}
st3 = {'1', '3', '4'}
st1.update(st2, st3)
print(st1) # {'3', 7, 8, '2', 9, '4', '1', '6'}

# 3
st1 = {1, 2, 3}
st2 = {'a', 'b', 'c'}
st3 = {4, 5, 6}
st4 = {'d', 'e', 'f'}
st1 = st1 | st3
st2 = st2 | st4
print(st1) # {1, 2, 3, 4, 5, 6}
print(st2) # {'e', 'b', 'f', 'a', 'd', 'c'}