# Python Variables
# In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value. Unlike many other programming languages, Python variables do not require explicit declaration of type. The type of the variable is inferred based on the value assigned.

# (inferred meaning deduce or conclude (something) from evidence and reasoning rather than from explicit statements.)

# Variables act as placeholders for data. They allow us to store and reuse values in our program.


# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive (myVar and myvar are different).
# Avoid using Python keywords (e.g., if, else, for) as variable names.

# Valid variable names
from sqlalchemy import Delete


name = "Alice"
_age = 25
salary2024 = 50000
my_variable = "Python"

# Invalid variable names
2name = "Bob"          # ❌ Starts with a digit
my-variable = "Error"  # ❌ Contains a hyphen
class = "CS101"        # ❌ Uses a reserved keyword

# Special Naming Cases

# Type	Example	Used For
# Regular Variable	total_cost	General use
# Constant	PI = 3.14159	Constants
# Class Name	BankAccount	Class names
# Private Variable	_password	Internal use (not enforced)
# Private with Name Mangling	__secret_key	Avoid accidental overrides in subclasses
# Special Method	__init__	Built-in methods


# Summary of Naming Conventions
# Convention	Used For	Example
# snake_case	Variables & functions	user_name, total_price
# CamelCase	Classes	BankAccount, DataScienceModel
# UPPER_CASE	Constants	MAX_SPEED, PI
# _single_underscore	Private variable (by convention)	_config
# __double_underscore	Name mangling (avoid external access)	__password
# __dunder__	Special methods	__init__, __str__
# Here are the naming conventions in Python with their respective names:

# CapWords or PascalCase: Class names
# snake_case: Variable names, function names, method names, module names, package names
# UPPER_CASE: Constant names
# dunder (double underscore): Special method names (e.g. __init__, __str__)

# It's worth noting that the official Python style guide, PEP 8, recommends using CapWords for class names and snake_case for variable names, function names, and other identifiers.

# PEP 8 – Style Guide for Python Code

# Assigning Different Values
# We can assign different values to multiple variables simultaneously, making the code concise and easier to read.


[ ]
x, y, z = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax

print(x, y, z)
# 1 2.5 Python

[ ]
x: int, y: float, z: str = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax

print(x, y, z)

# Delete a Variable Using del Keyword
# We can remove a variable from the namespace using the del keyword. This effectively deletes the variable and frees up the memory it was using.
# Assigning value to variable
x: int = 10
print(x)

# Removing the variable from memory using del keyword
del x

# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined
print(x) # NameError: name 'x' is not defined, because we already delete variable x (del x)