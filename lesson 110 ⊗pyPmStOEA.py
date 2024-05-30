# 1
st = {1, 2, 3}
st.add(4)
print(st) # {1, 2, 3, 4}

# 2
txt1 = 'xyz'
txt2 = 'xzy'
txt3 = 'xyz'
st.add(txt1)
st.add(txt2)
st.add(txt3)
print(st) #{1, 2, 3, 4, 'xzy', 'xyz'}