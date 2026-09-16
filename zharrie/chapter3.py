"""
===========================================================
Chapter 3 - TYPES
Strings | f-strings | Lists | Tuples | Sets | Dictionaries
Types summary | Type conversions | Binary numbers
-----------------------------------------------------------
Run it:      python3 chapter3.py
===========================================================
"""

from collections import namedtuple


def head(t):
    print("\n" + "=" * 55 + "\n" + t + "\n" + "=" * 55)


def task(t):
    print("\n  >> IN-CLASS EXERCISE: " + t)


# ============================================================
# 3.1  STRING BASICS
# ============================================================
# A string is a SEQUENCE OF CHARACTERS, written in quotes.
# - Ordered: each character has an INDEX, starting at 0.
# - len(s) gives the number of characters.
# - Negative index counts from the right: s[-1] is the last.
# - IMMUTABLE: you cannot change a character. s[0] = "A" -> TypeError.
#   To "change" a string, assign a whole new one.
# - "+" CONCATENATES two strings and builds a NEW string.
#   Strings only! 332 + " Main St" is an error; use str(332).
def s3_1():
    head("3.1  STRING BASICS")

    name = "Trish"
    print("  name          =", name)
    print("  len(name)     =", len(name))       # 5
    print("  name[0]       =", name[0])         # T  (first)
    print("  name[-1]      =", name[-1])        # h  (last)

    # Immutable: this fails on purpose
    try:
        name[0] = "D"
    except TypeError as e:
        print("  name[0]='D'   -> TypeError:", e)

    name = "Dana"                               # correct way to change it
    print("  reassigned    =", name)

    # Concatenation
    print("  'New'+'York'  =", "New" + "York")
    print("  str(332)+...  =", str(332) + " Main Street")

    task("Given first='Amaya', last='Sanders', build and print"
         "\n     'Amaya Sanders' using + . Then print its length.")


# ============================================================
# 3.2  STRING FORMATTING (f-pSTRINGS)
# ============================================================
# Put f before the quotes, then put expressions inside { }.
# Each { } is a REPLACEMENT FIELD - it is replaced by the value.
#   {x=}   prints the expression AND its value  (debug helper)
#   {{ }}  prints literal curly braces
# A COLON adds a FORMAT SPECIFICATION:  {value:how}
#   :d    integer            {4:d}      -> 4
#   :,d   commas             {7600:,d}  -> 7,600
#   :03d  leading zeros      {4:03d}    -> 004
#   :b    binary             {4:b}      -> 100
#   :x    hexadecimal        {31:x}     -> 1f
#   :e    exponent           {44:e}     -> 4.400000e+01
#   :f    6 decimals         {4:f}      -> 4.000000
#   :.2f  2 decimals         {4:.2f}    -> 4.00
#   :,.2f commas + decimals  {7600.1:,.2f} -> 7,600.10
def s3_2():
    head("3.2  STRING FORMATTING (f-STRINGS)")

    number, amount = 6, 32
    print(f"  {number} burritos cost ${amount}")

    kids, adults = 4, 2
    print(f"  {kids+adults} total people")      # expressions are allowed
    print(f"  debug -> {kids+adults=}")         # kids+adults=6
    print(f"  braces -> {{2}} + {{3}}")         # {2} + {3}

    print(f"  {7600:,d}   {4:03d}   {4:b}   {31:x}   {4:.2f}   {7600.1:,.2f}")

    task("num_students = 32. Print 'The math class has 32 students.'"
         "\n     Then print the price 1234.5 as 1,234.50")


# ============================================================
# 3.3  LIST BASICS
# ============================================================
# A LIST is a CONTAINER written with brackets: [10, "abc"]
# - Ordered (index from 0) and MUTABLE - you CAN change elements.
# - Can mix types. [] is an empty list.
# Methods (use a dot):
#   my_list.append(v)  add v to the end
#   my_list.pop(i)     remove the element AT INDEX i
#   my_list.remove(v)  remove the FIRST element with VALUE v
#   my_list.index(v)   position of first v      my_list.count(v)  how many v
# Functions (no dot):
#   len(l)  min(l)  max(l)  sum(l)  and  list1 + list2  (concatenate)
def s3_3():
    head("3.3  LIST BASICS")

    prices = [1.50, 3.75, 6.00]
    print("  prices        =", prices)
    print("  prices[0]     =", prices[0])
    prices[0] = 2.50                              # lists ARE mutable
    print("  after update  =", prices)

    my_list = [10, "bw"]
    my_list.append("abc"); print("  after append  =", my_list)
    my_list.pop(1);        print("  after pop(1)  =", my_list)
    my_list.remove("abc"); print("  after remove  =", my_list)

    houses = [380000, 900000, 875000] + [225000]  # concatenation
    print("  len / min / max / sum =",
          len(houses), min(houses), max(houses), sum(houses))
    print("  average       =", sum(houses) / len(houses))

    task("scores = [88, 92, 79]. Add 95 to the end, remove the 79,"
         "\n     then print the average of what is left.")


