"""
CHAPTER 6: FUNCTIONS
=====================
"""

def section(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


# ----------------------------------------------------------------
section("1. WHY FUNCTIONS?  (6.1, 6.4)")
# ----------------------------------------------------------------
# A function is a NAMED group of statements. Functions help us:
#   - remove REDUNDANT (repeated) code: write it once, call it many times
#   - keep the main program short and readable
#   - build and test a program piece by piece (modular development)
# Guideline: keep each function under about 30 lines, with one clear job.

# WITHOUT a function, the same formula is repeated 3 times (and has a bug!)
f1, f2, f3 = 32.0, 212.0, 98.6
c1 = (f1 - 32.0) * (5.0 / 9.0)
c2 = (f2 - 32.0) * (5.0 / 9.0)
c3 = (f3 + 32.0) * (5.0 / 9.0)        # BUG: + instead of -  (easy to miss)
print("Repeated code:", round(c1, 1), round(c2, 1), round(c3, 1))

# WITH a function: the formula is written ONCE, so it's fixed in one place
def f_to_c(f):
    return (f - 32.0) * (5.0 / 9.0)

print("Function:     ", round(f_to_c(f1), 1), round(f_to_c(f2), 1), round(f_to_c(f3), 1))


# ----------------------------------------------------------------
section("2. DEFINING, CALLING & RETURNING  (6.1)")
# ----------------------------------------------------------------
# def name(parameters):     <- function DEFINITION (header + indented block)
#     statements
#     return value          <- sends a value back to the caller
# name(arguments)           <- function CALL (execution jumps in, then comes back)
# Naming convention: lowercase_with_underscores  (calc_area, get_name)

def calc_pizza_area():
    pi_val = 3.14159265
    pizza_radius = 12.0 / 2.0
    return pi_val * pizza_radius * pizza_radius

print(f"12.0 inch pizza is {calc_pizza_area():.3f} square inches")

def compute_square(num_to_square):
    return num_to_square * num_to_square

num_squared = compute_square(7)           # the return value gets stored
print(f"7 squared is {num_squared}")

# Facts about return:
#   - a function returns only ONE object (but that object can be a tuple or list)
#   - no return (or a bare "return") -> the function returns None
#   - return can appear anywhere, and a function can have several of them
def no_return():
    x = 5          # nothing is returned

print("no_return() gives:", no_return())

# Task:
#   a) Write compute_sum(num1, num2) that returns num1 + num2.
#   b) Write compute_cube(num) that returns num * num * num.
#   c) get_pattern() returns "*****". Call it twice to print 2 lines of stars.


# ----------------------------------------------------------------
section("3. PARAMETERS vs. ARGUMENTS  (6.1)")
# ----------------------------------------------------------------
# PARAMETER = the input name in the definition  -> def area(diameter)
# ARGUMENT  = the value you pass in the call    -> area(12.0)
# An argument can be any expression: 12.0, x, x * 1.5
# Arguments are matched to parameters BY POSITION (1st to 1st, 2nd to 2nd...)
# No parameters? The () are still required in both the def and the call.

import math

def calc_pizza_volume(pizza_diameter, pizza_height):
    radius = pizza_diameter / 2.0
    return math.pi * radius * radius * pizza_height

print(f"12.0 x 0.3 pizza: {calc_pizza_volume(12.0, 0.3):.3f} cubic inches")
print(f"16.0 x 0.8 pizza: {calc_pizza_volume(16.0, 0.8):.3f} cubic inches")

# Task (predict first!):
#   def get_birthday_age(user_age): return user_age + 1
#   print(get_birthday_age(42), get_birthday_age(20))   # -> ?
#   Is  def my_fct(user_num + 5):  a valid definition? (No: parameters must be plain names)


# ----------------------------------------------------------------
section("4. HIERARCHICAL (NESTED) FUNCTION CALLS  (6.1)")
# ----------------------------------------------------------------
# Functions can call other functions. You've already done this: int(input())

def calc_circle_area(diameter):
    radius = diameter / 2.0
    return math.pi * radius * radius

def calc_pizza_calories(diameter):
    calories_per_sq_inch = 16.7
    return calc_circle_area(diameter) * calories_per_sq_inch   # function inside a function

print(f"12 inch pizza has {calc_pizza_calories(12.0):.2f} calories")


# ----------------------------------------------------------------
section("5. PRINT (VOID) FUNCTIONS  (6.2)")
# ----------------------------------------------------------------
# A function that only prints and has no return is a VOID function (it returns None).
# Write complicated output ONCE, then call it many times. To change it, edit one place.

def print_summary(oid, items, price):
    print(f"Order {oid}:")
    print(f"   Items: {items}")
    print(f"   Total: ${price:.2f}")

print_summary(42, 4, 13.99)
print_summary(43, 1, 5.50)

def print_menu():
    print("Today's Menu:\n  1) Gumbo\n  2) Jambalaya\n  3) Quit")

print_menu()
result = print_summary(1, 1, 1.0)
print("A void function returns:", result)

# Task: define print_university_location(city, name) that prints
#   "<city> is the location of <name> University."   (no return)


# ----------------------------------------------------------------
section("6. DYNAMIC TYPING & POLYMORPHISM  (6.3)")
# ----------------------------------------------------------------
# POLYMORPHISM: what an operation does depends on the types involved.
# DYNAMIC TYPING: Python checks types WHILE the program runs (not ahead of time).
#   Compare with C, C++ and Java, which use STATIC typing: types are declared and checked when compiling.

def add(x, y):
    return x + y

print(add(5, 7))              # 12           (numbers are added)
print(add("Tora", "Bora"))    # ToraBora     (strings are joined)
print("x" * 5)                # xxxxx        (* repeats a string)
try:
    add(5, "100")             # the type error only shows up at run time
except TypeError as e:
    print("Runtime error:", e)


# ----------------------------------------------------------------
section("7. MATH FUNCTIONS & CALLS IN EXPRESSIONS  (6.5)")
# ----------------------------------------------------------------
# A function call EVALUATES TO its return value, so you can use it in expressions.

CM_PER_INCH = 2.54            # a global CONSTANT (UPPERCASE name)
INCHES_PER_FOOT = 12

def height_us_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters."""
    total_inches = feet * INCHES_PER_FOOT + inches
    return total_inches * CM_PER_INCH

print("6'4\" =", height_us_to_cm(6, 4), "cm")
print("Average:", (height_us_to_cm(5, 0) + height_us_to_cm(6, 1)) / 2.0)
print("7^2 + 9^2 =", compute_square(7) + compute_square(9))
print("Nested:", pow(2, pow(3, 2)))        # 2^9 = 512

# MODULAR: complex functions are built from simpler ones
def calc_base_area(radius):
    return math.pi * radius * radius

def calc_cylinder_volume(radius, height):
    return calc_base_area(radius) * height

def calc_cylinder_surface(radius, height):
    return 2 * math.pi * radius * height + 2 * calc_base_area(radius)

print(f"Cylinder r=10 h=5: volume {calc_cylinder_volume(10, 5):.3f}, "
      f"surface {calc_cylinder_surface(10, 5):.3f}")

# Task:
#   a) Write celsius_to_fahrenheit(c): F = C * 9/5 + 32.   Test: 50 -> 122


# ----------------------------------------------------------------
section("8. FUNCTION STUBS & INCREMENTAL DEVELOPMENT  (6.6)")
# ----------------------------------------------------------------
# Incremental development: write a little, test it, repeat.
# STUB = a placeholder function whose body isn't written yet. 3 styles:

def stub_pass(steps):
    pass                                   # does nothing, so it returns None

def stub_fixme(steps):
    print("FIXME: finish steps_to_calories")
    return -1                              # a clear "not real yet" value

def stub_stop(n):
    raise NotImplementedError              # stops the program if called

print("pass stub  ->", stub_pass(1000))
print("FIXME stub ->", stub_fixme(1000))
try:
    stub_stop(3)
except NotImplementedError:
    print("NotImplementedError: this function isn't written yet")


# ----------------------------------------------------------------
section("9. FUNCTIONS WITH BRANCHES & LOOPS  (6.7)")
# ----------------------------------------------------------------
def calc_ebay_fee(sell_price):
    """$0.50 listing fee + 13% up to $50, 5% from $50-$1000, 2% above $1000."""
    fee = 0.50
    if sell_price <= 50:
        fee += sell_price * 0.13
    elif sell_price <= 1000:
        fee += 50 * 0.13 + (sell_price - 50) * 0.05
    else:
        fee += 50 * 0.13 + 950 * 0.05 + (sell_price - 1000) * 0.02
    return fee

for price in [0, 40, 100, 500, 2000]:
    print(f"Sell ${price:>5}: fee ${calc_ebay_fee(price):.2f}")

def print_odds(numbers):
    print("Odd numbers:", end=" ")
    for n in numbers:
        if n % 2 != 0:
            print(n, end=" ")
    print()

print_odds([5, 99, -44, 0, 12])

# Task: print_negatives(numbers)


# ----------------------------------------------------------------
section("10. FUNCTIONS ARE OBJECTS  (6.8)")
# ----------------------------------------------------------------
# def creates a function OBJECT (with a type, an id and a value = compiled bytecode).
# Its name is just a label for that object, so you can assign it or pass it around.
# The only thing you can DO with a function is CALL it (func1 + func2 is an error).

def print_face():
    print(" o o\n  >\n ---")

func = print_face        # NO parentheses: gives the object, doesn't call it
func()                   # same as print_face()
print(type(print_face))

def human_head():  print("  |||||\n  o   o\n    >\n  ooooo")
def monkey_head(): print(' .-"-.\n( o o )\n  \\_/')

def print_figure(face):  # a function received as an argument
    face()
    print("   |\n --|--\n  / \\")

print_figure(monkey_head)


# ----------------------------------------------------------------
section("11. COMMON ERRORS  (6.9)")
# ----------------------------------------------------------------
# 1) COPY-PASTE error: code is pasted but not fully edited
def fahrenheit_to_celsius_buggy(fahrenheit):
    celsius = (fahrenheit - 32) * (5.0 / 9.0)
    return fahrenheit                  # BUG: should be "return celsius"

# 2) MISSING RETURN, which silently gives None (a logic error, not a syntax error)
def steps_to_feet_buggy(num_steps):
    feet = num_steps * 3               # forgot the return!

print("Copy-paste bug:", fahrenheit_to_celsius_buggy(212))   # 212, but should be 100
print("Missing return:", steps_to_feet_buggy(1000))          # None

# Task: fix both functions above.

# ----------------------------------------------------------------
section("12. SCOPE: LOCAL vs. GLOBAL  (6.10)")
# ----------------------------------------------------------------
# LOCAL variable:  created inside a function, only visible inside it
# GLOBAL variable: created outside functions, visible until the end of the file
# To ASSIGN a new value to a global inside a function, you need "global".
# Good practice: use globals only for CONSTANTS.

employee_name = "N/A"

def set_name_wrong():
    employee_name = "Romeo"            # creates a NEW local variable

def set_name_right():
    global employee_name
    employee_name = "Juliet"           # changes the global variable

set_name_wrong();  print("After wrong:", employee_name)   # N/A
set_name_right();  print("After right:", employee_name)   # Juliet

def show_local():
    secret = 42
try:
    show_local()
    print(secret)
except NameError as e:
    print("NameError:", e)             # local variables disappear after the function returns

# A function must be DEFINED before it's CALLED (otherwise: NameError).


# ----------------------------------------------------------------
section("13. NAMESPACES & SCOPE RESOLUTION  (6.11)")
# ----------------------------------------------------------------
# NAMESPACE = a dictionary that maps names to objects:  globals(), locals()
# Each function call gets its OWN local namespace, which is deleted when the function returns.
# SCOPE RESOLUTION order:  Local -> (Enclosing) -> Global -> Built-in -> NameError

daily_cals, soda_cals = 2300, 200

def drink_soda(cals_left):
    print("  locals inside drink_soda:", locals())
    return cals_left - soda_cals       # cals_left is local, soda_cals is found in globals

daily_cals = drink_soda(daily_cals)
print("daily_cals:", daily_cals)
print("'drink_soda' in globals()?", "drink_soda" in globals())

# The same name can live in different namespaces:
def avg(a, b):
    tmp = (a + b) / 2.0                # local tmp
    return tmp
tmp = 5 + 10                           # global tmp
print(f"Avg: {avg(5, 10)}, Sum (global tmp): {tmp}")


# ----------------------------------------------------------------
section("14. ARGUMENTS & MUTABILITY  (6.12)")
# ----------------------------------------------------------------
# Python passes arguments by OBJECT REFERENCE ("pass-by-assignment").
#   IMMUTABLE (int, str, tuple): changes inside the function DON'T leak out
#   MUTABLE (list, dict): changes made in place DO show up outside the function

def birthday(age):
    age = age + 1                      # makes a new local object
timmy_age = 7
birthday(timmy_age)
print("Timmy is", timmy_age)           # still 7

def modify(num_list):
    num_list[1] = 99
my_list = [10, 20, 30]
modify(my_list[:])                     # pass a COPY, so the original is safe
print("Passed a copy:", my_list)
modify(my_list)                        # pass the original
print("Passed original:", my_list)     # [10, 99, 30]


# ----------------------------------------------------------------
section("15. KEYWORD ARGUMENTS & DEFAULT VALUES  (6.13)")
# ----------------------------------------------------------------
# KEYWORD args match by NAME, so order doesn't matter (good once you have about 4+ args).
# Rule: positional args FIRST, keyword args LAST.
# DEFAULT values make a parameter optional.

def print_date(day=1, month=1, year=2000, style=0):
    if style == 0:
        print(f"{month}/{day}/{year}")          # American
    elif style == 1:
        print(f"{day}/{month}/{year}")          # European
    else:
        print("Invalid style")

print_date(30, 7, 2012)                 # style uses its default of 0
print_date(30, 7, 2012, 1)
print_date(year=2012, month=4)          # skip any args that have defaults
print_date()                            # all defaults

def split_check(amount, people, tax=0.09, tip=0.15):
    return amount * (1 + tax + tip) / people

print(f"${split_check(50, 4):.2f} each")
print(f"${split_check(25, 3, tip=0.25):.2f} each")
# split_check(tax=0.07, 60.52, 2)   -> SyntaxError (keyword before positional)


# ----------------------------------------------------------------
section("16. *args AND **kwargs  (6.14)")
# ----------------------------------------------------------------
# *args   -> collects any extra POSITIONAL args into a TUPLE
# **kwargs -> collects any extra KEYWORD args into a DICT
# Order in the def: normal params, then *args, then **kwargs

def print_sandwich(bread, meat, *args):
    extras = " with " + " ".join(args) if args else ""
    print(f"{meat} on {bread}{extras}")

print_sandwich("sourdough", "turkey", "mayo")
print_sandwich("wheat", "ham", "mustard", "tomato", "lettuce")

def gen_command(application, **kwargs):
    command = application
    for key, value in kwargs.items():
        command += f" --{key}={value}"
    return command

print(gen_command("notepad.exe"))
print(gen_command("powerpoint.exe", file="pres.ppt", start=True, slide=3))


# ----------------------------------------------------------------
section("17. RETURNING MULTIPLE VALUES  (6.15)")
# ----------------------------------------------------------------
# Return a TUPLE, then UNPACK it into several variables.

def get_grade_stats(scores):
    mean = sum(scores) / len(scores)
    std_dev = (sum((s - mean) ** 2 for s in scores) / len(scores)) ** 0.5
    return mean, std_dev                 # the same as: return (mean, std_dev)

average, std = get_grade_stats([75, 84, 66, 99, 51, 65])   # unpacking
print(f"Average: {average:.2f}, Std dev: {std:.2f}")


# ----------------------------------------------------------------
section("18. DOCSTRINGS & help()  (6.16)")
# ----------------------------------------------------------------
# A DOCSTRING is a """string""" on the FIRST line of the function body.
# One line for simple functions; multi-line docstrings describe the arguments.

def ticket_price(origin, destination, coach=True):
    """Calculates the price of a ticket between two airports.

    Arguments:
    origin      -- code of the origin airport
    destination -- code of the destination airport
    coach       -- True for a coach ticket (default True)
    """
    return 199.0

print(ticket_price.__doc__)
# In the interactive interpreter, try:  help(ticket_price)  help(str)  help(max)


# ----------------------------------------------------------------
section('19.UNIT TESTS  (6.17)')
# ----------------------------------------------------------------
# UNIT TESTS check each function on its own: the right name, parameters and return value.
# Function names are CASE-SENSITIVE: kilo_To_Pounds is not kilo_to_pounds.

def kilo_to_pounds(kilos):
    return kilos * 2.204

assert round(kilo_to_pounds(10), 3) == 22.04   # a tiny "unit test" (round: floats are not exact!)


# ================================================================
# PRACTICE
# ================================================================
# P1. driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)
#     Print the cost for 10, 50 and 400 miles to 2 decimals.
#     Input 20.0, 3.1599  ->  1.58 / 7.90 / 63.20
# P2. fibonacci(n) with a FOR loop (no recursion); negative n -> -1.
#     fibonacci(7) is 13


if __name__ == "__main__":
    for miles in (10, 50, 400):
        print(f"{driving_cost(20.0, 3.1599, miles):.2f}")
    print(f"fibonacci(7) is {fibonacci(7)}")
