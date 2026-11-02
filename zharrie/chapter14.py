"""
CHAPTER 14 - RECURSION

OBJECTIVES:
  1. Identify the BASE CASE and RECURSIVE CASE of a recursive function.
  2. Trace recursive calls (each call has its own namespace).
  3. Implement recursive binary search.
  4. Debug recursion with indented print statements.
  5. Build a recursive function in two steps; use outer/inner functions.
  6. Write recursive math functions; explain the recursion depth limit.
  7. Use recursion to explore all possibilities.
"""
import sys


# =====================================================================
# 14.1 RECURSIVE FUNCTIONS
# =====================================================================

"""
WHAT IS A RECURSIVE FUNCTION?
A function that calls ITSELF. Every recursive function needs:
  1. BASE CASE      - stops the recursion (no recursive call).
  2. RECURSIVE CASE - calls itself on a SMALLER problem, moving toward
                      the base case.
There is no special syntax: parameters are defined like any function.

NAMESPACES: every call gets its OWN local variables, so each call below
has its own 'count' - they never overwrite each other.

    count_down(2)      count=2 -> prints 2, calls count_down(1)
      count_down(1)    count=1 -> prints 1, calls count_down(0)
        count_down(0)  count=0 -> prints Go! (base case), returns
      returns
    returns

ORDER MATTERS: code BEFORE the recursive call runs on the way DOWN;
code AFTER it runs on the way back UP (see count_up).
"""


def count_down(count):
    if count == 0:              # Base case
        print('Go!')
    else:                       # Recursive case
        print(count)
        count_down(count - 1)


def count_up(count):
    if count == 0:
        print('Start!')
    else:
        count_up(count - 1)     # recurse first ...
        print(count)            # ... print on the way back up


count_down(2)
count_up(3)

"""
  Q1 How many calls does count_down(5) make?           6  (5,4,3,2,1,0)
  Q2 How many calls does count_down(0) make?           1
  Q3 Are recursive parameters defined differently?     No

COMMON MISTAKES: no base case, or a call that doesn't shrink the problem
(count_down(count) instead of count_down(count - 1)) -> infinite recursion.

IN-CLASS EXERCISES
  14.1  Trace by hand - what does mystery(4) print?
              def mystery(n):
                  if n <= 0:
                      print("done")
                  else:
                      print(n)
                      mystery(n - 2)
"""


# =====================================================================
# 14.2 RECURSIVE ALGORITHM: SEARCH
# =====================================================================

"""
RECURSIVE ALGORITHMS
An algorithm is a sequence of steps that solves a problem.
  Make lemonade (not recursive): add sugar, lemon juice, water, stir.
  Mow the lawn (recursive):  mow front (left, right), mow back (left,
  right) - the steps themselves are "mowing", just a smaller region.

GUESSING A NUMBER FROM 0-100
  By 1s ~50 guesses | by 10s then 1s ~10 | BINARY SEARCH ~7 at most.
  Binary search guesses the MIDPOINT and keeps only the half that can
  still hold the number:  find 32 -> 50 (lower), 25 (higher),
  38 (lower), 32 found.  Same algorithm, smaller range = RECURSIVE.

  find(low, high):  mid = (high + low) // 2
      "lower"  -> find(low, mid)
      "higher" -> find(mid + 1, high)   (mid was already checked; using
                  mid would repeat the window 99..100 forever)
      correct  -> BASE CASE, stop.

SEARCHING A SORTED LIST (Fig 14.2.2) - two base cases:
  item == lst[mid] -> return mid  |  range_size == 1 -> return -1 (not found)
  Otherwise RETURN the result of searching the lower or upper half.
  (Demo only - in practice use list.index() or the 'in' operator.)
  Binary search only works on SORTED data; upper/lower case matters.

RECURSION vs LOOPS: anything recursive can be done with loops, but
problems that reduce to SMALLER, IDENTICAL problems are good candidates.
"""

# 14.2.1: Guessing game (computer answers for secret = 41)
def find_guess(low, high, secret):
    mid = (high + low) // 2
    # answer = input(f"Is it {mid}? (l/h/y): ")
    answer = "l" if secret < mid else "h" if secret > mid else "y"
    print(f"Is it {mid}? (l/h/y): {answer}")
    if (answer != "l") and (answer != "h"):     # Base case
        print("Got it!")
    elif answer == "l":
        find_guess(low, mid, secret)
    else:
        find_guess(mid + 1, high, secret)


find_guess(0, 100, 41)

