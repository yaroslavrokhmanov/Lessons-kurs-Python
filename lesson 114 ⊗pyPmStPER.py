# 1
st = {'x', 'y', 'z'}
st.discard('y')
print(st) # {'x', 'z'}

# 2
st = {1, 2, 3, 4, 5}
st.discard(2)
st.discard(4)
print(st) # {1, 3, 5}

# 3
st = {'ab', 'cd', 'ef'}
st.discard('b')
print(st) #{'ab', 'cd', 'ef'} если нет значения 'b' выводится исходное множество 