"""
================================================================================
 LECTURE: BRANCHING (Chapter 4)
================================================================================

This is a runnable lecture. Each section is a function with concise notes and
live examples. Run the file to see every section execute, then complete the
HANDS-ON EXERCISES at the bottom.

Sections
  4.1  If-else branches (general)
  4.2  Detecting equal values with branches
  4.3  Detecting ranges with branches (general)
  4.4  Relational operators & operator chaining
  4.5  Detecting ranges using logical operators
  4.6  Detecting ranges with gaps
  4.7  Multiple / nested if statements
  4.8  Comparing data types & common errors
  4.9  Membership and identity operators
  4.10 Order of evaluation (precedence)
  4.11 Code blocks and indentation
  4.12 Conditional (ternary) expressions
================================================================================
"""


# ------------------------------------------------------------------------------
# 4.1  IF-ELSE BRANCHES (GENERAL)
# ------------------------------------------------------------------------------
# A BRANCH is a sequence of statements executed only under a certain condition.
#   - if branch      : runs only if an expression is True.
#   - if-else branch : first block runs if True, else the second block runs.
#   - if-elif-else   : three or more branches; expressions checked in ORDER;
#                      the FIRST True branch runs, then the rest are skipped.
#                      The final `else` is optional.
def section_4_1():
    # if branch: hotel discount only for guests over 65
    hotel_rate = 155
    user_age = 68
    if user_age > 65:
        hotel_rate = hotel_rate - 20   # taken only when True
    print("4.1 hotel rate:", hotel_rate)             # 135

    # if-else: car insurance price by age
    age = 18
    if age < 25:
        insure_price = 4800
    else:
        insure_price = 2200
    print("4.1 insurance:", insure_price)            # 4800

    # if-elif-else: exactly one branch runs
    num_years = 25
    if num_years == 1:
        msg = "Newlyweds"
    elif num_years == 25:
        msg = "Silver"
    elif num_years == 50:
        msg = "Golden"
    else:
        msg = "Congrats"
    print("4.1 anniversary:", msg)                   # Silver


# ------------------------------------------------------------------------------
# 4.2  DETECTING EQUAL VALUES WITH BRANCHES
# ------------------------------------------------------------------------------
# Equality operator  ==  : True when both sides are equal   (NOT the same as =)
# Inequality operator !=  : True when the sides differ
# Both yield a BOOLEAN (True/False).
# Multi-branch uses the `elif` keyword ("else if").
def section_4_2():
    x = 3
    print("4.2 x == 3 :", x == 3)    # True
    print("4.2 x != 4 :", x != 4)    # True

    # Even/odd via remainder
    user_num = 45
    div_remainder = user_num % 2
    if div_remainder == 0:
        print(f"4.2 {user_num} is even.")
    else:
        print(f"4.2 {user_num} is odd.")            # odd

    # Multi-branch detecting specific values
    num_sales = 2
    if num_sales == 0:
        employee_bonus = 0
    elif num_sales == 1:
        employee_bonus = 2
    elif num_sales == 2:
        employee_bonus = 5
    elif num_sales == 4:
        employee_bonus = 5
    elif num_sales == 7:
        employee_bonus = 5
    else:
        employee_bonus = 10
    print("4.2 bonus:", employee_bonus)             # 5


# ------------------------------------------------------------------------------
# 4.3  DETECTING RANGES WITH BRANCHES (GENERAL)
# ------------------------------------------------------------------------------
# The SEQUENTIAL nature of if-elif-else detects ranges. Each expression only
# needs the UPPER bound; the lower bound is implied because all previous
# expressions were False (works for increasing ranges WITHOUT gaps).
def section_4_3():
    def soccer_team(age):
        if age < 6:
            return "No teams"       # 5 or under
        elif age < 8:
            return "U8 team"        # 6-7-5-4
        elif age < 10:
            return "U10 team"       # 8-9
        elif age < 12:
            return "U12 team"       # 10-11
        else:
            return "No teams"       # 12+
    for a in (5, 7, 9, 11, 14):
        print(f"4.3 age {a}: {soccer_team(a)}")


# ------------------------------------------------------------------------------
# 4.4  RELATIONAL OPERATORS & OPERATOR CHAINING
# ------------------------------------------------------------------------------
# Relational operators:  <   >   <=   >=   ==   !=
# Two-character operators must be exact: <=, >=  (=<, =>, <> are INVALID).
# Operator chaining:  a < b < c  means (a < b) and (b < c), evaluated
# left-to-right; `a` is NOT compared to `c`.
def section_4_4():
    x = 3
    print("4.4 x <= 4:", x <= 4)    # True
    print("4.4 x >= 4:", x >= 4)    # False

    # Range detection using sequential multi-branch
    def insurance(user_age):
        if user_age < 16:      # 15 and under
            return 0
        elif user_age < 25:    # 16-24
            return 4800
        elif user_age < 40:    # 25-39
            return 2350
        else:                  # 40+
            return 2100
    print("4.4 insurance(27):", insurance(27))       # 2350

    # Operator chaining: high-school grades 9..12 inclusive
    for grade in (10, 8, 12):
        in_hs = 9 <= grade <= 12
        print(f"4.4 grade {grade} in high school: {in_hs}")


