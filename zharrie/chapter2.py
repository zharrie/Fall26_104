
"""
=====================================================================
 CHAPTER 2 - VARIABLES, DATA, AND EXPRESSIONS
 Run this file top-to-bottom, read the comments, then complete the
 exercises marked "EXERCISE" on your own (write your code right below
 the prompt, or in a separate file).
=====================================================================
"""
import math
import random

# =====================================================================
# 1. VARIABLES AND ASSIGNMENT
# =====================================================================
# A variable is a NAME bound to a value. "=" is ASSIGNMENT, not
# mathematical equality: x = x + 1 means "put x's old value + 1 back
# into x" - it overwrites the previous value.

x = 5
y = x               # y takes x's current value (5)
z = x + 2           # z is 5 + 2 = 7
print(x, y, z)

x = 3               # x is overwritten; y and z are unaffected
print(x, y, z)

count = 1
count = count + 1   # "incrementing" - a very common pattern
print("count is now", count)

# EXERCISE 1.1: Given x = 9, y = x + 1, then x = 5 -- what is y? Predict
#               first, then check by writing the code.


# =====================================================================
# 2. IDENTIFIERS (VARIABLE NAMES)
# =====================================================================
# Rules: letters, digits, underscores only; cannot start with a digit;
# case-sensitive; cannot be a reserved keyword (True, for, if, ...).
# Style: lowercase_with_underscores, descriptive names.

num_students = 30                 # good: clear, snake_case
diagonal_tv_size_inches = 55.0    # good: unit included

# invalid examples (commented out - they would cause a SyntaxError):
# 3rd_place = "bronze"     # cannot start with a digit
# num cars = 4             # cannot contain a space
# class = "A"              # "class" is a reserved keyword

# EXERCISE 2.1: Which of these are valid identifiers? _score, 2fast,
#               my-var, my_var, True, total_
#               (Write your answer as a comment.)


# =====================================================================
# 3. OBJECTS: VALUE, TYPE, IDENTITY
# =====================================================================
# Every piece of data in Python is an OBJECT with a value, a type, and
# a unique identity (memory address), automatically created by the
# interpreter (you never create objects directly).

n = 4 + 4
print("value:", n)
print("type:", type(n))
print("identity:", id(n))
print("type of a string:", type("ABC"))

# NAME BINDING: an assignment binds a NAME to an existing object; it
# doesn't modify the object. int/str objects are IMMUTABLE (their value
# can't change) - "changing" a variable actually rebinds its name to a
# brand-new object, and the interpreter automatically discards unused
# objects (garbage collection).
a = 25000
b = a          # b is bound to the SAME object as a
a = a * 1.2    # a is rebound to a NEW object; b is unaffected
print(a, b)

# EXERCISE 3.1: Create a variable age = 19. Print its type and its id.


# =====================================================================
# 4. NUMERIC TYPES: int vs. float
# =====================================================================
# int   -> whole numbers (things you COUNT).
# float -> real numbers with a decimal point (things you MEASURE).
# Scientific notation uses "e": 6.02e23 means 6.02 x 10**23.

miles = 450.0
hours_to_fly = miles / 500.0
print(f"{miles} miles takes {hours_to_fly} hours to fly")

speed_of_light = 3.0e8     # 3.0 x 10^8 m/s
print(speed_of_light)

# Formatting float output to a fixed number of decimals:
pi_value = math.pi
print(f"Pi to 4 decimals: {pi_value:.4f}")
print(f"Currency style:   ${19.9:.2f}")

# Floats have a max size too - exceeding it raises OverflowError:
try:
    print(2.0 ** 2048)
except OverflowError as e:
    print("Overflow caught:", e)

# EXERCISE 4.1: Store your height in centimeters as a float, then print
#               it rounded to one decimal place using an f-string.


# =====================================================================
# 5. ARITHMETIC EXPRESSIONS & PRECEDENCE
# =====================================================================
# Order of operations: ()  >  **  >  unary -  >  * / %  >  + -
# (equal-precedence operators evaluate left to right)
# When in doubt, add parentheses to make intent explicit.

result = 3 * (4 + 10 / 2)      # parentheses first, then /, then *
print(result)                   # 3 * (4 + 5.0) = 27.0

total_count = 1 + (2 * 5) * 4   # 1 + 10*4 = 41
print(total_count)

# EXERCISE 5.1: Without running the code, evaluate: x = 4; y = x + 1*6/2
#               Then check your answer by writing and running the code.


# =====================================================================
# 6. COMPOUND OPERATORS
# =====================================================================
# Shorthand for "update a variable using its own value":
#   +=   -=   *=   /=   %=   //=   **=

