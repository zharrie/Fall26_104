
"""
=====================================================================
 CHAPTER 1 - INTRODUCTION TO PYTHON PROGRAMMING
 Run this file top-to-bottom, read the comments, then complete the
 exercises marked "EXERCISE" on your own (write your code right below
 the prompt, or in a separate file).
=====================================================================
"""

# =====================================================================
# 1. WHAT IS A PROGRAM?
# =====================================================================
# A program is a sequence of INSTRUCTIONS a computer executes one at a time. 
# Every program follows the pattern:  INPUT -> PROCESS -> OUTPUT
# Variables (x, y, z below) store data that can change ("vary").

x = 2
y = 5
z = x + y            # PROCESS: compute
print(z)             # OUTPUT: display the result

# EXERCISE 1.1: Change x and y above to 10 and 20. Predict z, then run
#               the file to check your answer.


# =====================================================================
# 2. WHAT IS PYTHON?
# =====================================================================
# Python is a high-level, general-purpose programming language known for readable, almost English-like syntax.
# Key traits:
#   - INTERPRETED, not compiled: no separate "build" step; an interpreter (Section 3) runs your code directly.
#   - DYNAMICALLY TYPED: you don't declare a variable's type in advance - Python infers it from the assigned value.
#   - CONCISE: built-ins like print() and input() do a lot with little code.

# Brief history: Python was created by Guido van Rossum (first released 1991), named after the show "Monty Python's Flying Circus". 
# Python 3 (2008) is the modern, actively used version (Python 2 reached end-of-life in 2020).

# Real-world uses: 
# web development (Django, Flask), 
# data science & machine learning (pandas, NumPy, scikit-learn), 
# automation/scripting,
# scientific computing, and teaching programming fundamentals.

print("Python figured out the type on its own:")
x = 5
print(x, "is a", type(x).__name__)   # no type declaration needed

# EXERCISE 2.1: In one comment line, name TWO fields (other than the ones listed above) where Python might be useful.


# =====================================================================
# 3. THE PYTHON INTERPRETER & SCRIPTS
# =====================================================================
# The INTERPRETER is a program that reads Python code and executes it, one STATEMENT at a time.

# Two ways to use it:
#   1. INTERACTIVE INTERPRETER: type one line, press Enter, see the result immediately (shows a ">>>" prompt). 
#      Good for quick experiments - unwieldy for long programs.
#         >>> wage = 20
#         >>> print(wage * 2)
#         40
#   2. SCRIPT MODE: write all your code in a .py FILE; the interpreter reads and executes it top to bottom. 
#      This is how real programs (including this file!) are run, e.g. from a terminal:
#         $ python3 chapter1_intro_to_python.py
#
# An EXPRESSION is code that evaluates to a value (e.g. wage * hours).
# Comments (#) are ignored by the interpreter - they help human readers.

wage = 20
hours = 40
weeks = 52
salary = wage * hours * weeks       # an assignment statement
print("Salary is:", salary)         # print() displays text + values

hours = 35                          # variables can be reassigned
salary = wage * hours * weeks
print("New salary is:", salary)

# EXERCISE 3.1: Open a terminal, launch the interactive interpreter (type "python3"), and compute 15 * 8 line by line.
#               Then quit (type exit() or press Ctrl+D).


# =====================================================================
# 4. IDEs AND THE COMMAND LINE
# =====================================================================
# An Integrated Development Environment (IDE) bundles a text editor, the interpreter, and helper tools into one application (e.g. VS Code,
# PyCharm, IDLE). Common IDE features:
#   - Syntax highlighting: colors keywords/strings/variables, helping
#     you spot mistakes (like an unclosed quote) at a glance.
#   - Auto delimiter completion: typing "(" auto-adds ")".
#   - A "Run" shortcut button, and a file manager for multi-file projects.
#
# A CONSOLE (terminal) is a text interface for running programs, seeing
# their output, and typing input. Its COMMAND-LINE INTERFACE (CLI) lets
# you pass command-line arguments after the program name, e.g.:
#     python3 main.py 0.5 25      <- "0.5" and "25" are arguments
#
# EXERCISE 4.1: Name one advantage of using an IDE over a plain text
#               editor + separate terminal (write as a comment).


# =====================================================================
# 5. BASIC OUTPUT: print()
# =====================================================================
# print() accepts multiple comma-separated items; Python automatically
# inserts a single space between them and a newline at the end.

print("Hello there.")
print("My name is...", "Carl?")     # multiple items, one call

