"""
===========================================================
 PYTHON LOOPS
 5.1 Loops (general)        5.7  While vs. for
 5.2 While loops            5.8  Nested loops
 5.3 More while examples    5.9  Developing incrementally
 5.4 Counting               5.10 Break and continue
 5.5 For loops              5.11 Loop else
 5.6 range()                5.12 enumerate()
===========================================================
"""

import random


def head(t):
    print("\n" + "=" * 57 + "\n" + t + "\n" + "=" * 57)


def task(t):
    print("\n  >> IN-CLASS EXERCISE: " + t)


# ============================================================
# 5.1  LOOPS (GENERAL)
# ============================================================
# Think of parents driving a baby around the block: check if the baby
# is asleep, if not, loop around again.
#
# A LOOP repeatedly executes its statements (the LOOP BODY) while the
# loop's expression is True. When the expression is False, execution
# proceeds PAST the loop. Each time through the body is an ITERATION.
#
# A loop is like a branch, except it jumps back to the expression when
# the body finishes.
#
# Three classic loop tasks, all done by examining values one at a time
# and updating a variable along the way:
#   SUM      sum = sum + val
#   COUNT    if val < 0:  count = count + 1
#   MAXIMUM  if val > max: max = val   (initialize max = -1 first, so
#                                       the comparison works on value 1)
def s5_1():
    head("5.1  LOOPS (GENERAL)")

    # Sum until the sentinel -1 is seen  (input 2 4 1 -1 -> sum 7)
    values = [2, 4, 1, -1]
    total = 0
    i = 0
    val = values[i]                  # get first input BEFORE the loop
    while val > -1:
        total = total + val
        i += 1
        val = values[i]              # get next input at END of body
    print("  sum of 2 4 1 (-1 ends) =", total)

    # Average: same loop, but also count the values  (2 4 9 -1 -> 5)
    values = [2, 4, 9, -1]
    total, num, i = 0, 0, 0
    val = values[i]
    while val > -1:
        total += val
        num += 1
        i += 1
        val = values[i]
    print("  average of 2 4 9       =", total / num)

    # Count negatives  (-1 -5 9 3 0 -> count 2)
    values = [-1, -5, 9, 3, 0]
    count, i = 0, 0
    while values[i] != 0:
        if values[i] < 0:
            count = count + 1
        i += 1
    print("  negatives in -1 -5 9 3 =", count)

    # Find the max  (22 5 99 3 0 -> 99)
    values = [22, 5, 99, 3, 0]
    biggest, i = -1, 0               # -1 so the first value always wins
    while values[i] != 0:
        if values[i] > biggest:
            biggest = values[i]
        i += 1
    print("  max of 22 5 99 3       =", biggest)

    task("If the FIRST input is the sentinel (list = [0]), how many times"
         "\n     does the counting loop body run? Explain why.")


# ============================================================
# 5.2  WHILE LOOPS
# ============================================================
#     while expression:      # loop expression
#         loop body          # runs while the expression is True
#     # statements after the loop
#
# Indentation marks the block of code belonging to the while loop.
#
# SENTINEL VALUE: a value that causes the loop to end, e.g. the user
# types "stop" or 999. The USER controls when the loop ends - that is
# what distinguishes a sentinel loop from other loops.
#
# INFINITE LOOP: the condition is always True, so the loop never stops.
# A common error is assuming equality will be reached. Good practice:
# use < or > along WITH equality (<=, >=) to avoid this.
# An infinite loop is valid in some programs, e.g. a game checking for
# input in real time.
def s5_2():
    head("5.2  WHILE LOOPS")

    value = 1
    while value < 6:
        print("  value =", value)
        value = value * 2          # 1, 2, 4 -> then 8 stops the loop
    print("  Done. value =", value)

    # Sentinel: keep asking until the password matches
    password = "star"
    guesses = ["kite", "moon", "star"]     # pretend these are input()
    k = 0
    user_input = guesses[k]
    while user_input != password:          # "star" is the SENTINEL
        print("  Wrong password. Try again. (got", user_input + ")")
        k += 1
        user_input = guesses[k]
    print("  Access granted.")

    # Body runs ZERO times if the condition starts False
    index = 0
    while index > 0:
        print("  never printed")
    print("  index > 0 was False -> body ran 0 times, then 'Bye'")

    task("total = 5. Write a while loop that prints total while it is <= 25,"
         "\n     doubling it each time. What are the three numbers printed?")


