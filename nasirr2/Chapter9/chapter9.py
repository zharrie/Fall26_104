"""
CHAPTER 9 · CLASSES
"""

# ═══════════════════════════════════════════════════════════════════════════
# 9.1 CLASSES: INTRODUCTION
# • Object = data (variables) + the operations on that data (methods)
# • People think in objects (chair, drawer), not materials (wood, metal).
#   Programs too: a Restaurant object, not loose variables and functions.
# • Abstraction / information hiding / encapsulation: use the oven's knob,
#   don't reach inside to adjust the flame.
# • ADT (abstract data type) = a type used only through well-defined operations.
#   A class is how Python implements an ADT.
# • You already use built-in objects: str and int hold a value + useful methods.
# ═══════════════════════════════════════════════════════════════════════════

s1 = "Hello!!"
i1 = 130
print(f"{type(s1)=}  {s1.isdigit()=}  {s1.lower()=}")
print(f"{type(i1)=}  {abs(-i1)=}  {float(i1)=}")

# ═══════════════════════════════════════════════════════════════════════════
# 9.2 CLASSES: GROUPING DATA
# • class Time:  creates a new type (class names use CapWords)
# • __init__ is the CONSTRUCTOR: it runs automatically when you call Time()
# • self = the new object being built;  self.hours = 0 creates an ATTRIBUTE
# • my_time = Time()  creates an INSTANCE;  my_time.hours uses dot notation
# • Each instance has its own values.  t2 = t1 does NOT copy — same object.
# ═══════════════════════════════════════════════════════════════════════════

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
print(f"time1 = {time1.hours}:{time1.minutes}   time2 = {time2.hours}:{time2.minutes}")

same = time1                       # another name for time1
same.hours = 9
print(f"{time1.hours=}  (changed through 'same')")

# ═══════════════════════════════════════════════════════════════════════════
# 9.3 INSTANCE METHODS
# • A method is a function inside a class. Its first parameter is always self.
# • Call it with obj.method() — Python passes obj as self automatically.
# • Use self.attribute inside the method to reach the object's data.
# • Names like __init__ are special ("dunder") methods; don't invent new ones.
# ═══════════════════════════════════════════════════════════════════════════

class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):
        return self.wage * self.hours_worked

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f"Alice's net pay: {alice.calculate_pay():.2f}")
# ✗ def calculate_pay():   (no self) → TypeError: takes 0 positional arguments but 1 was given

# ═══════════════════════════════════════════════════════════════════════════
# 9.4 CLASS AND INSTANCE OBJECT TYPES
# • Class attribute: defined in the class body → SHARED by every instance
# • Instance attribute: self.x = ... → belongs to ONE instance
# • Lookup order: the instance first, then the class
# • Same name in both → the instance's hides the class's (avoid this)
# ═══════════════════════════════════════════════════════════════════════════

class MarathonRunner:
    race_distance = 42.195         # class attribute (km), shared

    def __init__(self, speed):
        self.speed = speed         # instance attribute, one per runner

runner1 = MarathonRunner(7.5)
runner2 = MarathonRunner(8.0)
print(f"{runner1.speed=}  {runner2.speed=}  {runner2.race_distance=}")

MarathonRunner.race_distance = 26.2          # change the class attribute...
print(f"{runner1.race_distance=}  {runner2.race_distance=}")   # ...everyone sees it

runner1.race_distance = 10.0                 # creates an attribute on runner1 only
print(f"{runner1.race_distance=}  {runner2.race_distance=}")

# ═══════════════════════════════════════════════════════════════════════════
# 9.5 CLASS EXAMPLE: SEAT RESERVATION SYSTEM
# • Each Seat keeps its own data AND its operations together
# • A list of objects models the whole plane; the main code reads like the problem
# ═══════════════════════════════════════════════════════════════════════════

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

# ═══════════════════════════════════════════════════════════════════════════
# 9.6 CLASS CONSTRUCTORS
# • __init__ can take parameters → set attributes when the object is created
# • Parameters can have defaults: def __init__(self, name, wage=8.25, hours=20)
# • Required parameters first; defaulted ones can be passed by name
# ═══════════════════════════════════════════════════════════════════════════

class Worker:
    def __init__(self, name, wage=8.25, hours=20):
        self.name = name
        self.wage = wage
        self.hours = hours

todd = Worker("Todd")                          # uses the defaults
tricia = Worker("Tricia", wage=12.50, hours=40)
for w in [todd, tricia]:
    print(f"{w.name} earns {w.wage * w.hours:.2f} per week")
# Worker()  → TypeError: missing 1 required positional argument: 'name'

# ═══════════════════════════════════════════════════════════════════════════
# 9.7 CLASS INTERFACES
# • Interface = the methods a user is meant to call
# • Implementation = the internal details (attributes, helper methods)
# • A leading underscore (_diff_time) means "internal" — a convention only;
#   Python does not block it
# • Hiding details lets you change the inside without breaking user code
# ═══════════════════════════════════════════════════════════════════════════

