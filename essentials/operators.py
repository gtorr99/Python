# # Arithmetic Operators

# # ** -> exponential
# # // -> floor division

# a = 2
# b = 3

# print(a ** b)
# print(a // b)

# print(b ** a)
# print(b // a)

# b = 6
# b //= 2
# print(b)

# b **= 10
# print(b)

# # --------------------------------------------------------

# # Bitwise
# # &  - AND
# # |  - OR
# # ^  - XOR
# # ~  - One's Complement (flips the number)
# # << - Left Shift  ("walk" 3 to left)
# # >> - Right Shift ("walk" 3 to right)

# a = 2 # 10 = 00000010
# b = 3 # 11 = 00000011

# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)
# print(~b)
# print(a << b) # 2 << 3 => 00000010 << 3 = 00010000
# print(a >> b) # 2 >> 3 => 00000010 << 3 = 00000000

# # --------------------------------------------------------

# # Logical
# # and / or / not

# print(a==b and b==3)
# print(a==b or b==3)
# print(not(a==b) and b==3)

# # --------------------------------------------------------

# Membership Operators
# in / not in

# a = [10,20]

# print(10 in a)
# print(30 not in a)

# --------------------------------------------------------

# Identity Operators
# is / is not
# 
a = 10
b = 10

print(a is b)       # True
print(a == b)       # True

b = 10.0
print(a is b) # False
# "is" checks if objects appoint to the same value

print(a == b)  # True
# "==" checks if values are equal

print(a is not b)   # False
