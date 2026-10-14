"""
==========================================================================
 CLASSES · EXCEPTIONS · MODULES · FILES
==========================================================================

"""
import os
import sys
import csv
import struct

# ═══════════════════════════════════════════════════════════════════════════
#
#                           PART A · CLASSES  (Ch. 9)
#
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# A1 · WHY CLASSES?                                                     (9.1)
# THE ANSWER - a class lets you bundle data with the operations on it, so you
# can model a problem the way you think about it. Concretely, classes give you:
#   1. ORGANIZATION - related data + behavior live in one place, instead of
#      loose variables and functions scattered across the program.
#   2. MODELING - code reads like the problem: a Seat, an Employee, a
#      BankAccount - not a pile of parallel lists and helper functions.
#   3. ENCAPSULATION - users call well-named operations (the interface) and
#      ignore the internal details, which you can change without breaking them.
#   4. REUSE - one blueprint builds many independent objects, each with its
#      own data; you write the logic once (see BankAccount reused all lecture).
#   5. SAFETY - the class can enforce its own rules (e.g. no negative deposit,
#      Part B), so invalid data can't sneak in.
#
# Supporting ideas:
# • Object = data (variables) + the operations on that data (methods)
# • People think in objects (chair, drawer), not materials (wood, metal).
#   Programs too: a Restaurant object, not loose variables and functions.
# • Abstraction / information hiding / encapsulation: use the oven's knob,
#   don't reach inside to adjust the flame.
# • ADT (abstract data type) = a type used only through well-defined
#   operations. A class is how Python implements an ADT.
# • You already use objects: str and int hold a value + useful methods
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A1 Why classes? ===")
s1 = "Hello!!"
i1 = 130
print(f"{type(s1)=}  {s1.isdigit()=}  {s1.lower()=}")
print(f"{type(i1)=}  {abs(-i1)=}  {float(i1)=}")

# ───────────────────────────────────────────────────────────────────────────
# A2 · CREATING A CLASS: GROUPING DATA                                  (9.2)
# • class Time:  creates a new TYPE. Class names use CapWords.
# • The class is the blueprint; an INSTANCE (object) is one thing built
#   from it:   my_time = Time()   <- calling the class creates an instance
# • __init__ is the CONSTRUCTOR: it runs automatically when you call Time()
# • self = the new object being built.  self.hours = 0 creates an ATTRIBUTE
#   (attributes = the object's data; other languages call them fields or
#   properties)
# • Dot notation reads and writes attributes:  my_time.hours = 7
# • Each instance has its OWN attribute values.
# • t2 = t1 does NOT copy - both names refer to the SAME object.
#
#              class Time   (blueprint)
#             /                       \
#     time1 = Time()             time2 = Time()
#     hours=7, minutes=15        hours=12, minutes=0
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A2 Creating a class ===")
class Time:
    """A time of day"""
    def __init__(self):
        self.hours = 0
        self.minutes = 0

time1 = Time()
time1.hours = 7
time1.minutes = 15
time2 = Time()
time2.hours = 12
print(f"time1 = {time1.hours}:{time1.minutes:02d}   time2 = {time2.hours}:{time2.minutes:02d}")
print(f"{type(time1)=}")
print(f"{vars(time1)=}")          # vars() shows an instance's own attributes
print(f"{vars(time2)=}")

same = time1                      # another NAME for time1, not a copy
same.hours = 9
print(f"{time1.hours=}  {same is time1=}")

# ───────────────────────────────────────────────────────────────────────────
# A3 · INSTANCE METHODS                                                 (9.3)
# • A method is a function inside a class. Its first parameter is self.
# • Call it with obj.method(); Python passes obj as self automatically:
#       alice.calculate_pay()   is the same as   Employee.calculate_pay(alice)
# • Inside the method, use self.attribute to reach the object's data.
# • Names like __init__ are special ("dunder") methods; don't invent new ones.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A3 Instance methods ===")
class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):
        return self.wage * self.hours_worked

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f"{alice.calculate_pay()=}")
print(f"{Employee.calculate_pay(alice)=}")      # what Python does behind the scenes
# ✗ def calculate_pay():  (no self)
#   -> TypeError: ... takes 0 positional arguments but 1 was given

# ───────────────────────────────────────────────────────────────────────────
# A4 · CONSTRUCTORS WITH PARAMETERS                                     (9.6)
# • __init__ can take parameters -> set attributes when the object is created
# • Parameters can have defaults:  def __init__(self, name, wage=8.25, hours=20)
# • Required parameters first; defaulted ones can be passed by name
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A4 Constructors with parameters ===")
class Worker:
    def __init__(self, name, wage=8.25, hours=20):
        self.name = name
        self.wage = wage
        self.hours = hours

todd = Worker("Todd")                           # uses the defaults
tricia = Worker("Tricia", wage=12.50, hours=40)
for w in [todd, tricia]:
    print(f"{w.name} earns {w.wage * w.hours:.2f} per week")
# Worker() -> TypeError: Worker.__init__() missing 1 required positional argument: 'name'