class RaceTime:
    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):                      # interface
        hours, minutes = self._diff_time()
        print(f"Time to complete race: {hours}:{minutes:02d}")

    def print_pace(self):                      # interface
        hours, minutes = self._diff_time()
        print(f"Avg pace (mins/mile): {(hours * 60 + minutes) / self.distance:.2f}")

    def _diff_time(self):                      # internal helper
        total = (self.end_hrs * 60 + self.end_mins) - (self.start_hrs * 60 + self.start_mins)
        return total // 60, total % 60

race = RaceTime(5, 30, 7, 0, 5.0)
race.print_time()
race.print_pace()

# ═══════════════════════════════════════════════════════════════════════════
# 9.8 CLASS CUSTOMIZATION
# • __str__(self) → used by print(obj); must RETURN a string
#   (without it you see <__main__.Toy object at 0x...>)
# • Rich comparisons (operator overloading): self = left side, other = right side
#   __lt__ <   __le__ <=   __gt__ >   __ge__ >=   __eq__ ==   __ne__ !=
# ═══════════════════════════════════════════════════════════════════════════

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
    if t < earliest:                           # calls t.__lt__(earliest)
        earliest = t
print(f"Earliest time is {earliest}")
print(f"Clock(9, 15) < Clock(9, 30) → {Clock(9, 15) < Clock(9, 30)}")

# ═══════════════════════════════════════════════════════════════════════════
# 9.9 CLASSES AS NUMERIC TYPES
# • __add__ +   __sub__ -   __mul__ *   __truediv__ /   __floordiv__ //
#   __mod__ %   __pow__ **   __abs__ abs()   __int__ int()   __float__ float()
# • Return a NEW object (or an int/float for __int__/__float__)
# • isinstance(other, int) lets one method handle different right-hand types
# ═══════════════════════════════════════════════════════════════════════════

class Time24:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __sub__(self, other):
        if isinstance(other, int):                     # time - 5 → 5 hours earlier
            return Time24(self.hours - other, self.minutes)
        if isinstance(other, Time24):                  # time - time → difference
            total = abs((self.hours * 60 + self.minutes) - (other.hours * 60 + other.minutes))
            return Time24(total // 60, total % 60)
        raise NotImplementedError

    def __float__(self):
        return self.hours + self.minutes / 60

t1 = Time24(10, 15)
print(f"t1 - Time24(8, 0) = {t1 - Time24(8, 0)}")
print(f"t1 - 5            = {t1 - 5}")
print(f"float(t1)         = {float(t1)}")

# ═══════════════════════════════════════════════════════════════════════════
# 9.10 MEMORY ALLOCATION AND GARBAGE COLLECTION
# • Allocation: the Python runtime asks the operating system for memory for you
# • Reference count = how many variables refer to an object
# • When the count reaches 0, the GARBAGE COLLECTOR can free (deallocate) it
#   (exactly when depends on the Python implementation; CPython does it right away)
# ═══════════════════════════════════════════════════════════════════════════

class Tracked:
    def __init__(self, label):
        self.label = label
        print(f"allocated   {label}")

    def __del__(self):                          # runs when the object is freed
        print(f"deallocated {self.label}")

a = Tracked("A")           # A has 1 reference
b = a                      # A has 2 references
a = None                   # A has 1 reference (b) → still alive
print("b still refers to A")
b = None                   # A has 0 references → freed

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICE
# ═══════════════════════════════════════════════════════════════════════════


# 1. BankAccount: deposit, withdraw (refuse overdrafts), and __str__.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    pass

acct = BankAccount("Ana", 50)
acct.deposit(25)
print(f"1. withdraw 100 → {acct.withdraw(100)}, withdraw 30 → {acct.withdraw(30)}, {acct}")

# 2. Rectangle with area(), perimeter(), is_square().
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        pass

    def perimeter(self):
        pass

    def is_square(self):
        pass

box = Rectangle(3, 4)
print(f"2. area={box.area()}  perimeter={box.perimeter()}  square={box.is_square()}")

# 3. A class attribute that counts how many tickets were created.
class Ticket:
    pass

Ticket("A1"), Ticket("A2"), Ticket("B7")
print(f"3. Tickets created: {Ticket.count}")

# 4. Point that supports + and prints nicely.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        pass

    def __str__(self):
        pass

print(f"4. {Point(1, 2) + Point(3, 4)}")

# 5. __lt__ lets sorted() and max() work on a list of Student objects.
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        pass

roster = [Student("Ann", 3.2), Student("Bo", 3.9), Student("Cy", 2.8)]
print(f"5. lowest → highest: {[s.name for s in sorted(roster)]}   top: {max(roster).name}")
