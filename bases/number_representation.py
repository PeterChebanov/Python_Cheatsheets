""""Exponential representation"""

a = 2e-1  # 0.01 -->> 2 * 10 in power(-1)
b = 3e3  # 3000 -->> 3 * 10 in power(3)
c = 4e-2  # 0.04 -->> 4 * 10 in power(-2)

d = 3e20  # 3e+20 -->> very big numbers represented in exponential view -->> 3 * 10 in power(20)
e = 3e-20  # 3e-20 -->> very small numbers represented in exponential view -->> 3 * 10 in power(-20)
print(d)
print(e)

"""Binary representation"""

bin_001 = 0b001
print(f"001 in decimal: {bin_001}")  # 1

bin_0011101110100001 = 0b0011101110100001
print(f"0011101110100001 in decimal: {bin_0011101110100001}")  # 15265

bin_negative_001 = -0b001
print(bin_negative_001)  # -1

to_bin_1 = bin(1)
print(to_bin_1)  # 0b1

to_bin_100500 = bin(100500)
print(to_bin_100500)  # 0b11000100010010100

"""Hexadecimal representation"""

hex_26 = 0x1A
print(hex_26) # 26

hex_222 = 0xde
print(hex_222)# 222

hex43583 = 0xaa3f
print(hex43583)# 43583

hex_negative_842 = -0x34a
print(hex_negative_842) # -842

"""Bit operations"""

print('*'*50)
print("Bit operations:")
print('_'*50)
#operation NO => reverse all bits ex: 00000000 00000000 00000000 -->> 11111111 11111111 11111111
print("NO operation '~': ")
var_1 = 121
print(bin(var_1)) #0b1111001
var_1 = ~var_1
print(var_1) #-122
print(bin(var_1))

print('_'*50)
#operation AND =>
"""Table of truth of AND OPERATION:
    x1  x2 result
    0   0   0
    0   1   0
    1   0   0
    1   1   1
    """

print("AND operation '&': ")

four = 4
five = 5
print(four & five) #4
print('_'*50)
""" why 4 is result:
four:   0 0 0 0 0 1 0 0    
five:   0 0 0 0 0 1 0 1    
result: 0 0 0 0 0 1 0 0
""" #result has the same bit representation as 4



"""OR  '|' """
print("OR operation '|': ")
three = 3
four = 4

"""Table of truth of OR operation:
x1  x2  result:
0   0   0
1   0   1
0   1   1
1   1   1
"""

print(three | four) #7
""" why 7 is result:
three:  0 0 0 0 0 0 1 1    
four:   0 0 0 0 0 1 0 0    
result: 0 0 0 0 0 1 1 1
""" #result has the same bit representation as 7
print(0b00000111) #7
print('_'*50)

"""XOR """

"""Table of truth of XOR operation:
x1  x2  result:
0   0   0
1   0   1
0   1   1
1   1   0
"""

print("XOR operation '^'")

nine = 9
one = 1

nine ^= one
print(nine) #8 -> we have switched the bit
print('_'*50)
nine ^= one
print(nine) # 9 -> we have switched the bit to initial state == 9


"""SHIFT BITS """
h = 160
print(bin(h))# 0b10100000

h = h >> 1 #shifitng 1 bit to the right will devide the initial value on 2
print(h) #80
print(bin(h))# 0b1010000

h = h >> 2 #will divide the initial number on 2 in power(2)
print(h) #20

h = h >> 3 # the same is 20/8 --> as shifting on 3 bits to the right is 20 / 2 in power(3)
print(h)


h = h << 4 # will multiply 2 on 2 in power(4)
print(h) #32
print(bin(h))# 0b100000

"""Bit shifts works much more fast then traditional math operators like '*', '/', and highly in use on memory limited machines"""