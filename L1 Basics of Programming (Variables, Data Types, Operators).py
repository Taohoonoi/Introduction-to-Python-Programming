# single line comment

'''
multiline comments
'''

# Variables
x = 5
y = "Name"

# Data Types
# int, float, str, bool, list, tuple, dict, set
x: int = 5
y: float = 5.0
charater: str = 'c'
name: str = "Name" # is a sequence of characters
x: bool = True
x: list = [1, 2, 3]

x: tuple = (1, 2, 3)
x: dict = {"name": "John",
           "age": 36,
           "country": "Norway"}
x: set = {"apple", "apple", "banana", "cherry"}

# Operators
# Arithmetic Operators
x = 5
y = 3
print(x + y)  # 8
print(x - y)  # 2

print(x * y)  # 15 multiplication is repeated addition 5*3 = 5+5+5
print(x ** y)  # 125 x^y rasied to the power is repeated multiplication 5^3 = 5*5*5

print(x / y)  # 1.6666666666666667 = 3/3 + 2/3 = 1 + 0.6666666666666667
print(x // y)  # 1 floor division = 3/3 = 1
print(x % y)  # 2 remainder = 2/3 = 2


# Assignment Operators
x = 5
x += 3  # x = x + 3
x -= 3  # x = x - 3
x *= 3  # x = x * 3
x /= 3  # x = x / 3
x %= 3  # x = x % 3

# Comparison Operators value
x = 5
y = 3
z: bool = (x == y) # bool False
print(z)
z: bool = (x != y) # bool True

# Logical Operators
age = 15
z: bool = (age > 18 and age < 35)  # True

# Identity Operators memory location
x = 5
y = x
z: bool = (x is y)  # True

# Membership Operators
x = ["apple", "banana"]
z: bool = ("apple" in x)  # True

# Bitwise Operators
x = 5 # to binary 101
y = 7 # to binary 111
z = (x & y)  # 101_b2 & 111_b2 = 101_b2 = 5_b10
z = (x | y)  # 101_b2 | 111_b2 = 111_b2 = 7_b10
z = (x ^ y)  # 101_b2 ^ 111_b2 = 010_b2 = 2_b10
z = (x << 2)  # 101_b2 << 2 = 10100_b2 = 20_b10
z = (x >> 2)  # 101_b2 >> 2 = 1_b2 = 1_b10