# Fig 14.2.2: Recursively searching a sorted list
def find(lst, item, low, high):
    """Finds index of item in sorted lst[low..high], else -1."""
    range_size = (high - low) + 1
    mid = (high + low) // 2
    if item == lst[mid]:            # Base case 1: found at mid
        pos = mid
    elif range_size == 1:           # Base case 2: not found
        pos = -1
    elif item < lst[mid]:           # Search lower half
        pos = find(lst, item, low, mid)
    else:                           # Search upper half
        pos = find(lst, item, mid + 1, high)
    return pos


attendees = ["Adams, Mary", "Carver, Michael", "Domer, Hugo",
             "Fredericks, Carlo", "Li, Jie"]
for name in ["Simpson, Homer", "Domer, Hugo"]:      # input()
    pos = find(attendees, name, 0, len(attendees) - 1)
    print(f"{name}: " + (f"Found at position {pos}." if pos >= 0 else "Not found."))

# Challenge 14.2.1: Searching for a letter
def search(char_list, match_char, lower_index, upper_index):
    print(f"Searching range from index {lower_index} to {upper_index}")
    range_size = (upper_index - lower_index) + 1
    mid_index = (lower_index + upper_index) // 2
    mid_char = char_list[mid_index]
    if match_char == mid_char:
        print(f"{match_char} is found at index {mid_index}")
    elif range_size == 1:
        print(f"{match_char} is not in the list")
    elif match_char < mid_char:
        search(char_list, match_char, lower_index, mid_index)
    else:
        search(char_list, match_char, mid_index + 1, upper_index)


letters = list("abdfgkmpstwz")
search(letters, "p", 0, len(letters) - 1)
search(letters, "c", 0, len(letters) - 1)

"""
IN-CLASS EXERCISES
  14.2-A  By hand: list every guess find_guess makes for 77.
  14.2-B  binary_search(nums, target, low, high) for a sorted list of ints;
          return the index or -1. Test: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
"""


# =====================================================================
# 14.3 ADDING OUTPUT STATEMENTS FOR DEBUGGING
# =====================================================================
# 14.3 ADDING OUTPUT STATEMENTS FOR DEBUGGING

"""
DEBUGGING WITH INDENTED PRINTS
Recursive functions are hard to debug - print statements help, and
INDENTING them shows the depth of recursion:
  * add a parameter 'indent'; start every print with it
  * the script starts with "   "; each recursive call passes indent + "   "
  * nothing is removed before returning - each call has its OWN indent
Tip: comment debug prints out (#) instead of deleting them. (Advanced:
Python's 'logging' module.)

TRY 14.3.1: change "pos = -1" to "pos = 0" in the not-found case and the
output shows "Person not found." then "Returning pos = 0." -> bug found!
(Below, the not_found parameter lets us inject that bug.)
"""


def find_debug(lst, item, low, high, indent, not_found=-1):
    print(f"{indent}find() range {low} {high}")
    range_size = (high - low) + 1
    mid = (high + low) // 2
    if item == lst[mid]:
        print(f"{indent}Found person.")
        pos = mid
    elif range_size == 1:
        print(f"{indent}Person not found.")
        pos = not_found                     # book: pos = -1
    elif item < lst[mid]:
        print(f"{indent}Searching lower half.")
        pos = find_debug(lst, item, low, mid, indent + '   ', not_found)
    else:
        print(f"{indent}Searching upper half.")
        pos = find_debug(lst, item, mid + 1, high, indent + '   ', not_found)
    print(f"{indent}Returning pos = {pos}.")
    return pos


# 14.3.1: search for 'Meeks, Stan'
find_debug(attendees, "Meeks, Stan", 0, len(attendees) - 1, "   ")
# 14.3.1: the bug (pos = 0) made visible for 'Aaron, Joe'
find_debug(attendees, "Aaron, Joe", 0, len(attendees) - 1, "   ", not_found=0)

"""
IN-CLASS EXERCISES
  14.3-B  This should sum a list but crashes with a TypeError. Use indented
          prints to find the bug, then fix it.
              def sum_list(nums):
                  if len(nums) == 0:
                      return 0
                  else:
                      nums[0] + sum_list(nums[1:])
"""


# =====================================================================
# 14.4 CREATING A RECURSIVE FUNCTION
# =====================================================================

"""
TWO STEPS
  1. Write the BASE CASE (returns without recursing) and TEST it.
     There may be several base cases.
  2. Add the RECURSIVE CASE and test again.

FACTORIAL: n! = n * (n-1)!, with 0! = 1! = 1
    nfact(4) = 4 * nfact(3) = 4 * 3 * nfact(2) = 4 * 3 * 2 * nfact(1) = 24
Factorial is just a demo: the loop version is as clear (and Python has
math.factorial). Recursion shines with data of unknown size/shape, e.g.
TREES. Ask first: (1) is there a natural recursive solution? (2) is it
better than a loop?  E = M*C*C: no. n!: yes, but not better.
Binary search: yes, and arguably clearer.

COMMON ERROR - infinite recursion: missing a base case (e.g. 0), or a
recursive case that never reaches it (e.g. nfact(-1)).

OUTER / INNER PATTERN
  OUTER factorial(n): called by the program, validates the input.
  INNER _factorial(n): does the recursion ("_" = internal use only);
  can take extra parameters the user shouldn't need to pass.
"""