# ============================================================
# 5.3  MORE WHILE LOOP EXAMPLES
# ============================================================
# Three classic while loops from the chapter:
#
# 1. PRINT EACH DIGIT of a number, right to left:
#      num % 10  gives the rightmost digit
#      num // 10 removes the rightmost digit
#    Loop while num > 0. (Note: a negative number prints nothing.)
#
# 2. GREATEST COMMON DIVISOR (Euclid's algorithm):
#      if num_a > num_b: num_a = num_a - num_b
#      else:             num_b = num_b - num_a
#      repeat until they are equal - that value is the GCD.
#
# 3. CONVERSATION: reply with a random response until the user types
#    "Goodbye". random.randint(0, 2) returns a new random number from
#    0 to 2 each call. (A DOCSTRING is a multi-line string in triple
#    quotes, like the one at the top of this file.)
def s5_3():
    head("5.3  MORE WHILE LOOP EXAMPLES")

    num = 902                          # prints 2, then 0, then 9
    print("  digits of 902 (reversed):", end=" ")
    while num > 0:
        print(num % 10, end=" ")
        num = num // 10
    print()

    num_a, num_b = 15, 10              # GCD by repeated subtraction
    iterations = 0
    while num_a != num_b:
        if num_a > num_b:
            num_a = num_a - num_b
        else:
            num_b = num_b - num_a
        iterations += 1
    print(f"  GCD(15, 10) = {num_a} after {iterations} iterations")

    random.seed(5)                     # seed only so output repeats
    replies = ["Tell me more.", "Why do you say that?", "Interesting!"]
    user_texts = ["Hi", "I like loops", "Goodbye"]
    j = 0
    user_text = user_texts[j]
    while user_text != "Goodbye":
        print(f"  you: {user_text:<15} bot: {replies[random.randint(0, 2)]}")
        j += 1
        user_text = user_texts[j]
    print("  bot: Goodbye!")

    task("num_insects = 8. Write a while loop that runs while num_insects"
         "\n     is <= 100: print it, then double it. (8 16 32 64)")


# ============================================================
# 5.4  COUNTING
# ============================================================
# A LOOP VARIABLE can count iterations. The pattern:
#     loop_variable = 1                  <- initialize
#     while loop_variable <= 5:          <- condition
#         print(loop_variable)
#         loop_variable = loop_variable + 1   <- UPDATE
# Forgetting the update is the classic cause of an infinite loop.
#
# COMPOUND OPERATORS (shorthand):
#     x += 5   same as  x = x + 5
#     x -= 5   same as  x = x - 5
#     x *= 5   same as  x = x * 5
#     x /= 5   same as  x = x / 5
#
# VARIATIONS: count DOWN by decrementing, or step by more than 1, or
# multiply/divide. If you change how the variable updates, you may also
# need to change its initialization and the loop condition.
#
# APPLICATIONS: factorial (N! = N * (N-1) * ... * 1), the Fibonacci sequence.
def s5_4():
    head("5.4  COUNTING")

    loop_variable = 1
    while loop_variable <= 5:
        print("  count:", loop_variable)
        loop_variable += 1
    print("  loop ended, loop_variable =", loop_variable)   # 6

    variation = 10                      # count DOWN in steps of 5
    print("  counting down: ", end="")
    while variation >= 0:
        print(variation, end=" ")
        variation -= 5
    print("(next value -5 ends it)")

    factorial, count = 4, 3             # 4! = 4*3*2*1
    while count >= 1:
        factorial *= count
        count -= 1
    print("  Factorial: 4! =", factorial)

    count, first, second = 5, 1, 1      # Fibonacci
    print("  Fibonacci:", first, second, end=" ")
    while count > 0:
        sequence = first + second
        print(sequence, end=" ")
        first, second = second, sequence
        count -= 1
    print()