# --- Keeping output on the same line with end= ---
print("Hello there.", end=" ")
print("My name is...", end=" ")
print("Carl?")                      # all three appear on one line

# --- Escape sequences: \n (newline), \t (tab), \\ (backslash) ---
print("Name\tJob\n------------------")
print("Ann\tDeveloper\nJoe\tInfluencer")

# EXERCISE 5.1: Print the figure below using only print() statements:
# *****
# *   *
# *****
# EXERCISE 5.2: Print your email address, then on the SAME line print
#               " - verified" using end=.


# =====================================================================
# 6. BASIC INPUT: input()
# =====================================================================
# input() ALWAYS returns a string, even if the user types a number.
# Use int() or float() to convert that string before doing math.
# NOTE: real input() calls are commented out so this file runs without
# pausing; uncomment them and run in a terminal to try interactively.

# best_friend = input("Enter name of best friend: ")
# print("My best friend is", best_friend)

hourly_wage_text = "12"                  # pretend this came from input()
hourly_wage = int(hourly_wage_text)      # convert string -> int
print("Salary is", hourly_wage * 40 * 52)

# EXERCISE 6.1: Uncomment the two input() lines above and run the file
#               in a terminal (not just top-to-bottom) to try real input.
# EXERCISE 6.2: Write code (using input()) that reads two numbers typed
#               by the user and prints their product.


# =====================================================================
# 7. ERRORS: SYNTAX, RUNTIME, AND LOGIC
# =====================================================================
# SYNTAX ERROR: violates Python's grammar rules. Detected BEFORE the
# program runs. Example (do NOT uncomment - it would stop this file):
#     print("Hello"        <- missing closing parenthesis
#
# RUNTIME ERROR: valid syntax, but an impossible operation happens
# while the program runs, e.g. converting "Henry" to an integer.

try:
    number = int("Henry")          # raises ValueError
except ValueError as e:
    print("Runtime error caught:", e)

# LOGIC ERROR: the code runs fine but produces the WRONG result because
# the programmer made a mistake in the logic/formula.
current_salary = 10000
raise_percentage = 5          # BUG: should be 0.05 (5%), not 5 (500%!)
new_salary = current_salary + (current_salary * raise_percentage)
print("New salary (buggy):", new_salary)          # way too high!

raise_percentage_fixed = 0.05
new_salary_fixed = current_salary + (current_salary * raise_percentage_fixed)
print("New salary (fixed):", new_salary_fixed)

# Other common error TYPES you'll meet: NameError (using an undefined
# variable), TypeError (wrong type for an operation, e.g. "a" + 5),
# IndentationError (inconsistent indentation).

# EXERCISE 7.1: For each error type - SyntaxError, ValueError, NameError,
#               TypeError, IndentationError - write (as a comment) ONE
#               line of code that would trigger it.


# =====================================================================
# 8. HOW COMPUTERS RUN PROGRAMS (brief background)
# =====================================================================
# Under the hood, a computer's processor only understands 0s and 1s
# (bits), executing tiny machine instructions stored in memory (RAM).
# Early programmers wrote those 0s and 1s directly! High-level
# languages like Python let us write readable code instead:
#   - A COMPILER translates high-level code into a machine-executable
#     file ALL AT ONCE, before running (e.g. C, C++).
#   - An INTERPRETER (Section 3) reads and executes high-level code
#     directly, ONE LINE AT A TIME, without a separate build step - this is how Python works.


# =====================================================================
# 9. WHY WHITESPACE & PRECISION MATTER
# =====================================================================
# Programming demands EXACT precision: "=" vs "==", a missing space,
# an extra newline, or i vs j can all change a program's behavior or
# break automated grading. Always double-check output formatting.

print("Correctly formatted line 1.")
print("Correctly formatted line 2.")


# =====================================================================
# PRACTICE SET - try these on your own
# =====================================================================
# P1. Write a program that prints your name, and favorite language
#     on two separate lines using two separate print() calls.
# P2. Write a program that asks for a temperature in Celsius (input),
#     converts it to Fahrenheit using F = (9/5)*C + 32, and prints the
#     result. (Hint: convert the input string to float first.)
# P3. Ask the user for two numbers and print their sum, difference,
#     product, and quotient - each on its own line, clearly labeled.
# P4. Find and describe (in a comment) the bug in this snippet:
#         principal = 1000
#         rate = 5          # meant to be 0.05
#         interest = principal * rate
# P5. Print an ASCII art triangle of height 3, then a "trunk" below it:
#         *
#        ***
#       *****
#         |