def nfact(n):
    if n == 1 or n == 0:          # Step 1: base case
        fact = 1
    else:                         # Step 2: recursive case
        fact = n * nfact(n - 1)
    return fact


def factorial(n):
    """OUTER: validate, then start the recursion."""
    if n < 0:
        return None
    return _factorial(n)


def _factorial(n):
    """INNER: the recursion (assumes n >= 0)."""
    return 1 if n <= 1 else n * _factorial(n - 1)


sub("Factorials")
print("nfact(1) =", nfact(1), "| nfact(6) =", nfact(6))
print("factorial(5) =", factorial(5), "| factorial(-3) =", factorial(-3))

sub("Challenge 14.4.1: Output smileys")


def print_smiley(n):
    if n == 0:
        print(" happy ", end="")
    else:
        print("(:", end="")       # on the way down
        print_smiley(n - 1)
        print(":)", end="")       # on the way back up


print_smiley(4)                   # num_smiles = int(input())
print()

# Example: find_sum


def find_sum(in_value, total_val):
    print(in_value, end="")
    total_val += in_value
    if in_value <= 3:             # <- solution (base case)
        print(f" = {total_val}")
    else:
        print(" + ", end="")
        find_sum(in_value - 3, total_val)


find_sum(10, 0)

"""
IN-CLASS EXERCISES (use the two steps!)
  14.4-A  reverse_string(s) without slicing [::-1].     "abc" -> "cba"
  14.4-B  count_char(s, ch).                  count_char("banana", "a") -> 3
"""


# =====================================================================
# 14.5 RECURSIVE MATH FUNCTIONS
# =====================================================================

"""
FIBONACCI: 0, 1, 1, 2, 3, 5, 8, 13, ... (each number = sum of previous two)
  Fig 14.5.1 prints it step by step: fibonacci(v1, v2, run_cnt)
  Base case run_cnt <= 1: stop. Recursive: fibonacci(v2, v1 + v2, run_cnt - 1)
  Try 14.5.1: compute_nth_fib(n) RETURNS the nth number. Two base cases
  (0 -> 0, 1 -> 1); it makes TWO calls each time, so it gets slow fast.

GCD (Euclid, ~300 BC): subtract the smaller number from the larger until
  both are equal.  GCD(12, 8) = GCD(4, 8) = GCD(4, 4) = 4
  Base case: n1 == n2. Inputs must be >= 1.

DEPTH OF RECURSION = calls made but not yet returned. Each one uses
  memory, so Python limits it: sys.getrecursionlimit() (default ~1000),
  sys.setrecursionlimit(n). Going over raises RecursionError (a kind of
  RuntimeError - the name the book uses).
"""


def fibonacci(v1, v2, run_cnt):
    print(f"{v1} + {v2} = {v1 + v2}")
    if run_cnt <= 1:                        # Base case
        pass
    else:                                   # Recursive case
        fibonacci(v2, v1 + v2, run_cnt - 1)


def compute_nth_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return compute_nth_fib(n - 1) + compute_nth_fib(n - 2)


def gcd(n1, n2):
    if n1 == n2:                            # Base case
        return n1
    elif n1 < n2:                           # Recursive case
        return gcd(n1, n2 - n1)
    else:
        return gcd(n1 - n2, n2)


def rec_func(n):
    return 1 if n == 0 else rec_func(n - 1)


# Fibonacci, 10 steps
fibonacci(0, 1, 10)                         # run_for = int(input())
# compute_nth_fib
print("compute_nth_fib(4) =", compute_nth_fib(4), "| compute_nth_fib(10) =", compute_nth_fib(10))
# GCD
print("gcd(12, 8) =", gcd(12, 8), "| gcd(456, 784) =", gcd(456, 784))
# Recursion depth limit
print("Limit:", sys.getrecursionlimit())
for num in (500, 1000):
    try:
        print(f"rec_func({num}) =", rec_func(num))
    except RecursionError as err:
        print(f"rec_func({num}) -> RecursionError: {err}")

#raise_to_power 
def raise_to_power(base_val, exponent_val):
    if exponent_val == 0:
        result_val = 1
    else:
        result_val = base_val * raise_to_power(base_val, exponent_val - 1)  # <- solution
    return result_val


