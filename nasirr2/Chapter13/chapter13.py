"""
=====================================================================
 LECTURE: Classes & Inheritance
=====================================================================
"""
# =====================================================================
# PART 1 - CLASSES (review)
# =====================================================================
#   - A class is a BLUEPRINT; an object (instance) is built from it.
#   - __init__()  -> constructor, runs automatically on creation
#   - self        -> the instance itself (passed automatically)
#   - Instance attributes store data; methods operate on that data.
#   - Why classes? organize | reuse | model real world | extend (inheritance)

class Item:
    def __init__(self):
        self.name = ""
        self.quantity = 0

    def set_name(self, name):
        self.name = name

    def set_quantity(self, quantity):
        self.quantity = quantity

    def display(self):
        print(f"Item: {self.name}, Quantity: {self.quantity}")

item1 = Item()                      # create an instance
item1.set_name("Smith Cereal")
item1.set_quantity(9)
item1.display()                     # Item: Smith Cereal, Quantity: 9


# =====================================================================
# PART 2 - INHERITANCE
# =====================================================================
#   - A DERIVED class (subclass) is built from a BASE class (superclass).
#   - Syntax:  class Produce(Item):   <- base class in parentheses
#   - The derived class gets ALL base methods, and can ADD its own.
#   - Methods are inherited automatically, but INSTANCE attributes are
#     only created if you call the base constructor:
#         Item.__init__(self)
#
#   Board:        Item  (name, quantity, set_name, set_quantity, display)
#                   ^
#                Produce (+ expiration, set_expiration, get_expiration)

class Produce(Item):                # Produce inherits from Item
    def __init__(self):
        Item.__init__(self)         # creates name and quantity
        self.expiration = ""        # new attribute

    def set_expiration(self, expiration):
        self.expiration = expiration

    def get_expiration(self):
        return self.expiration

item2 = Produce()
item2.set_name("Apples")            # from Item
item2.set_quantity(40)              # from Item
item2.set_expiration("May 5, 2012") # from Produce
item2.display()                     # Item: Apples, Quantity: 40
print(f"Expires: {item2.get_expiration()}")

# What happens on  Produce()  :
#   1. Produce.__init__(self) is called
#   2. It calls Item.__init__(self)
#   3. Item's constructor creates name and quantity
#   4. Control returns to Produce.__init__()
#   5. expiration is created
#
# Terminology
#   Base class / superclass   -> the class inherited FROM   (Item)
#   Derived class / subclass  -> the class that inherits    (Produce)
#   Inheritance tree          -> hierarchy from derived up to base
#   Any class can be a base class - no special changes needed.

class BadProduce(Item):
    def __init__(self):             # forgot Item.__init__(self)
        self.expiration = ""

bad = BadProduce()
bad.set_name("Pears")               # works: methods ARE inherited
try:
    bad.display()                   # fails: quantity was never created
except AttributeError as e:
    print("AttributeError:", e)
# AttributeError - 'BadProduce' object has no attribute 'quantity'

# Common mistakes
#   - Forgetting Item.__init__(self) in the derived constructor
#   - Writing Item.__init__() without self
#   - Expecting a base-class object to have derived methods
#     (Item() has NO set_expiration - inheritance goes one way, down)


# =====================================================================
# PART 3 - ADVANCED CONCEPTS
# =====================================================================

# ---------------------------------------------------------------------
# 3.1 Attribute lookup - how Python finds  obj.something
# ---------------------------------------------------------------------
# Search order:
#   1. Instance namespace   (instance attributes)
#   2. Class namespace      (methods / class attributes)
#   3. Base classes         (recursively up the tree)
#   Not found anywhere -> AttributeError

class TransportMode:
    def move(self):
        print("Moving...")

class MotorVehicle(TransportMode):
    def start_engine(self):
        print("Engine started")

class Motorcycle(MotorVehicle):
    def wheelie(self):
        print("Doing a wheelie!")

