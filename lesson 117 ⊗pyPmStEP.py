# 1
st = {1, 2, 3, 4, 5}
num = 3
res = num in st
print(res) # True

# 2
st1 = {'1', '2', '3'}
st2 = {'4', '5', 3}
print('3' in st1 & st2) # False

# 3
st = {'ab', 'bc', 'cd'}
txt = 'bc'
print(txt not in st) # False

# 4
st = {'x', 'y', 'z', 'w'}
txt = 'yz'
print(txt not in st) # True