# ───────────────────────────────────────────────────────────────────────────
# A5 · CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES                          (9.4)
# • Class attribute: defined in the class body -> SHARED by every instance
# • Instance attribute: self.x = ... -> belongs to ONE instance
# • Lookup order: the instance first, then the class
# • Same name in both -> the instance's hides the class's (avoid this)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A5 Class vs instance attributes ===")
class MarathonRunner:
    race_distance = 42.195          # class attribute (km), shared

    def __init__(self, speed):
        self.speed = speed          # instance attribute, one per runner

runner1 = MarathonRunner(7.5)
runner2 = MarathonRunner(8.0)
print(f"{runner1.speed=}  {runner2.speed=}  {runner2.race_distance=}")

MarathonRunner.race_distance = 26.2             # change the class attribute...
print(f"{runner1.race_distance=}  {runner2.race_distance=}")   # ...everyone sees it

runner1.race_distance = 10.0                    # creates an attribute on runner1 only
print(f"{runner1.race_distance=}  {runner2.race_distance=}")
print(f"{vars(runner1)=}  {vars(runner2)=}")

# ───────────────────────────────────────────────────────────────────────────
# A6 · CLASS EXAMPLE: SEAT RESERVATION SYSTEM                           (9.5)
# • Each Seat keeps its own data AND its operations together
# • A list of objects models the whole plane; the main code reads like the
#   problem description
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A6 Seat reservation system ===")
class Seat:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.paid = 0.0

    def reserve(self, f_name, l_name, amt_paid):
        self.first_name = f_name
        self.last_name = l_name
        self.paid = amt_paid

    def make_empty(self):
        self.first_name = ""
        self.last_name = ""
        self.paid = 0.0

    def is_empty(self):
        return self.first_name == ""

    def print_seat(self):
        print(f"{self.first_name} {self.last_name}, Paid: {self.paid:.2f}")

seats = []
for i in range(3):
    seats.append(Seat())
seats[1].reserve("Ann", "Lee", 220.0)
for number, seat in enumerate(seats):
    print(f"Seat {number}: ", end="")
    if seat.is_empty():
        print("empty")
    else:
        seat.print_seat()

# ───────────────────────────────────────────────────────────────────────────
# A7 · CLASS INTERFACES                                                 (9.7)
# • Interface = the methods a user is meant to call
# • Implementation = the internal details (attributes, helper methods)
# • A leading underscore (_diff_time) just means "this is for internal use -
#   please don't call it from outside." It's a polite note to other
#   programmers, not a lock. Python still lets you call race._diff_time();
#   you're only ignoring the "keep out" sign.
#   (Two underscores, __x, are a bit stronger but still not truly private.
#   A name with no underscore is public - the normal way to use the class.)
# • Hiding details lets you change the inside without breaking user code
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A7 Class interfaces ===")
class RaceTime:
    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):                       # interface
        hours, minutes = self._diff_time()
        print(f"Time to complete race: {hours}:{minutes:02d}")

    def print_pace(self):                       # interface
        hours, minutes = self._diff_time()
        print(f"Avg pace (mins/mile): {(hours * 60 + minutes) / self.distance:.2f}")

    def _diff_time(self):                       # internal helper
        total = (self.end_hrs * 60 + self.end_mins) - (self.start_hrs * 60 + self.start_mins)
        return total // 60, total % 60

race = RaceTime(5, 30, 7, 0, 5.0)
race.print_time()
race.print_pace()

# ───────────────────────────────────────────────────────────────────────────
# A8 · CLASS CUSTOMIZATION                                              (9.8)
# • __str__(self) decides what print(obj) shows. It must RETURN a string
#   (not print it). Without __str__, print shows something ugly like
#   <__main__.Time object at 0x...> instead of a friendly description.
# • You can also teach your objects to use <, >, ==, etc. by adding special
#   methods. In each one, self is the LEFT side and other is the RIGHT side:
#       __lt__ is "<"   __gt__ is ">"   __eq__ is "=="   (also __le__ __ge__ __ne__)
#   Example: a < b runs a.__lt__(b).
# • If you don't add __eq__, then == only checks "are these the exact same
#   object?" - not whether their contents match.
# • Once you add __lt__ (how to compare two objects), sorted(), min() and
#   max() work on your objects automatically.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A8 Class customization ===")
print(time1)                                    # Time has no __str__

class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age

    def __str__(self):
        return f"{self.name} costs only ${self.price:.2f}. Not for children under {self.min_age}!"

print(Toy("Monster Truck XX", 14.99, 5))

class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours}:{self.minutes:02d}"

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        if self.hours == other.hours and self.minutes < other.minutes:
            return True
        return False

times = [Clock(10, 40), Clock(9, 15), Clock(12, 15)]
earliest = times[0]
for t in times:
    if t < earliest:                            # calls t.__lt__(earliest)
        earliest = t
print(f"Earliest time is {earliest}")
print(f"sorted: {[str(t) for t in sorted(times)]}")
print(f"{Clock(9, 15) == Clock(9, 15)=}   (no __eq__ -> different objects)")

