#==============Operator and Operand===========
# In Python (and programming in general), an operand is a value or variable that an operator acts on. Think of it like this:

# Operator: A symbol that performs an operation (e.g., +, -, *, /).
# Operand: The value(s) or variable(s) that the operator works with.

# Key Points:
# Operands are the "inputs" for an operator.
# The number of operands depends on the operator:
# Unary operators (e.g., not, -) work with one operand.
# Binary operators (e.g., +, -, *, /) work with two operands.

# Unary Operators
# Unary operators work with one operand (a single value or variable). They perform operations on just one thing.

# Examples:
# Negative (-):
# Changes the sign of the operand.

from doctest import Example


x = 5
y = -x  # y is now -5
print("y = ", y)

# 2.Logical NOT (not):
# Reverses a boolean value.
a = True
b = not a  # b is now False
print("b = ", b)

# Bitwise NOT (~):
# Inverts the bits of a number (used in binary operations).

x: int = 5  # Binary: 0101
y: int = ~x  # y is now -6 (binary: 1010, but in two's complement form)
print("y = ", y)

#==================Operators in Python=======
# Operators in Python are symbols used to perform operations on variables and values. Python supports several types of operators:
# 1. Arithmetic Operators
# Used for basic mathematical operations.

# Operator	Name	Example
# +	     Addition	 5 + 2 = 7
# -  	Subtraction	 5 - 2 = 3
# * 	Multiplication	 5 * 2 = 10
# /	   Division (float)	 5 / 2 = 2.5
# //	Floor Division	 5 // 2 = 2 (removes decimal part)
# %	  Modulus (remainder)	 5 % 2 = 1
# **	Exponentiation	 5 ** 2 = 25
a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
print("a % b  = ", a % b)   # 1 Modulus (remainder)
print("a % b  = ", a ** b)  # 1000 Exponentiation (10 * 10 * 10)

# 2. Comparison (Relational) Operators
# Used to compare two values.


# Operator	Name	Example
# ==	 Equal	    5 == 5 → True
# !=	Not equal	5 != 3 → True
# > 	Greater than	5 > 3 → True
# < 	Less than	5 < 3 → False
# >=	Greater than or equal	5 >= 5 → True
# <=	Less than or equal	5 <= 3 → False

x: int = 10
y: int = 5

print("x == y = ", x == y)  # False, Equal
print("x != y = ", x != y)  # True, Not equal
print("x > y  = ", x > y)   # True, Greater than
print("x < y  = ", x < y)   # False, Less than
print("x >= y = ", x >= y)  # True, Greater than or equal
print("x <= y = ", x <= y)  # False, Less than or equal


#What Are Chained Comparison Operators?
#In Python, we can chain comparison operators together to express multiple comparisons in a single line. This allows for more readable and concise code. Rather than writing multiple comparisons with the same variable repeatedly, Python lets us combine them.

x: int = 15
if 10 < x < 20:
    print("x is between 10 and 20")
    
    # Internally, Python interprets this as:
if 10 < x and x < 20:
    print("x is between 10 and 20")
    
# 3. Logical Operators
# Used to combine conditional statements.


# Operator	Name	Example
# and	Logical AND	(5 > 3 and 10 > 5) → True
# or	Logical OR	(5 > 3 or 10 < 5) → True
# not	Logical NOT	not(5 > 3) → False
x: bool = True
y: bool = False

print("x and y = ", x and y)  # False
print("x or y  = ", x or y)   # True
print("not x   = ", not x)    # False

# 4. Assignment Operators
# Used to assign values to variables.


# Operator	Example	Equivalent To
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# //=	x //= 3	x = x // 3


x = 5
print("Assignment: x = 5                    ",x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ",x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ",x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ",x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ",x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ",x)  # Output: 1.0

# 5. Identity Operators
# Used to compare memory locations.


# Operator	Name	Example
# is	Returns True if objects have the same memory location	x is y
# is not	Returns True if objects do not have the same memory location	x is not y


a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

print('\n-----\n') # seperator for better output readability

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))

# 6. Membership Operators
# Used to check if a value is in a sequence (list, tuple, set, dictionary, etc.).


# Operator	Name	Example
# in	Returns True if value is in the sequence	x in list
# not in	Returns True if value is NOT in the sequence	x not in list
my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  # True

print("\n-----\n")

my_string: str = "Operation Badar"

print("my_string                 = ", my_string)                # Operation Badar
print("'O' in my_string          = ", 'O' in my_string)         # True
print("'Hello' not in my_string  = ", 'Hello' not in my_string) # True

# Python Keywords
# Keywords in Python are reserved words that have special meanings and serve specific purposes in the language syntax. Python keywords cannot be used as the names of variables, functions, and classes or any other identifier.
import keyword

# Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
print("The list of \
keywords is : ")

# printing all keywords at once using "kwlist()"
print(keyword.kwlist)
