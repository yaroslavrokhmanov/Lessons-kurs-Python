# 1
st1 = {'a', 'b', 'c', 'd', 'e'}
st2 = {'d', 'e', 'f', 'g', 'h'}
res = st1.symmetric_difference(st2)
print(res) # {'b', 'c', 'h', 'f', 'a', 'g'}

# 2
st1 = {2, 4, 8, 10}
st2 = {1, 8, 3, 2}
st3 = {4, 7, 3, 1}
st4 = st1.symmetric_difference(st2)
res = st3.symmetric_difference(st4)
print(res) # {7, 10}