score = 10
score += 5          # same as score = score + 5
score *= 2
print("score:", score)

# EXERCISE 6.1: Start with balance = 100. Use compound operators to:
#               deposit 50, then withdraw 30, then print the balance.


# =====================================================================
# 7. DIVISION AND MODULO
# =====================================================================
# /   -> "true" division, always returns a float        (7 / 2 == 3.5)
# //  -> floor division, rounds down                     (7 // 2 == 3)
# %   -> modulo, the REMAINDER of a division              (7 % 2 == 1)

print(20 / 10, 20 // 10, 20 % 10)
print(7 / 2, 7 // 2, 7 % 2)

# Common use: extracting digits of a number
user_val = 927
ones_digit = user_val % 10           # 7
tens_digit = (user_val // 10) % 10   # 2
hundreds_digit = user_val // 100     # 9
print(ones_digit, tens_digit, hundreds_digit)

# EXERCISE 7.1: Given total_minutes = 135, compute and print the
#               equivalent hours and remaining minutes (2 hr 15 min).


# =====================================================================
# 8. MODULES AND SCRIPTS
# =====================================================================
# A MODULE is a .py file of reusable code; a SCRIPT is a .py file you
# run directly. `import module_name` makes that module's contents
# available via DOT NOTATION, e.g. math.sqrt(), random.randint().
# Importing a module runs all of its top-level code once.
#
# The special variable __name__ equals "__main__" only when a file is
# run directly (as a script) - not when it's imported by another file.
# This lets a file act as BOTH a reusable module AND a runnable script:
if __name__ == "__main__":
    print("This file was run directly as a script.")

# EXERCISE 8.1: In one comment, explain why splitting a large program
#               into several modules (e.g. buttons.py, score.py for a
#               game) makes it easier to manage.


# =====================================================================
# 9. THE math MODULE
# =====================================================================
print(math.sqrt(49))
print(math.pow(2, 10))
print(math.floor(2.7), math.ceil(2.3))
print(math.factorial(5))

# EXERCISE 9.1: Using math, compute the hypotenuse of a right triangle
#               with legs 3 and 4 (Hint: math.sqrt and **, or math.hypot).


# =====================================================================
# 10. RANDOM NUMBERS
# =====================================================================
# random.random()       -> float in [0.0, 1.0)
# random.randrange(n)   -> int in [0, n)
# random.randint(a, b)  -> int in [a, b]   (inclusive on BOTH ends!)

random.seed(42)                      # fixes the sequence (repeatable demo)
print(random.random())
print(random.randrange(10))          # 0 to 9
print(random.randint(1, 6))          # simulate a die roll, 1 to 6

# EXERCISE 10.1: Simulate flipping a coin 5 times, printing "Heads" or
#                "Tails" each time (Hint: random.randint(0, 1)).


# =====================================================================
# 11. REPRESENTING TEXT
# =====================================================================
# Strings are sequences of Unicode characters (each maps to a numeric
# code point, e.g. "A" -> 65). Escape sequences (\n, \t, \\, \") insert
# special characters. A raw string (r"...") ignores escape sequences -
# handy for file paths.

print("Tab\tNewline\nBackslash: \\")
path = r"C:\Users\new_folder"        # raw string: backslashes are literal
print(path)

print(ord("A"))       # character -> code point (65)
print(chr(65))         # code point -> character ('A')

# EXERCISE 11.1: Print your first and last name separated by a tab,
#               then print: Signature: "Approved"  using escaped quotes.


# =====================================================================
# 12. STYLE GUIDELINES (QUICK REFERENCE)
# =====================================================================
# - variables/functions: snake_case, descriptive          (num_items)
# - constants:            UPPER_CASE                       (MAX_SPEED)
# - classes:              CamelCase                         (RaceTime)
# - one space around operators, no trailing spaces
# - 4-space indentation, no tabs


# =====================================================================
# PRACTICE SET - try these on your own
# =====================================================================
# P1. Ask for a radius (float) and print a circle's area and
#     circumference, rounded to 2 decimals. (area = PI * r**2)
# P2. Ask for a 4-digit number and print each of its digits separately
#     using // and % only (no strings, no loops).
# P3. "2,000,000,000" is NOT valid Python. Rewrite it as a valid
#     integer literal.
# P4. Generate and print 3 random integers between 1 and 100 using
#     random.randint().
# P5. Given weight_kg = 72.5, use an f-string to print the weight in
#     pounds (1 kg = 2.20462 lbs), rounded to 1 decimal place.