bike = Motorcycle()
bike.wheelie()                      # found in Motorcycle
bike.start_engine()                 # found in MotorVehicle
bike.move()                         # found in TransportMode (top)


# ---------------------------------------------------------------------
# 3.2 Overriding - same method name in the derived class REPLACES it
# ---------------------------------------------------------------------

class Produce(Item):
    def __init__(self):
        Item.__init__(self)
        self.expiration = ""

    def display(self):              # overrides Item.display()
        print(f"Produce: {self.name}, Quantity: {self.quantity}, "
              f"Expires: {self.expiration}")

item1 = Item()
item1.name, item1.quantity = "Cereal", 10
item1.display()                     # Item: Cereal, Quantity: 10

item2 = Produce()
item2.name, item2.quantity, item2.expiration = "Bananas", 25, "June 1, 2023"
item2.display()                     # Produce: Bananas, Quantity: 25, Expires: June 1, 2023
# Why? Lookup finds display() in Produce FIRST and stops searching.


# ---------------------------------------------------------------------
# 3.3 Extending - call the base method, THEN add behavior
# ---------------------------------------------------------------------
print("\n--- 3.3 Extending ---")

class Produce(Item):
    def __init__(self):
        Item.__init__(self)
        self.expiration = ""

    def display(self):
        Item.display(self)          # reuse base logic
        print(f"Expiration: {self.expiration}")   # add new behavior

item2 = Produce()
item2.name, item2.quantity, item2.expiration = "Strawberries", 15, "April 20, 2023"
item2.display()
# Item: Strawberries, Quantity: 15
# Expiration: April 20, 2023

# Common mistakes
#   - Calling self.display() inside display() -> infinite recursion!
#     Use Item.display(self) to reach the base version.
#   - Override vs extend: override = replace, extend = base + extra


# ---------------------------------------------------------------------
# 3.4 Inheritance vs Composition  (is-a vs has-a)
# ---------------------------------------------------------------------
#   "X IS A Y"   -> inheritance   Produce is an Item, Child is a Person
#   "X HAS A Y"  -> composition   Mother has children, Car has an Engine

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

class Child(Person):                # is-a Person
    def __init__(self, name, birthdate):
        Person.__init__(self, name, birthdate)

class Mother(Person):               # is-a Person      (inheritance)
    def __init__(self, name, birthdate):
        Person.__init__(self, name, birthdate)
        self.children = []          # has-a list of Child (composition)

    def add_child(self, child):
        self.children.append(child)

mom = Mother("Maria", "1980-03-12")
mom.add_child(Child("Leo", "2010-07-01"))
mom.add_child(Child("Ana", "2013-11-20"))
print(f"{mom.name} has children: {[c.name for c in mom.children]}")


# ---------------------------------------------------------------------
# 3.5 Variations in class derivation
# ---------------------------------------------------------------------
#   The class name in parentheses is the base class (the class being inherited
#   from). Read each example from the code:
#     class Fruit(Produce) means "Fruit inherits from Produce."
#
#   1. Chain: Fruit inherits from Produce; Produce inherits from Item.
#      Fruit gets Produce's behavior and also inherits Item's behavior.
#          Item
#           |
#        Produce
#           |
#         Fruit
#   2. Siblings: Produce and Book each inherit from Item. Neither inherits
#      from the other.
#          Item
#         /    \
#    Produce   Book
#   3. Multiple inheritance: House inherits from both listed base classes.
class Fruit(Produce): pass          # 1. Fruit inherits from Produce
class Book(Item): pass              # 2. Book and Produce both inherit from Item
class Dwelling: pass
class Property: pass
class House(Dwelling, Property): pass   # 3. House inherits from both classes


# =====================================================================
# PART 4 - MULTIPLE INHERITANCE & MIXINS
# =====================================================================
#   Multiple inheritance means a class can inherit from more than one class.
#   Here, a VampireBat is both a WingedAnimal and a Mammal, so it can use
#   methods from both. Its __init__ calls both base constructors to set up
#   the attributes each one provides.
#
#   A mixin is a small class that adds one optional feature. LoggedItem gets
#   its name from Item and its logging method from LoggerMixin.

