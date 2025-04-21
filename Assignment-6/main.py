# Lession #2
# Python Data Types


# 1. Numeric 
# a. Integer (int)
num_int: int = 42

print(type(num_int)," num_int = ",num_int,)  

# b. Floating-Point (float)
num_float: float = 3.14

print(type(num_float), " num_float = ", num_float) 

# c. Complex (complex)
num_complex: complex = 1 + 3j
print(type(num_complex), " num_complex =",num_complex)
# -------------------------------------------------------------------

# 2. Boolean (bool)
is_python_fun: bool = True #False
print(type(is_python_fun), " is_python_fun = ", is_python_fun)

#--------------------------------------------------------------------

# 3. Sequence Types
# a. String (str)
text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # 
print(type(text_single), " text_single   = ", text_single)    # 
print(type(text_multi), " text_multi    = ", text_multi)      # 
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # 

# b. List (list)
list_numbers: list = [1, 2, 3, 4, 5]
list_strings: list = ["apple", "banana"," cherry"]
list_mixed: list = [1, "apple", 3.14, True]
print(type(list_numbers)," list_numbers =", list_numbers)
print(type(list_strings)," list_strings =", list_strings)
print(type(list_mixed), "list_mixed =", list_mixed)

# c. Tuple (tuple)
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  

# d. Range (range)
my_range: range = range(1, 10, 2) # start, stop , step
print(type(my_range), " my_range =", my_range)
#--------------------------------------------------------------------

# 4. Set Types
# a. set (set)
my_set: set = {1,2,3,4,5}
print(type(my_set), " my_set =", my_set)

# b. Frozen Set (frozenset)
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
print(type(frozen_set), " frozen_set = ", frozen_set) 
#--------------------------------------------------------------------

# 5. Mapping Type
my_dict: dict = {
    "name": "Adnan",
    "age": 20,
    "is_student": True
}
print(type(my_dict), "my_dict =", my_dict)
#--------------------------------------------------------------------

# 6. Binary Types
# a. Bytes (bytes)
byte_data: bytes = b"Hello"
print(type(byte_data), " byte_data = ", byte_data)

# b. Bytearray (bytearray)
byte_array: bytearray = bytearray([65, 66, 67, 69]) #65=A, 66=B ....decimal number system
print(type(byte_array), " byte_array = ", byte_array)  # 
print(byte_array[0])
print(chr(byte_array[0]))
print("Empty bytearray(): ",bytearray())

# c. Memoryview (memoryview)
mem_view: memoryview = memoryview(b"Operation Badar")
print(type(mem_view), " mem_view = ", mem_view)  # 
print(bytes(mem_view[0:5]))
print( mem_view[6:11] ) #cast it to byte otherwise it will show memory address


# Lession #3
# Operator and Operand
# unary oprators
x = 5
y = -x #unary operators
print ("y =",y)

# 1. Arithmetic Operators
#  Example
a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
print("a % b  = ", a % b)   # 1 Modulus (remainder)
print("a % b  = ", a ** b)  # 1000 Exponentiation (10 * 10 * 10)
#--------------------------------------------------------------------


# Lession #4
# Strings in Python
# Creating Strings
my_string: str = '''Hello,
World!'''
print(my_string)
#---------------------------------------------------------------------


# Lession #5
# Control Flow and Decision Making in Python
# 1. if Statement
num: int = 10

if num > 0:
    print("The number is positive.")

#2. else Statement

num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")
#-------------------------------------------------------------------------

# Lession #6
# lists and tuples    
#Example
fruits: list = "['apple', 'banana', 'cherry']"
mixed: list = "[1, "'apple'", 3.14, True]"
print(fruits)
print(mixed)

#Removing Elements
fruits.remove("banana")

#Tuples
Tuple1: tuple = (1,2,3,4,5)
Tuple2: tuple = (["apple", "banana", "cherry"]) 
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple
print(Tuple1)
print(Tuple2)
print(mixed_tuple)
#---------------------------------------------------------------------

# Lession #7
#The Set Data Type
my_set: set = {1,2,3,4,5}
print(my_set)

my_set.add(6) # Add an element to the set

my_set.remove(3) # Remove an element from the set
#--------------------------------------------------------------------


# Lession #8
#Modules & Functions

import math
print(math.sqrt(25))  # Output: 5.0


import math
print(math.pi)  # Output: 3.141592653589793

#import specific function or variable from a module 
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793
#---------------------------------------------------------------------


#Lession #9
#Exception Handling

try :
   result = 10 / 0
except:
    print ("An error occurred.")

    #The finally block
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("This will always execute.")

     