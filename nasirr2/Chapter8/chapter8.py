"""
CHAPTER 8 · LISTS AND DICTIONARIES
"""
import sys

# ═══════════════════════════════════════════════════════════════════════════
# 8.1 LISTS
# • A list is a MUTABLE, ordered CONTAINER:  [ ]  or  list(iterable)
# • Elements can be any type (even other lists). Index starts at 0; -1 = last.
# • The index must be an int. Out of range → IndexError.
# • In-place changes: my_list[i] = x   and   del my_list[i]
#   Slicing and + create NEW lists.
# • b = a  → same list, two names.     b = a[:]  → a real copy.
# ═══════════════════════════════════════════════════════════════════════════

my_list = ["hello", -4.2, 5]
print(f"{my_list[0]=}  {my_list[-1]=}  {len(my_list)=}  {list('abc')=}")
# my_list[3]    → IndexError: list index out of range
# my_list[1.0]  → TypeError: list indices must be integers

nums = [1, 2, 3]
nums[2] = 9                       # change an element in place → [1, 2, 9]
del nums[1]                       # delete an element in place → [1, 9]
print(f"{nums=}  {nums + [4]=}  {nums[0:1]=}")

my_teams = ["Raptors", "Heat", "Nets"]
your_teams = my_teams             # SAME list
copy_teams = my_teams[:]          # NEW list
my_teams[1] = "Lakers"
print(f"{your_teams=}  {copy_teams=}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.2 LIST METHODS  (all change the list in place)
# • Add:     append(x)  extend([x, y])  insert(i, x)
# • Remove:  remove(x) by VALUE (missing → ValueError)   pop() / pop(i) by INDEX
# • Order:   sort()  reverse()          Info: index(x)  count(x)
# ═══════════════════════════════════════════════════════════════════════════

vals = [5, 8]
vals.append(16)                   # [5, 8, 16]
vals.extend([4, 12])              # [5, 8, 16, 4, 12]
vals.insert(1, 1.7)               # [5, 1.7, 8, 16, 4, 12]
vals.remove(8)                    # [5, 1.7, 16, 4, 12]
last = vals.pop()                 # removes and returns 12
first = vals.pop(0)               # removes and returns 5
print(f"{vals=}  {last=}  {first=}")

scores = [14, 5, 8, 5]
scores.sort()                     # [5, 5, 8, 14]
scores.reverse()                  # [14, 8, 5, 5]
print(f"{scores=}  {scores.index(8)=}  {scores.count(5)=}")
# ✗ scores = scores.sort()  → scores becomes None (methods return None)

# ═══════════════════════════════════════════════════════════════════════════
# 8.3 ITERATING OVER A LIST
# • for item in my_list            → each element
# • for i in range(len(my_list))   → each index
# • for i, item in enumerate(...)  → index AND element
# • Start a "best so far" variable at None (0 can give the wrong answer)
# • Built-ins: sum() max() min() any() all()
# ═══════════════════════════════════════════════════════════════════════════

nums = [3, 5, 23, -1, 456, 1, 6, 83]
for index, value in enumerate(nums[:3]):
    print(f"{index}: {value}")

max_even = None                   # "nothing found yet"
for num in nums:
    if num % 2 == 0:
        if max_even == None or num > max_even:
            max_even = num
print(f"Max even #: {max_even}")

print(f"{sum(nums)=}  {max(nums)=}  {min(nums)=}")
print(f"{any([0, 2])=}  {all([0, 1])=}  {all([])=}")
# nums[10]  → IndexError (the loop never goes past the last index)

# ═══════════════════════════════════════════════════════════════════════════
# 8.4 LIST GAMES — three classic loop patterns
# • Find the max:  store a value when a bigger one appears
# • Count:         increment a counter when a condition is true
# • Swap pass:     swapping neighbors moves the largest value to the end
# ═══════════════════════════════════════════════════════════════════════════

values = [12, -5, 30, 7, -2, 18]
best = values[0]
negatives = 0
for value in values:
    if value > best:
        best = value
    if value < 0:
        negatives += 1
print(f"{best=}  {negatives=}")

for i in range(len(values) - 1):
    if values[i] > values[i + 1]:
        values[i], values[i + 1] = values[i + 1], values[i]     # swap
print(f"After one swap pass: {values}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.5 LIST NESTING
# • A list can hold lists → a table:  table[row][col]
# • Nested loops: outer loop = each row, inner loop = each item in that row
# • Any depth works: cube[a][b][c]
# ═══════════════════════════════════════════════════════════════════════════

tic_tac_toe = [["X", "O", "X"],
               [" ", "X", " "],
               ["O", "O", "X"]]
print(f"{tic_tac_toe[0]=}  {tic_tac_toe[1][1]=}")
tic_tac_toe[1][0] = "O"           # change one cell

for row in tic_tac_toe:           # print the board
    for cell in row:
        print(cell, end=" ")
    print()

currency = [[1, 5, 10], [0.75, 3.77, 7.53]]
for r, row in enumerate(currency):
    for c, item in enumerate(row):
        print(f"currency[{r}][{c}] = {item:.2f}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.6 LIST SLICING   my_list[start:end:stride]  → NEW list, end NOT included
# • [:end] from the start   [start:] to the end   [:] full copy
# • Negative numbers count from the end; an end past the list is fine
# • end before start → []
# ═══════════════════════════════════════════════════════════════════════════

years = [1992, 1996, 2000, 2004, 2008]
print(f"{years[0:2]=}  {years[2:]=}  {years[:3]=}")
print(f"{years[0:-1]=}  {years[-3:-1]=}  {years[::2]=}")
print(f"{years[3:20]=}  {years[3:1]=}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.7 LOOPS MODIFYING LISTS
# • To change VALUES → loop over indices: my_list[i] = ...
#   (assigning to the loop variable does NOT change the list)
# • To change SIZE (remove items) → loop over a COPY: for x in my_list[:]
# ═══════════════════════════════════════════════════════════════════════════
print("\n=== 8.7 Loops modifying lists ===")
nums = [5, -5, -4, 6]
for num in nums:
    if num < 0:
        num = 0                   # ✗ only changes num
print(f"Loop variable: {nums}")
for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0               # ✓ changes the list
print(f"Index loop:    {nums}")

remove_these = [15, 20, 25, 30]
nums1 = [5, 10, 15, 20]
for val in nums1:                 # ✗ removing while looping skips elements
    if val in remove_these:
        nums1.remove(val)
print(f"Without copy:  {nums1}")  # 20 was skipped
nums1 = [5, 10, 15, 20]
for val in nums1[:]:              # ✓ loop over a copy
    if val in remove_these:
        nums1.remove(val)
print(f"With copy:     {nums1}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.8 LIST COMPREHENSIONS   [expression  for item in iterable  if condition]
# • Builds a NEW list in one line; the "if" part is optional
# ═══════════════════════════════════════════════════════════════════════════

my_list = [5, 20, 50]
print(f"{[i + 10 for i in my_list]=}")
print(f"{[int(t) for t in '7 9 3'.split()]=}")              # text → ints
print(f"{[sum(row) for row in [[5, 10], [2, 3], [100]]]=}")  # sum of each row
print(f"{[n for n in [5, 52, 16, 7] if n % 2 == 0]=}")       # evens only

# ═══════════════════════════════════════════════════════════════════════════
# 8.9 SORTING LISTS
# • my_list.sort() → in place, returns None     sorted(my_list) → NEW list
# • key=function compares function(item);  reverse=True → high to low
# • Strings sort by character code: "Z" (90) comes before "a" (97)
# ═══════════════════════════════════════════════════════════════════════════

numbers = [-5, 5, -100, 23]
print(f"{sorted(numbers)=}  {numbers=} (unchanged)")
names = ["Venus", "rafael", "Serena", "john"]
print(f"{sorted(names)=}")
print(f"{sorted(names, key=str.lower)=}")
print(f"{sorted([[25], [15, 35], [10, 15]], key=max)=}")
print(f"{sorted(numbers, reverse=True)=}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.10 COMMAND-LINE ARGUMENTS
# • > python myprog.py Tricia 12   →  sys.argv == ["myprog.py", "Tricia", "12"]
# • argv[0] is the program name; every argument is a STRING (convert with int())
# • Spaces separate arguments; quotes keep one: "Mary Jane"
# • Check len(sys.argv) first and print a usage message if it's wrong
# ═══════════════════════════════════════════════════════════════════════════

def greet(argv):                          # a real program would use sys.argv
    if len(argv) != 3:
        print("Usage: python myprog.py name age")
        return                            # a real program would call sys.exit(1)
    name = argv[1]
    age = int(argv[2])
    print(f"Hello {name}. {age} is a great age.")

greet(["myprog.py", "Tricia", "12"])      # > python myprog.py Tricia 12
greet(["myprog.py", "Franco"])            # > python myprog.py Franco
greet(["myprog.py", "Mary Jane", "65"])   # > python myprog.py "Mary Jane" 65
print(f"This script received: {sys.argv}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.11 ENGINEERING EXAMPLES — lists hold measurements; 2-D lists are matrices
# ═══════════════════════════════════════════════════════════════════════════

voltage = 12.0                            # resistors in series: I = V / total R
resistors = [3.3, 1.5, 2.0, 4.0, 2.2]
current = voltage / sum(resistors)
for i, r in enumerate(resistors):
    print(f"Resistor {i + 1}: {current * r:.1f} V")

m1 = [[1, 2], [3, 4]]                     # matrix multiplication
m2 = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += m1[i][k] * m2[k][j]
print(f"m1 x m2 = {result}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.12 DICTIONARIES   key → value  (like word → definition)
# • {"Jose": "A+"}   dict(Jose="A+")   dict([("Jose", "A+")])
# • d[key] reads (missing → KeyError)   d[key] = v adds OR modifies
# • del d[key] removes    key in d tests      Values can be anything (even lists)
# ═══════════════════════════════════════════════════════════════════════════

grades = {"Jose": "A+", "Gino": "C-"}
grades["Jose"] = "B+"                     # modify
grades["Jason"] = ["B+", "A-"]            # add
del grades["Gino"]                        # remove
print(f"{grades=}  {grades['Jose']=}  {'Gino' in grades=}")
# grades["Bob"]  → KeyError: 'Bob'

# ═══════════════════════════════════════════════════════════════════════════
# 8.13 DICTIONARY METHODS
# • get(key, default) → no KeyError      update(other) → merge in
# • pop(key, default) → remove + return   clear() → empty it
# ═══════════════════════════════════════════════════════════════════════════

menu = {"fries": 2.39, "burger": 3.50}
print(f"{menu.get('fries', 0)=}  {menu.get('soda', 0)=}")
menu.update({"soda": 1.49, "burger": 3.69})    # adds soda, changes burger
removed = menu.pop("fries")
print(f"{menu=}  {removed=}")
menu.clear()
print(f"{menu=}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.14 ITERATING OVER A DICTIONARY
# • for key in d   ·   for key, value in d.items()   ·   d.keys()   d.values()
# • keys/values/items are VIEWS: they update when the dict changes;
#   they can't be indexed → use list(d.keys())
# ═══════════════════════════════════════════════════════════════════════════

calories = {"Coke": 90, "Coke_zero": 0, "Pepsi": 94}
for soda, cal in calories.items():
    print(f"{soda}: {cal}")
sodas = calories.keys()
calories["Sprite"] = 140                  # the view sees the new key
print(f"{list(sodas)=}  {sorted(calories.values())=}")

# ═══════════════════════════════════════════════════════════════════════════
# 8.15 DICTIONARY NESTING
# • A value can be another dict:  students["Jose"]["Grade"]
# • Indent nested dicts so the structure is easy to read
# ═══════════════════════════════════════════════════════════════════════════
print("\n=== 8.15 Dictionary nesting ===")
gradebook = {
    "John":   {"Homeworks": [79, 80, 74], "Midterm": 85, "Final": 92},
    "Ricky":  {"Homeworks": [50, 52, 78], "Midterm": 40, "Final": 65},
}
for name, record in gradebook.items():
    total = sum(record["Homeworks"]) + record["Midterm"] + record["Final"]
    print(f"{name}: {100 * total / 500:.1f}%")
print(f"{gradebook['John']['Homeworks'][0]=}")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE
# ═══════════════════════════════════════════════════════════════════════════
print("\n=== End-of-class examples ===")

# 1. Count how many times each word appears.
def word_counts(text):
    pass
print(f"1. {word_counts('The cat and the hat')=}")

# 2. Remove duplicates but keep the original order.
def unique(items):
    pass
print(f"2. {unique([3, 1, 3, 2, 1])=}")

# 3. Sum each column of a 2-D list.
def column_sums(table):
    pass
print(f"3. {column_sums([[1, 2, 3], [4, 5, 6]])=}")

# 4. Squares of the odd numbers only (comprehension).
#your solution here

# 5. Names of the top 2 scores, best first.
# scores = {"Ann": 91, "Bo": 78, "Cy": 99, "Di": 85}
# top_two = #your solution here
# print(f"5. {top_two=}")