# ------------------------------------------------------------------------------
# 4.5  DETECTING RANGES USING LOGICAL OPERATORS
# ------------------------------------------------------------------------------
# Logical operators (Python keywords, lowercase): and, or, not
#   and : True only if BOTH operands are True
#   or  : True if AT LEAST ONE operand is True
#   not : opposite of the operand
# A Boolean is a value that is either True or False (capitalized keywords).
# Explicitly detect a range by stating BOTH bounds:  (0 < x) and (x < 100)
def section_4_5():
    age, days = 19, 7
    print("4.5 (age>16) and (age<25):", (age > 16) and (age < 25))  # True
    print("4.5 (age>16) and (days>10):", (age > 16) and (days > 10))  # False
    print("4.5 (age>16) or (days>10):", (age > 16) or (days > 10))    # True
    print("4.5 not (days > 10):", not (days > 10))                    # True

    # TV channels example
    def channel_type(ch):
        if (ch >= 2) and (ch <= 499):
            return "s"        # standard
        elif (ch >= 1002) and (ch <= 1499):
            return "h"        # high-definition
        else:
            return "e"        # error
    for c in (3, 1300, 700):
        print(f"4.5 channel {c}: {channel_type(c)}")


# ------------------------------------------------------------------------------
# 4.6  DETECTING RANGES WITH GAPS
# ------------------------------------------------------------------------------
# A GAP is a middle range handled by a different branch. Explicitly detect
# multiple valid ranges with `and` for bounds and combine them with `or`.
def section_4_6():
    # Movie tickets: child (<=12), senior (>=65), everyone else (the gap)
    def ticket_price(user_age):
        if user_age <= 12:
            return 11
        elif user_age >= 65:
            return 12
        else:                 # gap: ages 13-64
            return 14
    for a in (7, 40, 67):
        print(f"4.6 age {a}: ${ticket_price(a)}")

    # Two valid ranges combined with OR (office numbers 100-150 or 200-250)
    def valid_office(n):
        return (100 <= n <= 150) or (200 <= n <= 250)
    print("4.6 valid_office(130):", valid_office(130))   # True
    print("4.6 valid_office(175):", valid_office(175))   # False


# ------------------------------------------------------------------------------
# 4.7  MULTIPLE / NESTED IF STATEMENTS
# ------------------------------------------------------------------------------
# Multiple DISTINCT if statements are independent: MORE THAN ONE can run.
# This differs from if-elif-else where only ONE branch runs.
# NESTED if-else: a branch may contain another if-else.
def section_4_7():
    # Independent ifs: several can print
    user_age = 26
    if user_age < 16:
        print("4.7 Enjoy your early years.")
    if user_age > 15:
        print("4.7 Old enough to drive.")
    if user_age > 17:
        print("4.7 Old enough to vote.")
    if user_age > 24:
        print("4.7 Car rentals available.")

    # Nested if-else
    sales_type, sales_bonus = 2, 4
    if sales_type == 2:
        if sales_bonus < 5:
            sales_bonus = 10
        else:
            sales_bonus = sales_bonus + 2
    else:
        sales_bonus = sales_bonus + 1
    print("4.7 sales_bonus:", sales_bonus)           # 10


# ------------------------------------------------------------------------------
# 4.8  COMPARING DATA TYPES & COMMON ERRORS
# ------------------------------------------------------------------------------
# - Relational/equality operators work for int, float, and str.
# - Avoid == with floats (imprecise representation).
# - Strings compare char-by-char via Unicode; case matters ("T" != "t").
# - Comparing incompatible types (1 < "abc") raises a TypeError.
# - Lists/tuples compare element-by-element; dicts only with == / !=.
# COMMON ERRORS:
#   * using = instead of == in a condition  -> SyntaxError
#   * invalid operators like =>, !<, <>      -> SyntaxError
def section_4_8():
    print("4.8 'Tuesday' == 'Tuesday':", "Tuesday" == "Tuesday")  # True
    print("4.8 'Tuesday' == 'tuesday':", "Tuesday" == "tuesday")  # False
    print("4.8 [1,5,2] < [1,4,3]:", [1, 5, 2] < [1, 4, 3])        # False

    # TypeError demonstration (safely caught)
    try:
        result = 1 < "abc"
    except TypeError as e:
        print("4.8 TypeError caught:", e)