# ───────────────────────────────────────────────────────────────────────────
# A9 · CLASSES AS NUMERIC TYPES                                         (9.9)
# • You can teach your objects to work with math symbols like + and -:
#       __add__ is "+"   __sub__ is "-"   __mul__ is "*"   __truediv__ is "/"
# • Each one takes (self, other): self is the left side, other is the right.
# • It should RETURN A NEW object (don't change self).
#   Example below: a Wallet you can add money to with +.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A9 Classes as numeric types ===")
class Wallet:
    def __init__(self, dollars):
        self.dollars = dollars

    def __str__(self):
        return f"${self.dollars}"

    def __add__(self, other):                   # runs when you write wallet + wallet
        return Wallet(self.dollars + other.dollars)   # give back a NEW Wallet

mine = Wallet(20)
yours = Wallet(5)
combined = mine + yours                          # calls mine.__add__(yours)
print(f"{mine} + {yours} = {combined}")          # $20 + $5 = $25
print(f"mine is unchanged: {mine}")              # still $20

# ───────────────────────────────────────────────────────────────────────────
# A10 · MEMORY ALLOCATION AND GARBAGE COLLECTION                       (9.10)
# • Every object you create takes up some memory. Python handles this for you
#   (unlike C/C++, you never ask for or free memory by hand).
# • Python keeps a simple count: "how many variables are pointing at this
#   object?" This is called the REFERENCE COUNT.
#       a = Tracked("A")   -> 1 variable points at it   (count = 1)
#       b = a              -> now 2 point at the SAME object (count = 2)
#       a = None           -> a let go, but b still holds it (count = 1)
#       b = None           -> nobody points at it  (count = 0)
# • When the count hits 0, nothing can reach the object anymore, so Python
#   throws it away and reuses the memory. This clean-up is called GARBAGE
#   COLLECTION. In the demo below, __del__ runs at that moment.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A10 Memory allocation and garbage collection ===")
class Tracked:
    def __init__(self, label):
        self.label = label
        print(f"allocated   {label}")

    def __del__(self):                          # runs when the object is freed
        print(f"deallocated {self.label}")

a = Tracked("A")            # A has 1 reference
b = a                       # A has 2 references
a = None                    # A has 1 reference (b) -> still alive
print("b still refers to A")
b = None                    # A has 0 references -> freed

# ───────────────────────────────────────────────────────────────────────────
# A11 · PUTTING PART A TOGETHER: BankAccount (version 1)
#   class attribute · constructor with a default · instance attributes ·
#   methods · __str__ · __lt__
# ───────────────────────────────────────────────────────────────────────────
print("\n=== A11 BankAccount v1 ===")
class BankAccount:
    bank_name = "Python Savings"                # class attribute: shared

    def __init__(self, owner, balance=0.0):     # constructor with a default
        self.owner = owner                      # instance attributes
        self.balance = balance

    def deposit(self, amount):                  # instance methods
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):                          # print(account)
        return f"{self.owner}: ${self.balance:.2f}"

    def __lt__(self, other):                    # <, sorted(), max()
        return self.balance < other.balance

ana = BankAccount("Ana", 50)
ben = BankAccount("Ben")
ana.deposit(25)
print(f"{ana} | {ben} | {BankAccount.bank_name}")
print(f"withdraw 100 -> {ana.withdraw(100)}, withdraw 30 -> {ana.withdraw(30)}, {ana}")
print(f"richest: {max([ana, ben]).owner}")
ben.deposit(-50)                                # accepted silently!
print(f"after ben.deposit(-50): {ben}   <- the class should refuse this (Part B)")

# Common mistakes
#   * Forgetting self:  def area():  or  hours = 0  inside __init__ (that is
#     a local variable, not an attribute - use self.hours = 0)
#   * Misspelling __init__ (e.g. __int__) -> constructor never runs:
#     Time(5) -> TypeError: Time() takes no arguments
#   * __str__ that prints instead of returning -> TypeError: __str__ returned
#     non-string (type NoneType)
#   * Expecting t2 = t1 to make a copy


# ═══════════════════════════════════════════════════════════════════════════
#
#                         PART B · EXCEPTIONS  (Ch. 10)
#
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# B1 · HANDLING EXCEPTIONS WITH try AND except                         (10.1)
# • Exception = an error that happens WHILE the program runs.
#   Not handled -> Python prints a traceback and the program STOPS.
# • Put code that might fail in a try block; except runs only if it fails.
# • When a line fails, the REST of the try block is skipped -> except runs
#   -> the program continues after the except block.
# • Common types: ValueError (bad value), ZeroDivisionError, KeyError
#   (missing dict key), IndexError (index out of range), EOFError (input()
#   found no input)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== B1 try and except ===")
def bmi_report(weight_text, height_text):          # in class: values from input()
    try:
        weight = int(weight_text)
        height = int(height_text)
        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi:.1f}")
    except:
        print("Could not calculate health info.")
    print("...program keeps running")

bmi_report("150", "66")
bmi_report("One-hundred fifty", "66")    # without try: ValueError -> program stops

print("Common exception types:")
# Each line below triggers a different built-in exception on purpose.
try:
    int("Ten")                       # text that is not a number
except ValueError as err:
    print(f"  int('Ten')            -> {type(err).__name__}")
try:
    10 / 0                           # dividing by zero
