# & (and)
a = 6 # 00000110
b = 12 #00001100
c = a & b #  00000100 --> 4
print(c)
# both bits to compare should be 1 in order to have 1


# | (or)
d = 6  #00000110
e = 12 #00001100
f = d | e#00001110 ---> 14
print(f)
# the result can be one if just one bit is 1 or both are 1

# ^ (exclusive or)
# the result can be one if only one of the bits is one
d = 6  #00000110
e = 12 #00001100
f = d ^ e#00001010 ---> 10
print(f)

# << (shift a bit to the left) (each time u shift the value doubles)
d = 6 << 1  #00001100
print(d)

# >> (shift a bit to the right) (each time u shift the value caught in half)
d = 6 >> 1  #00001100
print(d)