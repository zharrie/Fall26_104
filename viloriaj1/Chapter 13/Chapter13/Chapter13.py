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
#       "<ClassName>: <the object's __dict__>". Mix it into a Laptop class
import math

class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        print(f"{self.year} {self.make}")

class Truck(Vehicle):
    def __init__(self, make, year, payload):
        Vehicle.__init__(self, make, year)
        self.payload = payload

    def describe(self):
        Vehicle.describe(self)
        print(self.payload)

user_input_make = input()
user_input_year = input()
user_input_payload = input()


print("================================================")
print("Vehicle")
auto = Vehicle(user_input_make, user_input_year)
auto.describe()


print("================================================")
print("Truck")
auto1 = Truck(user_input_make, user_input_year, user_input_payload)
auto1.describe()

class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        print(0)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        Shape.area(self)
        area = self.w * self.h
        print(f"{area:.2f}")
        

class Circle(Shape):
    def __init__(self, w, h, r):
        Shape.__ini__(self, w, h)
        self.r = r

    def area(self):
        Shape.area(self)
        self.area = (math.pi) * (self.r**2)
        print(f"{self.area:.2f}")

user_input_w = int(input())
user_input_h = int(input())
user_input_r = int(input())


print("================================================")
print("Shape")
shape1 = Shape(user_input_w, user_input_h)
shape1.area()

print("================================================")
print("Rectangle")
rectangle1 = Rectangle(user_input_w, user_input_h)
rectangle1.area()

print("================================================")
print("Rectangle")
circle1 = Rectangle(user_input_w, user_input_h)
c1.area()

      