except ZeroDivisionError as err:
    print(f"  10 / 0                -> {type(err).__name__}")
try:
    {"Jose": "A+"}["Bob"]            # missing dictionary key
except KeyError as err:
    print(f"  grades['Bob']         -> {type(err).__name__}")
try:
    [1, 2, 3][5]                     # index past the end of a list
except IndexError as err:
    print(f"  [1, 2, 3][5]          -> {type(err).__name__}")

# ───────────────────────────────────────────────────────────────────────────
# B2 · MULTIPLE EXCEPTION HANDLERS                                     (10.2)
# • You can give one try several except blocks, one for each kind of error:
#       except ValueError:        -> handles bad values
#       except ZeroDivisionError: -> handles divide-by-zero
# • Want one block to cover a few types? Group them in parentheses:
#       except (TypeError, NameError):
# • Python checks the except blocks top to bottom and runs only the FIRST
#   one that matches. If none match, the program stops with that error.
# • A plain "except:" (no type) catches EVERYTHING. Use it rarely and put it
#   LAST - it can hide real bugs, like a misspelled variable name.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== B2 Multiple exception handlers ===")
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

for value in ["5", None]:
    try:
        total = value + 5                       # "5" + 5 and None + 5 -> TypeError
    except (TypeError, NameError):
        print(f"{value!r} + 5 -> handled TypeError")

# ───────────────────────────────────────────────────────────────────────────
# B3 · RAISING EXCEPTIONS + EXCEPTIONS WITH FUNCTIONS            (10.3, 10.4)
# • raise ValueError("Invalid weight.") creates and throws an exception NOW
# • except ValueError as excpt:  -> print(excpt) shows the message
# • A function that raises (and does not handle) exits immediately; the
#   exception goes back to the CALLER, whose try/except handles it
#   -> no need for special return values like -1 or False
# ───────────────────────────────────────────────────────────────────────────
print("\n=== B3 Raising exceptions; exceptions with functions ===")
def get_weight(text):
    weight = int(text)
    if weight < 0:
        raise ValueError("Invalid weight.")
    return weight                               # skipped if raise ran

def get_height(text):
    height = int(text)
    if height <= 0:
        raise ValueError("Invalid height.")
    return height

for w, h in [("150", "66"), ("-1", "66"), ("150", "-1")]:
    try:                                        # the caller handles both functions
        weight = get_weight(w)
        height = get_height(h)
        print(f"BMI: {(weight / (height * height)) * 703:.1f}")
    except ValueError as excpt:
        print(f"{excpt} Could not calculate health info.")
# ✗ raise "Invalid weight" -> TypeError: exceptions must derive from BaseException

# ───────────────────────────────────────────────────────────────────────────
# B4 · USING finally TO CLEAN UP                                       (10.5)
# • A "finally:" block is code that ALWAYS runs at the end of a try - whether
#   things went fine, hit an error, or that error was handled. It comes last.
# • Think of it as "no matter what happens above, do this on the way out."
# • It's meant for CLEAN-UP: things you must do regardless of success or
#   failure, like closing a file or a network connection you opened.
# • It even runs when try or except does a "return" - Python does the finally
#   block first, THEN actually returns.
#     Example: try to divide; if it fails, print a message; EITHER way, finally
#     prints the result so you always see an ending line.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== B4 finally ===")
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

# ───────────────────────────────────────────────────────────────────────────
# B5 · CUSTOM EXCEPTION TYPES                                          (10.6)
# • An exception is an OBJECT of a CLASS (Part A!). Make your own type by
#   inheriting from Exception (the parentheses name the parent class):
#       class InsufficientFundsError(Exception):
#           pass
# • End the name with "Error"; callers can then catch exactly your problem
# ───────────────────────────────────────────────────────────────────────────
print("\n=== B5 Custom exception types ===")
class InsufficientFundsError(Exception):
    pass

try:
    raise InsufficientFundsError("need $30.00 more")
except InsufficientFundsError as excpt:
    print(f"{type(excpt).__name__}: {excpt}")
    print(f"{isinstance(excpt, Exception)=}")

# ───────────────────────────────────────────────────────────────────────────
# B6 BankAccount (version 2) RAISES instead of returning False
#   deposit/withdraw raise ValueError for bad amounts and
#   InsufficientFundsError for overdrafts; the CALLER decides what to do.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== B6 BankAccount v2 ===")
class BankAccount:
    bank_name = "Python Savings"

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"deposit must be positive, got {amount}")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"withdrawal must be positive, got {amount}")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"{self.owner} needs ${amount - self.balance:.2f} more")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance:.2f}"

    def __lt__(self, other):
        return self.balance < other.balance

ben = BankAccount("Ben", 100)
for action, amount in [("deposit", 50), ("deposit", -50), ("withdraw", 500), ("withdraw", 20)]:
    try:
        if action == "deposit":
            ben.deposit(amount)
        else:
            ben.withdraw(amount)
        print(f"OK      {action} {amount}")
    except InsufficientFundsError as excpt:
        print(f"DENIED  {excpt}")
    except ValueError as excpt:
        print(f"ERROR   {excpt}")
    finally:
        print(f"        balance -> {ben}")


