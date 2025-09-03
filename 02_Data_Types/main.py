# =========Python Data Types===========

# Data types determine the type of value a variable can hold and the operations that can be performed on it. They define the format, structure, size, range, and behavior of data, controlling how it's stored and used in a program. This helps ensure data is used correctly and efficiently.

#=========== 1. Numeric Types=========
# Python has three main numeric types:

# a. Integer (int)
# Whole numbers, positive or negative, without decimals.
num_int: int = 42

print(type(num_int)," num_int = ",num_int,) 

# b. Float (float)
# Numbers that contain a decimal point, representing real numbers.
num_float: float = 3.14
print(type(num_float)," num_float = ",num_float,) 

# c. Complex (complex)
# Numbers with a real and imaginary part, represented as a + bj.
num_complex: complex = 2 + 3j
print(type(num_complex)," num_complex = ",num_complex,) 

# Accessing Real and Imaginary Parts
# Python provides attributes .real and .imag to extract the real and imaginary parts of a complex number.
z = 3 + 4j

print("Real Part:", z.real)   # Output: 3.0
print("Imaginary Part:", z.imag)  # Output: 4.0
print(type(z)," z = ",z,)

# ==============2. Boolean (bool)========

#Represents True or False.
is_python_fun: bool = True #False

print(type(is_python_fun), " is_python_fun = ", is_python_fun)

#==============3. Sequence Types========
# Sequence types store multiple items in an ordered manner.

# a. String (str)
# A sequence of characters enclosed in quotes.
text_double: str  = "Hello, Python!" 
text_single: str  = 'Hello, Python!' 
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    
print(type(text_single), " text_single   = ", text_single)    
print(type(text_multi), " text_multi    = ", text_multi)      
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)

# b. List (list)
# An ordered, mutable collection.
fruits: list = ["apple", "banana", 20, True, 3.14, 3j]
print(type(fruits), " fruits = ", fruits)

# c. Tuple (tuple)
# An ordered, immutable collection.
tuple_example: tuple = ("apple", "banana", 20, True, 3.14, 3j)
print(type(tuple_example), " tuple_example = ", tuple_example)

# 4. Set Types (set)
# An unordered collection of unique elements.
fruits_set: set = {1,2,2, 3,5}
print(type(fruits_set), " fruits_set = ", fruits_set)

# b. Frozen Set (frozenset)
# Immutable version of a set.
fruits_frozenset: frozenset = frozenset([11,2,3,3,4,5])
print(type(fruits_frozenset), " fruits_frozenset = ", fruits_frozenset)

#================5. Mapping Type==========
# Dictionary (dict) Stores key-value pairs.
my_dict: dict = {
    "name": "Alice",
    "age": 25,
    "language": "Python"
    }
print(type(my_dict)," my_dict = ", my_dict )  