print("4^2 =", raise_to_power(4, 2))

"""
IN-CLASS EXERCISES
  14.5-A  Discuss: why is compute_nth_fib(35) slow? How many times is
          compute_nth_fib(1) called inside compute_nth_fib(5)?
"""


# =====================================================================
# 14.6 RECURSIVE EXPLORATION OF ALL POSSIBILITIES
# =====================================================================
section("14.6 RECURSIVE EXPLORATION OF ALL POSSIBILITIES")

r"""
EXPLORING ALL POSSIBILITIES: reorderings of letters, subsets of items,
paths between cities. Picture a TREE of choices (remaining/chosen):

                       abc/
          /             |             \
       bc/a           ac/b           ab/c       <- choose 1st letter
      /    \         /    \         /    \
   c/ab   b/ac    c/ba   a/bc    b/ca   a/cb    <- choose 2nd letter
    |      |       |      |       |      |
  /abc   /acb    /bac   /bca    /cab   /cba     <- leaves = BASE CASE

BASE CASE: nothing remaining -> output the result (a leaf).
RECURSIVE CASE: for EACH remaining option:
    CHOOSE it -> EXPLORE (recursive call) -> UN-CHOOSE it (put it back)
scramble() builds NEW strings, so nothing needs undoing. The shopping and
travel examples change lists IN PLACE, so they must undo each choice.

Note: the shopping spree prints ORDERED picks (24 lines), e.g. both
"Milk Belt Toys" and "Belt Milk Toys" - only 4 bags are truly different.
Possibilities grow fast: n letters -> n! orderings. Test small inputs.
"""


def scramble(r_letters, s_letters):
    if len(r_letters) == 0:                 # Base case: all letters used
        print(s_letters)
    else:                                   # Move each letter to scrambled
        for i in range(len(r_letters)):
            remaining_letters = r_letters[:i] + r_letters[i + 1:]
            scramble(remaining_letters, s_letters + r_letters[i])


max_items_in_bag = 3


def shopping_bag_combinations(curr_bag, remaining_items):
    if len(curr_bag) == max_items_in_bag:   # Base case: bag full
        names = "  ".join(item["name"] for item in curr_bag)
        print(f"{names} = {sum(item['price'] for item in curr_bag):.2f}")
    else:
        for index, item in enumerate(remaining_items):
            curr_bag.append(item)                       # choose
            remaining_items.pop(index)
            shopping_bag_combinations(curr_bag, remaining_items)   # explore
            remaining_items.insert(index, item)         # un-choose
            curr_bag.pop()


city_names = ["Boston", "Chicago", "Los Angeles"]
distances = [[0, 960, 2960],                # Boston
             [960, 0, 2011],                # Chicago
             [2960, 2011, 0]]               # Los Angeles


def travel_paths(curr_path, need_to_visit):
    if len(curr_path) == len(city_names):   # Base case: visited all cities
        total = sum(distances[curr_path[i - 1]][curr_path[i]] for i in range(1, len(curr_path)))
        print("".join(f"{city_names[c]:<13}" for c in curr_path) + f"= {total}")
    else:
        for i in range(len(need_to_visit)):
            city = need_to_visit.pop(i)                 # visit city
            curr_path.append(city)
            travel_paths(curr_path, need_to_visit)
            need_to_visit.insert(i, city)               # go back
            curr_path.pop()


items = [{"name": "Milk", "price": 1.25}, {"name": "Belt", "price": 23.55},
         {"name": "Toys", "price": 19.05}, {"name": "Cups", "price": 11.85}]

# scramble('cat')
scramble("cat", "")                         # word = input()
# Shopping spree (24 ordered picks)
shopping_bag_combinations([], items)
# Traveling salesman
travel_paths([], [0, 1, 2])


# explore()
def explore(remain_vals, picked_vals):
    if len(remain_vals) == 0:
        print(*picked_vals)
    else:
        for i, val in enumerate(remain_vals):                       # <- solution
            explore(remain_vals[:i] + remain_vals[i + 1:], picked_vals + [val])


explore([1, 2, 3], [])

"""
Summary
  Base case      : stops the recursion (can be more than one)
  Recursive case : calls itself on a SMALLER problem
  Namespace      : each call has its own local variables
  Before / after : code before the call runs going down, after it going up
  Binary search  : check middle, recurse on (low, mid) or (mid+1, high); SORTED
  Debugging      : 'indent' parameter, each call adds "   "
  Creating       : 1) base case + test  2) recursive case + test
  Outer / inner  : factorial(n) validates -> _factorial(n) recurses
  Depth limit    : sys.getrecursionlimit() ~1000 -> RecursionError
  Explore all    : choose -> explore -> un-choose
"""