# ============================================================
# 5.5  FOR LOOPS
# ============================================================
#     for variable in container:
#         loop body
# Each iteration assigns the variable the NEXT element of the container.
# The container is typically a list, string, or dictionary.
#
# - Over a STRING: the variable gets each character, left to right.
# - Over a DICTIONARY: the variable gets each KEY, in insertion order.
#   Look up the value with the key.
# - reversed(container) iterates backward, last element to first.
#
# A for loop repeats a DEFINED number of times - it stops when the
# elements run out, so it cannot accidentally become infinite.
def s5_5():
    head("5.5  FOR LOOPS")

    for list_name in ["Kai", "Sam", "Alex"]:
        print(f"  Hi {list_name}!")
    print("  Done")

    for char in "Yes":
        print("  char:", char)

    channels = {"MTV": 35, "CNN": 28, "NBC": 4}
    for channel_name in channels:                  # iterates over KEYS
        print(f"  {channel_name} is on channel {channels[channel_name]}")

    daily_revenues = [2350.25, 1800.50, 1795.00, 2050.25,
                      1985.75, 2005.00, 1890.50]
    total = 0
    for day in daily_revenues:
        total += day
    print(f"  Weekly revenue: ${total:.2f}")
    print(f"  Daily average revenue: ${total/len(daily_revenues):.2f}")

    names = ["Biffle", "Bowyer", "Busch"]
    print("  forward: ", end="")
    for name in names:
        print(name, "|", end=" ")
    print("\n  reversed:", end=" ")
    for name in reversed(names):
        print(name, "|", end=" ")
    print()

    task("temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]."
         "\n     Use a for loop to count how many are below freezing (< 0).")


# ============================================================
# 5.6  COUNTING USING THE range() FUNCTION
# ============================================================
# range() generates a sequence of integers: it starts at the START
# (included), steps by STEP, and stops BEFORE the END (not included).
#
#   range(Y)        all non-negative integers < Y      range(3)  -> 0 1 2
#   range(X, Y)     integers >= X and < Y              range(3,7)-> 3 4 5 6
#   range(X, Y, Z)  step by Z; Z may be NEGATIVE       range(5,0,-1)-> 5 4 3 2 1
#
# range() creates a "range" OBJECT. It is a sequence type like a list
# or tuple, but IMMUTABLE, and is generally only used in a for loop.
def s5_6():
    head("5.6  COUNTING USING THE range() FUNCTION")

    print("  range(5)         ->", list(range(5)))
    print("  range(3, 7)      ->", list(range(3, 7)))
    print("  range(-7, -3)    ->", list(range(-7, -3)))
    print("  range(0, 50, 10) ->", list(range(0, 50, 10)))
    print("  range(0, 5, 2)   ->", list(range(0, 5, 2)))
    print("  range(5, 0, -2)  ->", list(range(5, 0, -2)))
    print("  range(3, -1, -1) ->", list(range(3, -1, -1)))

    savings = 1000
    for year in range(1, 4):
        savings += savings * 0.05
        print(f"  year {year}: ${savings:.2f}")

    task("Write the SIMPLEST range() for each:"
         "\n     (a) every integer 0 to 500   (b) every integer 10 to 20"
         "\n     (c) every 2nd integer 10 to 20  (d) every integer 5 down to -5")


# ============================================================
# 5.7  WHILE vs. FOR LOOPS
# ============================================================
# These two are equivalent:
#     i = 0                        for i in range(100):
#     while i < 100:                   # body
#         # body
#         i += 1
#
# A for loop with range() is generally PREFERRED over a while loop for
# counting, because a for loop iterates over a finite container and is
# guaranteed to finish - a while loop can hang if you forget to update.
#
# General guidelines (not hard rules):
#   1. for   - when the number of iterations is computable in advance
#              (count down from X to 0, print a string N times)
#   2. for   - when accessing the elements of a container
#   3. while - when the number of iterations is NOT known in advance
#              (repeat until the user enters a particular character)
def s5_7():
    head("5.7  WHILE vs. FOR LOOPS")

    total = 0                       # for version
    for i in range(1, 6):
        total += i
    print("  for   version, total =", total)

    total, i = 0, 1                 # while version, same result
    while i <= 5:
        total += i
        i += 1
    print("  while version, total =", total)

    balance, years = 1000, 0        # only while fits: count unknown
    while balance < 1500:
        balance *= 1.10
        years += 1
    print(f"  while is required here: {years} years to pass $1500")

    task("while or for?"
         "\n     (a) iterate as long as user-entered string c is not 'q'"
         "\n     (b) iterate until x and y are equal (both change in the body)"
         "\n     (c) iterate 1500 times")