# Common mistakes
#   * Bare except: everywhere -> hides real bugs (typos, NameError)
#   * A broad handler (except Exception) before a specific one
#   * raise "text" instead of raise ValueError("text")
#   * Using a variable after except whose assignment was skipped


# ═══════════════════════════════════════════════════════════════════════════
#
#                           PART C · MODULES  (Ch. 11)
#
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# C1 · MODULES AND import                                              (11.1)
# • A SCRIPT is a .py file you RUN directly:  python report.py
#   A MODULE is a .py file whose code you want to REUSE. Instead of running
#   it, another file "imports" it to borrow its functions and classes.
#   Write useful code once, then import it wherever you need it.
# • To use a module, write:  import fractions
#   (just the file name "fractions", no ".py", and the spelling must match
#   exactly - Fractions would not work.)
# • What Python does the first time you  import fractions :
#     - it finds and runs the fractions file once, then remembers it, so
#       importing it again later does nothing (the code won't run twice).
# • After importing, reach inside it with a dot:  fractions.Fraction(1, 2)
#   (module name, then a dot, then the thing you want).
# • Put your imports at the TOP of the file. A module your program relies on
#   is called a DEPENDENCY.
#
#   A module is just a .py file. If our BankAccount (Parts A & B) lived in a
#   file called bank.py, we would write  import bank  and then use
#   bank.BankAccount("Cy", 10). Below we use Python's built-in "fractions"
#   module to show how importing works, so there's nothing extra to install.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C1 Modules and import ===")
print(f"{'fractions' in sys.modules=}")         # False: not loaded yet
import fractions                                # 1st import: runs + caches it
import fractions                                # 2nd import: nothing runs again
print(f"{'fractions' in sys.modules=}")         # True: loaded exactly once
half = fractions.Fraction(1, 2)                 # dot notation reaches its names
print(f"{half + fractions.Fraction(1, 3)=}")

# Import errors are exceptions too (Part B):
try:
    import bank                                 # no bank.py here -> fails
except ModuleNotFoundError as err:
    print(f"import bank -> ModuleNotFoundError: {err}")

# ───────────────────────────────────────────────────────────────────────────
# C2 · FINDING MODULES                                                 (11.2)
# • Search order for  import x :
#     1. BUILT-IN modules (compiled into Python: sys, time, ...)
#     2. the folders in sys.path (a plain list), in order:
#          a. the folder of the executing script
#          b. folders in the environment variable PYTHONPATH
#               Windows:      set PYTHONPATH=c:\dir1;c:\other\directory
#               macOS/Linux:  export PYTHONPATH=/dir1:/other/directory
#          c. the folder where Python is installed
#   First match wins. Nothing found -> ModuleNotFoundError.
# • NEVER name your file like an existing module (random.py, math.py ...):
#   yours is found in the script folder FIRST and hides the real one.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C2 Finding modules ===")
print(f"{'sys' in sys.builtin_module_names=}  {'fractions' in sys.builtin_module_names=}")
print(f"{sys.path[0]=}   <- the running script's folder, searched first")
print(f"{fractions.__file__=}   <- where Python found the module")

# ───────────────────────────────────────────────────────────────────────────
# C3 · from ... import ...   AND   import ... as ...                   (11.3)
# • import math                      -> one name, math; use math.sqrt
# • from math import sqrt            -> copies only that name; use sqrt
#                                       (the name math is NOT created)
# • import math as m                 -> import math but call it m
# • from module import *             -> copies ALL names; interpreter only
# • A from-import silently REPLACES a name you already had.
#   (If BankAccount lived in bank.py you would write
#    `from bank import BankAccount, InsufficientFundsError` to use them by
#    their short names - exactly the names we already defined in Part B.)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C3 from ... import ... / import ... as ... ===")
import math
from math import sqrt                           # copies just sqrt
import math as m                                # alias for the module
print(f"{sqrt(16)=}  {m.pi=}  {math.factorial(5)=}")
print(f"{m is math=}  (import ... as makes an alias, not a copy)")

# ───────────────────────────────────────────────────────────────────────────
# C4 · EXECUTING MODULES AS SCRIPTS: __name__                          (11.4)
# • The problem: importing a file RUNS everything in it. So if a file prints
#   something or asks for input at the top level, that happens the moment you
#   import it - usually not what you want. You wanted its functions, not its
#   test code.
# • Python's clue: every file has a built-in variable called __name__ that
#   tells the file HOW it was started:
#       - run directly (python bank.py)  ->  __name__ is "__main__"
#       - imported by another file       ->  __name__ is the file's name ("bank")
# • The fix: wrap your test code in an "if" that checks for that clue:
#       if __name__ == "__main__":
#           ...test code goes here...
#   This code runs only when the file is RUN directly, and is SKIPPED when the
#   file is imported. Keep your functions and classes OUTSIDE the if, so other
#   files can still import and use them.
#
#   # bank.py would end like this:
#   #     if __name__ == "__main__":        # runs only with:  python bank.py
#   #         test = BankAccount("Test", 100)
#   #         test.withdraw(30)
#   #         print(test)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C4 __name__ and the main guard ===")
print(f"{__name__=}   <- this file is being run directly")
print(f"{math.__name__=}   <- imported, so its name is the module name")
print("A main guard keeps a module's test code from running on import.")

