# 1
st = {'x', 'y', 'z', 'w'}
st.update('abxcz')
print(st) # {'a', 'z', 'c', 'w', 'b', 'y', 'x'}

# 2
st = {1, 2, 3}
lst = [3, 4, 5, 6]
st.update(lst)
print(st) #{1, 2, 3, 4, 5, 6}

# 3
st = {'12', '34', '56'}
tlp = (2, 4, 6)

st.update(tlp)
print(st) #{2, 4, 6, '34', '56', '12'}