# ============================================================
# 5.8  NESTED LOOPS
# ============================================================
# A NESTED LOOP is a loop in the body of another loop: the OUTER loop
# and the INNER loop. For every ONE iteration of the outer loop, the
# inner loop runs ALL the way through.
# Total inner-body executions = outer count x inner count.

def s5_8():
    head("5.8  NESTED LOOPS")

    num_rows, num_cols = 2, 3                 # print a rectangle
    for rows in range(num_rows):
        for cols in range(num_cols):
            print("*", end=" ")
        print()

    for current_row in range(1, 3):           # theater seat labels
        current_column_letter = "A"
        for current_column in range(1, 4):
            print(f"  {current_row}{current_column_letter}", end="")
            current_column_letter = chr(ord(current_column_letter) + 1)
        print()

    print("  histogram: 40 ->", end=" ")      # one * per 5 units
    for i in range(40 // 5):
        print("*", end="")
    print()

    task("for i in range(5): for j in range(10, 12): print(...)"
         "\n     How many times does print run? Then write nested loops"
         "\n     that print a 3-row, 4-column rectangle of '*'.")


# ============================================================
# 5.9  DEVELOPING PROGRAMS INCREMENTALLY
# ============================================================
# Do NOT write the whole program and then run it hoping it works - if
# it fails you may have many bugs at once, and debugging is hard.
# INCREMENTAL PROGRAMMING: start with a simple version and grow it
# little by little, running it at every step.
#
# A FIXME comment marks code that still needs work. Many editors
# highlight them. Large projects add a name and date:
#     # FIXME(01/22/2018, John): handle lowercase letters
# A finished program should have NO FIXME comments left.
#
# Example: convert a phone number with letters (1-555-HOLIDAY) to digits.
def s5_9():
    head("5.9  DEVELOPING PROGRAMS INCREMENTALLY")

    user_input = "1-555-HOLIDAY"

    print("  Version 1 - just echo each element, check the loop works:")
    index = 0
    for character in user_input[:4]:
        print(f"    Element {index} is: {character}")
        index += 1
    print("    ...")

    print("  Version 2 - keep digits, '?' for everything else:")
    phone_number = ""
    for character in user_input:
        if "0" <= character <= "9":
            phone_number += character
        else:
            phone_number += "?"
    print("    Numbers only:", phone_number)
    # FIXME: add elif branches for letters and the hyphen

    print("  Version 3 - also keep hyphens, and decode A-C as 2:")
    phone_number = ""
    for character in user_input:
        if ("0" <= character <= "9") or (character == "-"):
            phone_number += character
        elif ("a" <= character <= "c") or ("A" <= character <= "C"):
            phone_number += "2"
        else:
            phone_number += "?"
    print("    Numbers only:", phone_number)

    print("  Version 4 - all keypad letters decoded:")
    keypad = {"abc": "2", "def": "3", "ghi": "4", "jkl": "5",
              "mno": "6", "pqrs": "7", "tuv": "8", "wxyz": "9"}
    phone_number = ""
    for character in user_input:
        if ("0" <= character <= "9") or (character == "-"):
            phone_number += character
        else:
            phone_number += "?"
            for letters in keypad:
                if character.lower() in letters:
                    phone_number = phone_number[:-1] + keypad[letters]
    print("    Numbers only:", phone_number)

    task("True or False: (a) incremental programming reduces errors,"
         "\n     (b) FIXME comments help you remember what to add,"
         "\n     (c) a finished program should still contain FIXMEs.")


# ============================================================
# 5.10  BREAK AND CONTINUE
# ============================================================
# break    - exits the loop IMMEDIATELY.
# continue - jumps immediately back to the while/for header, skipping
#            the rest of the current iteration.
# Each affects only the loop it is directly inside (in nested loops,
# the INNER loop) - that is why the example below breaks twice.
#
# Both can make a loop easier to read by avoiding complex conditions
# and excessive indenting. But a reader can easily OVERLOOK them, so
# use them only when their purpose is clear.
def s5_10():
    head("5.10  BREAK AND CONTINUE")

    # break: find the FIRST meal that spends the money exactly
    empanada_cost, taco_cost, user_money = 3, 4, 20
    max_empanadas = user_money // empanada_cost
    max_tacos = user_money // taco_cost
    meal_cost = 0
    for num_tacos in range(max_tacos + 1):
        for num_empanadas in range(max_empanadas + 1):
            meal_cost = num_empanadas * empanada_cost + num_tacos * taco_cost
            if meal_cost == user_money:
                break                      # exits the INNER loop only
        if meal_cost == user_money:
            break                          # exits the OUTER loop
    if meal_cost == user_money:
        print(f"  ${meal_cost} buys {num_empanadas} empanadas and"
              f" {num_tacos} tacos without change.")

    # continue: show ALL meals whose item count splits evenly among diners
    user_money, num_diners = 60, 3
    max_empanadas = user_money // empanada_cost
    max_tacos = user_money // taco_cost
    num_options = 0
    for num_tacos in range(max_tacos + 1):
        for num_empanadas in range(max_empanadas + 1):
            if (num_tacos + num_empanadas) % num_diners != 0:
                continue                   # skip the rest of this pass
            meal_cost = num_empanadas * empanada_cost + num_tacos * taco_cost
            if meal_cost == user_money:
                print(f"  ${meal_cost} buys {num_empanadas} empanadas and"
                      f" {num_tacos} tacos without change.")
                num_options += 1
    if num_options == 0:
        print("  You cannot buy a meal without having change left over.")

    task("'Simon says': compare simon = 'RRGBRYYBGY' to user = 'RRGBBRYBGY'"
         "\n     one index at a time. Add 1 point per match, break on the"
         "\n     first mismatch, then print the score.")


# ============================================================
# 5.11  LOOP else
# ============================================================
# A loop may have an else clause that executes ONLY if the loop
# terminated normally - that is, WITHOUT hitting a break.
#
#     for name in iterable:          while expression:
#         body                           body
#     else:                          else:
#         runs if no break               runs if no break
#
# Read "else" as "no break". It is ideal for searches: the else branch
# is the "not found" case.
def s5_11():
    head("5.11  LOOP else")

    names = ["Janice", "Clarice", "Martin", "Veronica", "Jason"]

    for num in (2, 8):
        print(f"  print {num} names:", end=" ")
        for i in range(len(names)):
            if i == num:
                break                      # break -> else is SKIPPED
            print(names[i], end=" ")
        else:
            print("All names printed.", end="")
        print()

    legal = ["Bjork", "Michael", "Nora"]   # Danish baby-name check
    for entered in ("Michaal", "Zoidberg"):
        for name in legal:
            if name[0] == entered[0]:
                print(f"  '{entered}' not legal - did you mean {name}?")
                break
        else:
            print(f"  '{entered}' has no close match at all.")

    task("x = 0, y = 5. Loop while x < y, breaking if x == z."
         "\n     What prints when z is 3? When z is 10?")


# ============================================================
# 5.12  enumerate() - BOTH INDEX AND VALUE
# ============================================================
# You often need the position AND the value. Two clumsy ways:
#     for index in range(len(origins)): value = origins[index]
#     for value in origins:             index = origins.index(value)
# (The second is also WRONG if the list has duplicates - index() always
#  finds the FIRST match.)
#
# enumerate() gives you both at once:
#     for (index, value) in enumerate(origins):
#
# Each iteration enumerate() yields a TUPLE (index, value), and the for
# loop UNPACKS it into two variables. Unpacking performs several
# assignments at once: num1, num2 = [350, 400] sets num1=350, num2=400.
def s5_12():
    head("5.12  enumerate() - BOTH INDEX AND VALUE")

    origins = [4, 8, 10]

    for index in range(len(origins)):              # clumsy way 1
        print(f"  range+len:  Element {index}: {origins[index]}")

    for (index, value) in enumerate(origins):      # the clean way
        print(f"  enumerate:  Element {index}: {value}")

    num1, num2 = [350, 400]                        # unpacking
    print("  unpacking: num1 =", num1, " num2 =", num2)

    orders_queue = ["latte", "mocha", "chai"]      # numbering from 1
    for (k, beverage_name) in enumerate(orders_queue):
        print(f"  #{k + 1}: {beverage_name}")

    task("my_list = ['Greek', 'Nordic', 'Mayan']. Use enumerate to print"
         "\n     each index and value on its own line.")


if __name__ == "__main__":
    print(__doc__)
    for section in (s5_1, s5_2, s5_3, s5_4, s5_5, s5_6, s5_7, s5_8,
                    s5_9, s5_10, s5_11, s5_12, s5_13, labs):
        section()