# ───────────────────────────────────────────────────────────────────────────
# C5 · PACKAGES                                                        (11.6)
# • PACKAGE = a folder of related modules, marked by a file __init__.py
#   (often empty). Subpackage = a package inside a package. Dots follow the
#   folders:   urllib/                     (a real standard-library package)
#                __init__.py
#                parse.py   -> def quote(text), def urlparse(text), ...
# • Three ways to import, all shown below:
#     import urllib.parse               -> urllib.parse.quote("a b")
#     from urllib import parse          -> parse.quote("a b")
#     from urllib.parse import quote    -> quote("a b")
# • import a.b.c -> c must be a package or MODULE (not a function).
#   (A package of your own, e.g. school/grades.py, imports the same way:
#    import school.grades  /  from school import grades  /
#    from school.grades import letter.)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C5 Packages ===")
import urllib.parse
from urllib import parse
from urllib.parse import quote
print(f"{urllib.parse.quote('a b')=}")
print(f"{parse.quote('x/y')=}  {quote('p q')=}")

# ───────────────────────────────────────────────────────────────────────────
# C6 · THE STANDARD LIBRARY                                            (11.7)
# • Modules that come WITH Python - just import them. Check here before
#   writing code yourself:  https://docs.python.org/3/library/
#     math  random  datetime  time  copy  os  sys  urllib  pdb ...
# • This file uses several: os, sys, csv, struct, math, fractions, urllib.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C6 Standard library ===")
import datetime
import random
random.seed(1)                  # same "random" numbers every run
print(f"{random.randint(1, 6)=}  {datetime.date(2026, 12, 25).strftime('%A')=}")

# Common mistakes
#   * import bank.py  /  import Bank   (wrong name or extension)
#   * Test code without the main guard -> runs on every import
#   * Classes/defs placed INSIDE the guard -> importers can't use them
#   * Naming files math.py, random.py, csv.py ...


# ═══════════════════════════════════════════════════════════════════════════
#
#                        PART D · FILES  (File I/O)
#
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# D1 · OPENING AND WRITING FILES; FILE MODES
# • To work with a file you first OPEN it, then when you're done you CLOSE it:
#       file = open("myfile.txt", "w")   # open it
#       ...                              # read or write
#       file.close()                     # close it
#   Just a name ("myfile.txt") means "in the same folder as the program"; you
#   can also give a full path to a file anywhere on the computer.
# • The second argument is the MODE - it says what you plan to do:
#       "r"  READ     - look at an existing file (error if it doesn't exist)
#       "w"  WRITE    - make a new file; if it already exists, ERASE it first
#       "a"  APPEND   - add to the END of a file (keeps what's already there)
#   (Add "b" for non-text files like images: "rb", "wb".)
# • WARNING: "w" wipes the file the moment you open it. Use "a" when you want
#   to keep the old contents and add more.
# • file.write(text) writes a STRING. Two things to remember:
#       - numbers must be turned into text first:  file.write(str(5.75))
#       - it does NOT add line breaks - put "\n" yourself to start a new line.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D1 Writing files and modes ===")
file = open("myfile.txt", "w")                  # "w": create / OVERWRITE
file.write("Gotham is quiet tonight.\n")
file.write("The signal is on.\n")
file.close()

file = open("myfile.txt", "a")                  # "a": add to the end
file.write("Time to go.\n")
file.close()

file = open("numbers.txt", "w")
for n in [10, 20.5, 30]:
    file.write(str(n) + "\n")                   # numbers -> str first
file.close()
# file.write(5.75) -> TypeError: write() argument must be str, not float

# ───────────────────────────────────────────────────────────────────────────
# D2 · READING FILES
#     file.read()       -> whole file as ONE string   (read(n): n characters)
#     file.readlines()  -> LIST of strings, one per line
#     file.readline()   -> ONE line per call; returns "" at EOF (end of file)
#     for line in file: -> one line at a time (memory-friendly)
# • Lines keep their "\n" -> use .strip()
# • Typical workflow: read -> iterate over lines -> compute a result
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D2 Reading files ===")
file = open("myfile.txt")                       # default mode "r"
print(f"{file.read()=}")
print(f"{file.read()=}")                        # already at EOF -> ''
file.close()

file = open("myfile.txt")
print(f"{file.readlines()=}")
file.close()

file = open("myfile.txt")
print(f"{file.readline()=}")
print(f"{file.readline()=}")
file.close()

file = open("numbers.txt")
total = 0
count = 0
for line in file:
    total += float(line)                        # float() ignores the "\n"
    count += 1
file.close()
print(f"Count = {count}, Total = {total}, Average = {total / count:.2f}")

# ───────────────────────────────────────────────────────────────────────────
# D3 · THE with STATEMENT (best practice)
# • with open(...) as f:  closes the file automatically at the end of the
#   block - even if an exception occurs (like try/finally in B4, built in)
# • Several files at once:  with open(a) as f1, open(b, "w") as f2:
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D3 with ===")
with open("myfile.txt") as myfile:
    contents = myfile.read()
    print(f"inside:  {myfile.closed=}")