# ------------------------------------------------------------------------------
# 4.9  MEMBERSHIP AND IDENTITY OPERATORS
# ------------------------------------------------------------------------------
# Membership:  in / not in  -> True if a value is found in a container.
#   * lists/tuples: checks elements; strings: checks substrings;
#     dicts: checks KEYS only (not values).
# Identity:    is / is not  -> True if two names reference the SAME object
#   (compares object identity/memory address, NOT value).
#   Good practice: use == for value comparison; reserve `is` for None checks.
def section_4_9():
    roster = ["Alves", "Messi", "Fabregas"]
    print("4.9 'Messi' in roster:", "Messi" in roster)      # True
    print("4.9 'abc' in '123abcd':", "abc" in "123abcd")    # True

    my_dict = {"A": 1, "B": 2, "C": 3}
    print("4.9 'B' in my_dict:", "B" in my_dict)            # True (key)
    print("4.9  3  in my_dict:", 3 in my_dict)              # False (value)

    a = [1, 2]
    b = a
    c = [1, 2]
    print("4.9 b is a:", b is a)         # True  (same object)
    print("4.9 c is a:", c is a)         # False (equal value, diff object)
    print("4.9 c == a:", c == a)         # True


# ------------------------------------------------------------------------------
# 4.10 ORDER OF EVALUATION (PRECEDENCE)
# ------------------------------------------------------------------------------
# Highest -> lowest precedence:
#   ()              parentheses
#   * / % + -       arithmetic
#   < <= > >= == != in   relational/equality/membership
#   not             logical NOT
#   and             logical AND
#   or              logical OR
# Good practice: add parentheses to make intent explicit.
def section_4_10():
    x, y, z = 7, 6, 3
    # y*z < x+1 or z == 3  ->  (18 < 8) or (3 == 3)  -> False or True -> True
    print("4.10 y*z < x+1 or z == 3:", y * z < x + 1 or z == 3)   # True

    # not a == b  is  not (a == b)  because == binds tighter than not
    a, b = 4, 5
    print("4.10 not a == b:", not a == b)            # True

    # and before or
    num1, num2, num3 = 9, 0, 0
    print("4.10 mixed and/or:",
          num1 == 9 or num2 == 0 and num3 == 0)      # True


# ------------------------------------------------------------------------------
# 4.11 CODE BLOCKS AND INDENTATION
# ------------------------------------------------------------------------------
# A CODE BLOCK is a group of statements at the same indentation level.
# - A new block follows a line ending in a colon (if/elif/else/def...).
# - Indent consistently; the standard is FOUR spaces.
# - NEVER mix tabs and spaces -> IndentationError in Python 3.
def section_4_11():
    model = "Ford"
    year = 1918
    antique = year < 1970
    domestic = model in ["Ford", "Chevrolet", "Dodge"]
    if antique:                       # block level 1
        if domestic:                  # block level 2 (nested)
            print("4.11 My model-T still runs like a charm...")


# ------------------------------------------------------------------------------
# 4.12 CONDITIONAL (TERNARY) EXPRESSIONS
# ------------------------------------------------------------------------------
# Form:   expr_when_true if condition else expr_when_false
# The condition is evaluated FIRST. A three-operand "ternary" operation.
# Good practice: restrict to simple assignments.
def section_4_12():
    x = 2
    print("4.12 5 if x==2 else 9*x:", 5 if x == 2 else 9 * x)     # 5

    # y = 0 if x < 100 else x
    x = 250
    y = 0 if x < 100 else x
    print("4.12 y:", y)                              # 250

    # absolute value with a conditional expression
    n = -8
    print("4.12 abs:", -n if n < 0 else n)           # 8


def run_all_sections():
    for fn in (
        section_4_1, section_4_2, section_4_3, section_4_4,
        section_4_5, section_4_6, section_4_7, section_4_8,
        section_4_9, section_4_10, section_4_11, section_4_12,
    ):
        print(f"\n--- {fn.__name__} ---")
        fn()


# ==============================================================================
#                            HANDS-ON EXERCISES
# ==============================================================================
# Try each on your own first, then run to check. Reference solutions follow.
#
# EX 1 (4.1/4.2 if-elif-else): Restaurant seating.
#     Given party_size, return "counter" for 1, "small table" for 2,
#     otherwise "large table".
#
# EX 2 (4.2 even/odd & equality): Return "even" or "odd" for an integer n.
#
# EX 3 (4.3/4.4 ranges): Given user_age, return the soccer team
#     ("No teams", "U8 team", "U10 team", "U12 team") using an increasing
#     range multi-branch (no logical operators, no gaps).
#
# EX 4 (4.5 logical operators): Return True if x is in the range 1..99
#     inclusive, using logical AND.
#
# EX 5 (4.6 ranges with gaps): Movie ticket price -> 11 if age <= 12,
#     12 if age >= 65, else 14.
#
# EX 6 (4.7 nested/multiple): Given vehicle_year, print all that apply:
#     >=1955 "carries several people"; <1960 "few safety features";
#     >=1994 "has traction control".
#
# EX 7 (4.9 membership): Return "Special number" if n is in [-99, 0, 44],
#     else "Not special number".
#
# EX 8 (4.12 conditional expression): Return "negative" if v < 0 else
#     "non-negative", using a single ternary expression.
#
# EX 9 (CHALLENGE - Leap year): A year is a leap year if divisible by 4,
#     except century years must be divisible by 400.
#
# EX 10 (CHALLENGE - Smallest of three): Return the smallest of a, b, c.
# ------------------------------------------------------------------------------


if __name__ == "__main__":
    run_all_sections()
