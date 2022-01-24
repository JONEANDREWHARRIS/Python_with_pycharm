a = 5 # 101 (3 bits)
b = 6 # 110 (3 bits)

a = a ^ b  #11 (4 bits) so we waste one extra bit
b = a ^ b #5
a = a ^ b #6
print(a,b)
# this is how we swamp the variables
print(bin(a))
print(bin(b))
a = 5 # 101 (3 bits)
b = 6 # 110 (3 bits)

a,b = b,a
# this is how we swamp the variables

print(a,b)