print(f"outside: {myfile.closed=}")

with open("myfile.txt") as infile, open("upper.txt", "w") as outfile:
    outfile.write(infile.read().upper())
with open("upper.txt") as f:
    print(f.read(), end="")

# ───────────────────────────────────────────────────────────────────────────
# D4 · THE os MODULE: PATHS AND FOLDERS
# The "os" module lets your program work with files and folders the way you
# would in a file explorer: check what exists, make folders, list contents.
# • Building a path: different systems separate folders differently
#   (Windows uses "\", Mac/Linux use "/"). Don't hardcode either one - let
#   Python pick the right one for you:
#       os.path.join("subdir", "bat_mobile.jpg")   -> "subdir/bat_mobile.jpg"
# • Asking questions about a path:
#       os.path.exists(p)  - does it exist at all?
#       os.path.isfile(p)  - is it a file?       os.path.isdir(p) - a folder?
#       os.path.getsize(p) - how many bytes?     os.path.basename(p) - just the name
# • Doing things with folders/files:
#       os.getcwd()     - the folder we're currently working in
#       os.listdir(p)   - names of everything inside folder p
#       os.makedirs(p)  - create a folder (and any missing parent folders)
#       os.remove(p)    - delete a file     os.rmdir(p) - delete an empty folder
# • Exploring a whole folder tree: os.walk(top) visits every folder under
#   "top" and hands you, for each one, its name, its subfolders, and its files.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D4 os module ===")
# Build a tiny folder tree so os.walk has something to explore.
os.makedirs(os.path.join("school", "math"), exist_ok=True)
with open(os.path.join("school", "roster.txt"), "w") as f:
    f.write("Ann\nBo\n")
with open(os.path.join("school", "math", "grades.txt"), "w") as f:
    f.write("A\nB\n")

path = os.path.join("subdir", "bat_mobile.jpg")
print(f"{path=}  {os.path.sep=}")
print(f"{os.path.exists('myfile.txt')=}  {os.path.isdir('school')=}")
print(f"{os.path.getsize('myfile.txt')=}  {os.path.splitext('report.final.pdf')=}")
for dirname, subdirs, files in os.walk("school"):
    print(f"Directory: {dirname}  Subdirs: {sorted(subdirs)}  Files: {sorted(files)}")

# ───────────────────────────────────────────────────────────────────────────
# D5 · CSV FILES: SAVING OBJECTS
# • CSV = comma-separated values: each line is a row, commas separate the
#   fields; the first row is often a header.
# • csv.reader(file) -> each row is a LIST OF STRINGS; next(reader) skips
#   the header; convert with int()/float() before doing math
# • csv.writer(file).writerow(list) / writerows(list_of_lists)
#   open with newline="" when writing (avoids blank lines on Windows)
# • Fields containing commas are quoted automatically: "Wayne, Bruce"
# • Objects -> rows: write each object's ATTRIBUTES (Part A)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D5 CSV files ===")
def save_accounts(accounts, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["owner", "balance"])
        for account in accounts:
            writer.writerow([account.owner, account.balance])

accounts = [BankAccount("Ana", 45.0), BankAccount("Ben", 130.0),
            BankAccount("Wayne, Bruce", 1000000.0)]
save_accounts(accounts, "accounts.csv")
with open("accounts.csv") as f:
    print(f.read(), end="")

