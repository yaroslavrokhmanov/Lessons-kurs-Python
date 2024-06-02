# 1
st = {'1', '2', '3', '4', '5', '6'}
txt = '123456'
res = st.issubset(txt)
print(res) # True

# 2
st = {'ab', 'cd', 'ef'}
tlp = ('ab', 'cd', 'ef')
res = st.issubset(tlp)
print(res) # True

# 3
st1 = {1, 2, 3, 4, 5}
st2 = {1, 2, 3}
res = st2 <= st1
print(res) # True