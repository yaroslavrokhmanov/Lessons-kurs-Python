# 1
st1 = {1, 3, 6, 8}
st2 = {5, 8, 4, 2}
st3 = {4, 7, 3, 1}
st4 = st1 | st3
st5 = st4 & st3
print(st4) # {1, 3, 4, 6, 7, 8}
print(st5) # {1, 3, 4, 7}

# 2
st1 = {4, 2, 6, 10}
st2 = {1, 6, 3, 2}
st3 = {5, 8}
st4 = {6, 3, 1}
st5 = st1 - st2
st6 = st3 | st4
res = st5.intersection(st6)
print(st5)
print(st6)
print(res)
res = set()  # set() Пустое множество. Hет общих элементов