with open("accounts.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"{header=}")
    for row in reader:
        print(f"{row=}  -> balance as number: {float(row[1])}")

# ───────────────────────────────────────────────────────────────────────────
# D6 · FILES + EXCEPTIONS
# • Missing file -> FileNotFoundError (a kind of OSError; IOError is another
#   name for OSError). Bad text -> ValueError when converting.
# • Classic version (10.5): try / except / finally closes the file.
# • Modern version: with closes the file; try/except handles the errors.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D6 Files + exceptions ===")
with open("good.txt", "w") as f:
    f.write("5\n423\n234\n")
with open("letters.txt", "w") as f:
    f.write("five\n")

for file_name in ["good.txt", "letters.txt", "missing.txt"]:      # 10.5 version
    nums = []
    rd_nums = None
    try:
        rd_nums = open(file_name, "r")
        for line in rd_nums:
            nums.append(int(line))
    except IOError:
        print(f"Could not find {file_name}")
    except ValueError:
        print(f"Could not read number from {file_name}")
    finally:
        if rd_nums != None:
            rd_nums.close()
    print(f"  {file_name}: numbers found {nums}")

def load_accounts(filename):                                       # with version
    accounts = []
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            next(reader)                                           # skip header
            for row in reader:
                try:
                    accounts.append(BankAccount(row[0], float(row[1])))
                except (IndexError, ValueError):
                    print(f"  skipped bad row: {row}")
    except FileNotFoundError:
        print(f"  {filename} not found -> starting with no accounts")
    return accounts

with open("messy.csv", "w") as f:
    f.write("owner,balance\nCy,10\nDan,lots\nEve\n")
print([str(a) for a in load_accounts("messy.csv")])
print([str(a) for a in load_accounts("missing.csv")])

# ───────────────────────────────────────────────────────────────────────────
# D7 · QUICK LOOK: BINARY FILES, struct, sys.argv
# This is a quick preview of three "good to know" topics.
#
# • BINARY FILES: text files hold readable characters. But files like images,
#   PDFs, and music hold raw BYTES (plain numbers), not letters. To work with
#   those, add "b" to the mode: "rb" to read, "wb" to write. Now reading gives
#   you bytes, and writing expects bytes. A bytes value looks like b"abc".
#
# • struct: a helper for turning numbers into bytes and back, so you can save
#   them in a binary file.
#       struct.pack(...)   takes numbers -> gives you bytes (to write)
#       struct.unpack(...) takes bytes   -> gives back the numbers (as a tuple)
#   The first argument is a short "format" string describing the pieces (e.g.
#   how many numbers and how big each is). Don't memorize the codes - just know
#   pack = numbers into bytes, unpack = bytes back into numbers.
#
# • sys.argv: the list of words typed after your program's name on the command
#   line, so a program can take input without asking with input(). They're all
#   strings. sys.argv[0] is the program's own name; extras follow:
#       python myscript.py myfile1.txt   ->   sys.argv[1] is "myfile1.txt"
# ───────────────────────────────────────────────────────────────────────────
print("\n=== D7 Binary files, struct, sys.argv ===")
with open("record.bin", "wb") as f:
    f.write(struct.pack("<hh4s", 100, 200, b"text"))
with open("record.bin", "rb") as f:
    raw = f.read()
print(f"{raw=}  {type(raw)=}")
print(f"{struct.unpack('<hh4s', raw)=}")
print(f"{sys.argv=}")


# Common mistakes
#   * "w" when you meant "a" -> data lost      * math on CSV strings
#   * forgetting "\n" / .strip()               * forgetting to skip the header
#   * hardcoded "\\" or "/" in paths -> use os.path.join


# ═══════════════════════════════════════════════════════════════════════════
#
#                  PART E · PUTTING IT ALL TOGETHER
#
#   CLASS (A)      BankAccount objects with methods, __str__, __lt__
#   EXCEPTIONS (B) ValueError, KeyError, custom InsufficientFundsError
#   MODULE (C)     import mechanics covered in Part C; the class would live
#                  in bank.py (here it is the version defined in Part B)
#   FILES (D)      accounts loaded from and saved to accounts.csv
# ═══════════════════════════════════════════════════════════════════════════
print("\n=== E Putting it all together ===")
# BankAccount and InsufficientFundsError come from Part B. If they lived in
# bank.py you would write:  from bank import BankAccount, InsufficientFundsError

accounts = load_accounts("accounts.csv")                    # (D) + (B)
by_owner = {account.owner: account for account in accounts}
transactions = [("Ana", "withdraw", "20"), ("Ben", "withdraw", "500"),
                ("Ben", "deposit", "abc"), ("Zoe", "deposit", "10"),
                ("Ana", "deposit", "-5"), ("Ben", "deposit", "70")]

for owner, action, amount_text in transactions:
    try:
        account = by_owner[owner]                           # KeyError
        amount = float(amount_text)                         # ValueError
        if action == "deposit":
            account.deposit(amount)                         # ValueError
        else:
            account.withdraw(amount)                        # InsufficientFundsError
        print(f"OK      {owner} {action} {amount:.2f} -> {account}")
    except KeyError:
        print(f"ERROR   no account for {owner}")
    except InsufficientFundsError as excpt:
        print(f"DENIED  {excpt}")
    except ValueError as excpt:
        print(f"ERROR   {owner}: {excpt}")

save_accounts(accounts, "accounts.csv")                     # (D)
print("Report (highest balance first):")
for account in sorted(accounts, reverse=True):              # uses __lt__ (A)
    print(f"  {account}")

# ═══════════════════════════════════════════════════════════════════════════
# RECAP
# ═══════════════════════════════════════════════════════════════════════════
# CLASSES     class Name:  def __init__(self, a, b=0): self.a = a  (attribute)
#             obj = Name(1)   obj.a   obj.method()  == Name.method(obj)
#             class attribute: shared · instance attribute: one per object
#             _helper = internal (convention) · __str__ for print()
#             __lt__ __eq__ ... for comparisons · __add__ __sub__ ... for math
#             t2 = t1 -> same object · refcount 0 -> garbage collected
# EXCEPTIONS  try: ... except ValueError as e: ... finally: (always runs)
#             first matching handler wins · raise ValueError("msg")
#             class MyError(Exception): pass   -> custom type
# MODULES     import m -> m.name · from m import a · import m as x
#             code runs ONCE (sys.modules) · search: built-ins -> sys.path
#             if __name__ == "__main__":  (only when run as a script)
#             package = folder + __init__.py · standard library
# FILES       with open(p, "r"/"w"/"a"/"rb"/"wb") as f:   (auto-close)
#             f.read() f.readline() f.readlines() for line in f · f.write(str)
#             os.path.join/exists/getsize · os.walk · csv.reader / csv.writer
#             FileNotFoundError, ValueError -> handle with try/except
# ═══════════════════════════════════════════════════════════════════════════