# ============================================================
# 3.4  TUPLE BASICS
# ============================================================
# A TUPLE is like a list but IMMUTABLE: (5, 15, 20)
# Use it when POSITION has meaning and data must not change,
# e.g. (latitude, longitude). len() and indexing still work.
#
# A NAMED TUPLE gives the positions NAMES, so code reads better:
#   Car = namedtuple("Car", ["make", "model", "price"])   <- makes the TYPE
#   c   = Car("Chevrolet", "Blazer", 32000)               <- makes an OBJECT
#   c.price   is much clearer than   c[2]
def s3_4():
    head("3.4  TUPLE BASICS")

    white_house = (38.8977, 77.0366)
    print("  coordinates   =", white_house)
    print("  latitude      =", white_house[0], " longitude =", white_house[1])
    print("  len           =", len(white_house))

    try:
        white_house[1] = 50
    except TypeError as e:
        print("  change it     -> TypeError:", e)

    Car = namedtuple("Car", ["make", "model", "price"])
    blazer = Car("Chevrolet", "Blazer", 32000)
    print("  named tuple   =", blazer)
    print("  blazer.price  =", blazer.price)

    task("Create Dog = namedtuple with fields name, breed, color."
         "\n     Make one dog and print its breed.")


# ============================================================
# 3.5  SET BASICS
# ============================================================
# A SET is UNORDERED and holds UNIQUE elements: {1, 2, 3}
# - No index! my_set[0] is an error (there is no "first" element).
# - set([1,2,2,3]) -> {1, 2, 3}   duplicates disappear.
# - An EMPTY set must be set() ; {} makes an empty DICTIONARY.
# Methods: add(v)  update(other)  remove(v)  pop()  clear()  len(s)
# Set math: union  intersection  difference  symmetric_difference
def s3_5():
    head("3.5  SET BASICS")

    print("  set([100,200,100,200,300]) =", sorted(set([100, 200, 100, 200, 300])))

    names = {"Pedro", "Khan", "Dean"}
    names.add("Hyungu");                print("  after add     =", sorted(names))
    names.update({"Kara", "Tia"});      print("  after update  =", sorted(names))
    names.remove("Dean");               print("  after remove  =", sorted(names))
    print("  len(names)    =", len(names))

    monsters = {"Gorgon", "Medusa"}
    horde = {"Gorgon", "Bert", "Tom"}
    print("  union         =", sorted(monsters.union(horde)))
    print("  intersection  =", sorted(monsters.intersection(horde)))
    print("  difference    =", sorted(monsters.difference(horde)))
    print("  symmetric_dif =", sorted(monsters.symmetric_difference(horde)))

    # sorted() is only used so the printed order is always the same.

    task("colors = ['red', 'blue', 'red', 'green']."
         "\n     Build a set of the unique colors and print how many there are.")


# ============================================================
# 3.6  DICTIONARY BASICS
# ============================================================
# A DICTIONARY maps a KEY to a VALUE:  {"apples": 1.99}
# - Key must be immutable (string, number, tuple); value can be anything.
# - Look up with the KEY in brackets, NOT by position: prices["apples"]
# - A missing key gives a KeyError.
#   d[k] = v   adds the pair if k is new, OR updates it if k already exists
#   del d[k]   removes the pair
# Use a dict when data is ASSOCIATED (name -> grade). Use a list if it is
# just an ordered collection.
def s3_6():
    head("3.6  DICTIONARY BASICS")

    prices = {"apples": 1.99, "oranges": 1.49}
    print("  prices            =", prices)
    print("  prices['apples']  =", prices["apples"])

    try:
        prices["lemons"]
    except KeyError as e:
        print("  prices['lemons']  -> KeyError:", e)

    prices["bananas"] = 1.49          # ADD (new key)
    print("  after add         =", prices)
    prices["bananas"] = 1.69          # MODIFY (key already exists)
    print("  after modify      =", prices)
    del prices["bananas"]             # REMOVE
    print("  after delete      =", prices)

    task("Create a dict grades with 'Jessica': 'B'. Add 'John': 'A+',"
         "\n     change Jessica to 'A', delete John, then print the dict.")


