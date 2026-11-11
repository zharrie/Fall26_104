"""
CHAPTER 10 · EXCEPTIONS
"""
import os

# ═══════════════════════════════════════════════════════════════════════════
# 10.1 HANDLING EXCEPTIONS USING TRY AND EXCEPT
# • Exception = an error that happens WHILE the program runs.
#   Not handled → Python prints a traceback and the program STOPS.
# • Put code that might fail in a try block; the except block runs only if it fails.
# • When a line fails, the REST of the try block is skipped → except runs →
#   the program continues after the except block.
# • Common types: ValueError (bad value), ZeroDivisionError, KeyError (missing
#   dict key), IndexError (index out of range), EOFError (input() found no input)
# ═══════════════════════════════════════════════════════════════════════════

def bmi_report(weight_text, height_text):         # in class: values from input()
    try:
        weight = int(weight_text)
        height = int(height_text)
        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi:.1f}  (CDC: 18.6-24.9 normal)")
    except:
        print("Could not calculate health info.")
    print("...program keeps running")

bmi_report("150", "66")
bmi_report("One-hundred fifty", "66")    # without try: ValueError → program stops

print("Common exception types:")
# eval() runs a string as code — used here only to show several errors quickly
for code in ['int("Ten")', '10 / 0', '{"Jose": "A+"}["Bob"]', '[1, 2, 3][5]']:
    try:
        eval(code)
    except Exception as err:
        print(f"  {code:<24} → {type(err).__name__}")

# ═══════════════════════════════════════════════════════════════════════════
# 10.2 MULTIPLE EXCEPTION HANDLERS
# • One except block per type:  except ValueError:   except ZeroDivisionError:
# • One block for several types: except (TypeError, NameError):
# • except: alone is a catch-all — it must come LAST and should be used rarely
#   (it also hides real bugs, like a misspelled variable name)
# • Handlers are checked top to bottom; only the FIRST match runs.
#   No match → the exception is unhandled and the program stops.
# ═══════════════════════════════════════════════════════════════════════════

def bmi_report2(weight_text, height_text):
    try:
        weight = int(weight_text)
        height = int(height_text)
        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi:.1f}")
    except ValueError:
        print("Could not calculate health info.")
    except ZeroDivisionError:
        print("Invalid height entered. Must be > 0.")

bmi_report2("150", "66")
bmi_report2("abc", "66")
bmi_report2("150", "0")

for value in ["5", 5, None]:
    try:
        total = value + 5                     # "5" + 5 and None + 5 → TypeError
        print(f"{value!r} + 5 = {total}")
    except (TypeError, NameError):
        print(f"{value!r} + 5 → handled TypeError")

# ═══════════════════════════════════════════════════════════════════════════
# 10.3 RAISING EXCEPTIONS
# • raise ValueError("Invalid weight.") creates and throws an exception right now
# • except ValueError as excpt:  → excpt is the exception; print(excpt) shows its message
# • Error checks stay out of the main logic, so the normal steps are easy to read
# ═══════════════════════════════════════════════════════════════════════════

def bmi_report3(weight, height):
    try:
        if weight < 0:
            raise ValueError("Invalid weight.")
        if height <= 0:
            raise ValueError("Invalid height.")
        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi:.1f}")
    except ValueError as excpt:
        print(f"{excpt} Could not calculate health info.")

bmi_report3(150, 66)
bmi_report3(-1, 66)
bmi_report3(150, 0)
# ✗ raise "Invalid weight"  → TypeError: you must raise an exception object

# ═══════════════════════════════════════════════════════════════════════════
# 10.4 EXCEPTIONS WITH FUNCTIONS
# • If a function raises and does not handle the exception, the function
#   exits immediately and the exception goes back to the CALLER.
# • The caller's try/except handles it → no need for special return values like -1.
# ═══════════════════════════════════════════════════════════════════════════

def get_weight(text):
    weight = int(text)
    if weight < 0:
        raise ValueError("Invalid weight.")
    return weight                     # skipped if raise ran

def get_height(text):
    height = int(text)
    if height <= 0:
        raise ValueError("Invalid height.")
    return height

for w, h in [("150", "66"), ("-1", "66"), ("150", "-1")]:
    try:                              # the caller handles errors from both functions
        weight = get_weight(w)
        height = get_height(h)
        print(f"BMI: {(weight / (height * height)) * 703:.1f}")
    except ValueError as excpt:
        print(excpt)

# ═══════════════════════════════════════════════════════════════════════════
# 10.5 USING FINALLY TO CLEAN UP
# • finally: runs ALWAYS — error or not, handled or not — and comes LAST
# • Use it for clean-up, such as closing a file
# • Even if try or except uses return, finally runs first
# ═══════════════════════════════════════════════════════════════════════════

def divide(a, b):
    z = -1
    try:
        z = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print(f"Result is {z}")

divide(4, 2)
divide(4, 0)

with open("good.txt", "w") as f:              # make two small demo files
    f.write("5\n423\n234\n")
with open("letters.txt", "w") as f:
    f.write("five\n")

for file_name in ["good.txt", "letters.txt", "missing.txt"]:
    nums = []
    rd_nums = None
    try:
        rd_nums = open(file_name, "r")         # missing file → IOError
        for line in rd_nums:
            nums.append(int(line))             # bad text → ValueError
    except IOError:
        print(f"Could not find {file_name}")
    except ValueError:
        print(f"Could not read number from {file_name}")
    finally:
        print(f"Closing {file_name}")
        if rd_nums != None:
            rd_nums.close()
    print(f"Numbers found: {nums}")

os.remove("good.txt")                          # remove the demo files
os.remove("letters.txt")

# ═══════════════════════════════════════════════════════════════════════════
# 10.6 CUSTOM EXCEPTION TYPES
# • Make your own type by inheriting from Exception:
#       class LessThanZeroError(Exception):
#           pass
# • End the name with "Error"; callers can then catch exactly your problem
# ═══════════════════════════════════════════════════════════════════════════

class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value                     # extra info stored on the exception

for my_num in [25, -100]:
    try:
        if my_num < 0:
            raise LessThanZeroError("my_num must be greater than 0")
        print(f"my_num: {my_num}")
    except LessThanZeroError as excpt:
        print(f"LessThanZeroError: {excpt.value}")

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE
# ═══════════════════════════════════════════════════════════════════════════


# 1. safe_int: return int(text), or a default if the text isn't a number.
def safe_int(text, default=0):
    pass
print(f"1. {safe_int('42')=}  {safe_int('forty-two', -1)=}")

# 2. Predict the output: does finally run before the return value is used?
def report():
    pass
print(f"2. then: {report()}")

# 3. percent: raise ValueError for bad data; the caller prints the message.
def percent(score, total):
    pass

for score, total in [(45, 50), (45, 0), (60, 50)]:
    pass

# 4. Custom exception: withdraw() raises InsufficientFundsError.
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"need ${amount - balance} more")
    return balance - amount

for amount in [30, 130]:
    try:
        print(f"4. New balance: {withdraw(100, amount)}")
    except InsufficientFundsError as excpt:
        print(f"4. Declined: {excpt}")

# 5. Average the numbers in a line of text, skipping bad tokens.
def average(text):
    pass
print(f"5. {average('10 x 20 -- 30')=}  {average('none here')=}")