class WingedAnimal:
    def __init__(self):
        self.wingspan = 0.3
    def fly(self):
        print(f"Flying with a {self.wingspan} m wingspan")

class Mammal:
    def __init__(self):
        self.fur = "brown"
    def feed_young(self):
        print("Feeding young with milk")

class VampireBat(WingedAnimal, Mammal):
    def __init__(self):
        WingedAnimal.__init__(self)  # sets self.wingspan
        Mammal.__init__(self)        # sets self.fur

bat = VampireBat()
bat.fly()                           # inherited from WingedAnimal
bat.feed_young()                    # inherited from Mammal
print(f"{bat.fur=}")                # set by Mammal.__init__

class LoggerMixin:
    """Adds logging to any class."""
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class Item:
    def __init__(self, name):
        self.name = name

class LoggedItem(Item, LoggerMixin):
    def __init__(self, name):
        Item.__init__(self, name)    # sets self.name
        self.log(f"Created item: {name}")

item = LoggedItem("Laptop")         # [LoggedItem] Created item: Laptop
item.log("Item updated")            # [LoggedItem] Item updated


# =====================================================================
# EXTRA - PYTHON NOTES
# =====================================================================
#   Getters and setters are methods that read or change an attribute.
#   In Python, you can usually read or change a public attribute directly:
#       item.set_name("Hot Pockets")  ->  item.name = "Hot Pockets"
#   Use @property when you want normal attribute syntax (item.name) but
#   also need to validate or calculate the value.
#
#   Python does not enforce private attributes. By convention, a name like
#   _data means "internal; please don't use this from outside the class."
#   Inside a class, Python rewrites an attribute name that starts with two
#   underscores. For example, inside Account, self.__balance is stored under
#   the name self._Account__balance. This is called name mangling.
#   It helps avoid accidental clashes: if a subclass also uses self.__balance,
#   Python gives that attribute the subclass's name instead. The two attributes
#   won't accidentally overwrite each other. Name mangling is not security or
#   true privacy; code can still access the rewritten name if needed.
#   Inside Account's methods, write self.__balance; Python handles the rewrite.
#
#   UML class diagrams use + for public, - for private, and # for protected.
#   These are diagram labels, not Python syntax. Python's leading underscores
#   are conventions and name-mangling, not enforced access levels.
print("\n--- EXTRA: name mangling ---")

class Account:
    def __init__(self):
        self.__balance = 100        # Python stores this as _Account__balance

acct = Account()
try:
    print(acct.__balance)           # looks for __balance; that name isn't stored
except AttributeError:
    print("acct.__balance -> AttributeError")
print(f"{acct._Account__balance=}") # the mangled name can still be accessed


# =====================================================================
# Practice
# =====================================================================
# Ex 1  Create class Vehicle with __init__(self, make, year) and
#       describe() that prints "2020 Ford". Create Truck(Vehicle) that
#       adds payload and EXTENDS describe() to also print the payload.
#
# Ex 2  Shape has area() returning 0. Create Rectangle(w, h) and
#       Circle(r) that OVERRIDE area(). Loop over a list of shapes and
#       print each area (rounded to 2 decimals).
#
# Ex 3  Is-a or Has-a? Write "inheritance" or "composition":
#       a) Dog / Animal   b) Library / Book   c) Manager / Employee
#       d) Computer / CPU
#
# Ex 4  Write a mixin DescribeMixin with describe() that prints
#       "<ClassName>: <the object's __dict__>". Mix it into a Laptop class.
# =====================================================================

# =====================================================================
# RECAP
# =====================================================================
#   class Child(Base):           -> inherit
#   Base.__init__(self, ...)     -> create inherited instance attributes
#   Lookup: instance -> class -> base classes -> AttributeError
#   Override = replace a method | Extend = Base.method(self) + extra
#   is-a -> inheritance | has-a -> composition
#   class C(A, B):               -> multiple inheritance
#   Mixin = small class that only adds behavior