# ============================================================
# 3.7  COMMON DATA TYPES SUMMARY
# ============================================================
# NUMERIC:  int (whole numbers)      float (decimals)
# CONTAINERS:
#   string  sequence, immutable, text only
#   list    sequence, MUTABLE
#   tuple   sequence, immutable
#   set     unordered, unique elements
#   dict    key -> value pairs
#
# How to choose:
#   ordered data ................. list
#   ordered + must not change .... tuple
#   unique values, order not needed set
#   each item has an identifier .. dict
def s3_7():
    head("3.7  COMMON DATA TYPES SUMMARY")

    print("  type      ordered  mutable  indexed  example")
    print("  " + "-" * 48)
    for r in [("string", "yes", "no ", "yes", '"abc"'),
              ("list  ", "yes", "yes", "yes", "[1, 2, 3]"),
              ("tuple ", "yes", "no ", "yes", "(1, 2, 3)"),
              ("set   ", "no ", "yes", "NO ", "{1, 2, 3}"),
              ("dict  ", "yes", "yes", "by key", '{"a": 1}')]:
        print(f"  {r[0]}    {r[1]}      {r[2]}      {r[3]}     {r[4]}")

    task("Which container fits best?"
         "\n     (a) test scores that may be adjusted later"
         "\n     (b) one student's name and final grade"
         "\n     (c) names and grades for the whole class")


# ============================================================
# 3.9  TYPE CONVERSIONS
# ============================================================
# IMPLICIT: Python converts automatically in math.
#   1 + 2   -> int      1 + 2.0 -> float   (float if EITHER side is float)
# EXPLICIT: you call a conversion function.
#   int(x)    -> integer; a float is TRUNCATED, not rounded: int(1.55) = 1
#   float(x)  -> float:   float("7.99") = 7.99
#   str(x)    -> string:  str(99) = "99"
# IMPORTANT: input() ALWAYS returns a string, so convert before doing math.
def s3_9():
    head("3.9  TYPE CONVERSIONS")

    print("  1 + 2     =", 1 + 2, type(1 + 2).__name__)
    print("  1 + 2.0   =", 1 + 2.0, type(1 + 2.0).__name__)
    print("  int(1.55) =", int(1.55), "  (truncated, not rounded)")
    print("  float('7.99') =", float("7.99"))
    print("  str(99) + ' feet' =", str(99) + " feet")

    raw = "18"                       # pretend this came from input()
    print("  '18' + '18'       =", raw + raw, " <- string glued together")
    print("  int('18')+int('18')=", int(raw) + int(raw), " <- real math")

    task("num_feet = 22 (an int). Convert it to a string str_feet and print"
         "\n     'Number of feet: ' + str_feet")


# ============================================================
# 3.10  BINARY NUMBERS
# ============================================================
# Decimal (base 10): each place is a power of 10.  273 = 2*100 + 7*10 + 3*1
# Binary  (base 2) : each place is a power of 2.
#     place values: 128  64  32  16  8  4  2  1
#     1011 = 8 + 0 + 2 + 1 = 11
# 8 bits hold 0 to 255 (that is 2**8 = 256 combinations).
# In Python:  bin(9) -> '0b1001'   f"{9:b}" -> '1001'   int("1001", 2) -> 9
def s3_10():
    head("3.10  BINARY NUMBERS")

    print("  place values:  128  64  32  16   8   4   2   1")

    # Convert decimal numbers to binary one at a time.
    print(f"    9 decimal = {9:08b} binary")
    print(f"   50 decimal = {50:08b} binary")
    print(f"  212 decimal = {212:08b} binary")
    print(f"  255 decimal = {255:08b} binary")

    # Convert binary strings back to decimal one at a time.
    print(f"  00001111 binary = {int('00001111', 2)} decimal")
    print(f"  10001000 binary = {int('10001000', 2)} decimal")

    print("  bin(9) =", bin(9), "  f'{9:b}' =", f"{9:b}")

    task("Convert 17 and 51 to 8-bit binary by hand,"
         "\n     then check yourself with an f-string.")


if __name__ == "__main__":
    print(__doc__)
    sections = (s3_1, s3_2, s3_3, s3_4, s3_5, s3_6, s3_7, s3_9, s3_10, practice)
    for section in sections:
        choice = input(
            f"\nPress Enter to run {section.__name__}, or type q to quit: "
        )
        if choice.strip().lower() == "q":
            break
        section()
