import math
#ex1 veichle and truck classes
class Vehicle:
    def __init__(self, make, year):
        self.make=make
        self.year=year
    def describe(self):
        print(f"{self.year} {self.make}")

class Truck(Vehicle):
    def __init__(self,make,year,payload):
        Vehicle.__init__(self,make,year)
        self.payload=payload
    def describe(self):
        Vehicle.describe(self)
        print(self.payload)

#ex2 shape, area, and rectangle classes
class Shape():
    def __init__(self,x,y):
        self.w=x
        self.h=y
    def area():
        return 0
    def type(self):
        return self.__class__.__name__
class Rectangle(Shape):
    def __init__(self,w,h):
        Shape.__init__(self,w,h)
    def area(self):
        return self.w*self.h
    def type(self):
        return self.__class__.__name__
class Circle(Shape):
    def __init__(self,r):
        Shape.__init__(self,0,0)
        self.r=r
    def area(self):
        return math.pi * self.r * self.r
    def type(self):
        return self.__class__.__name__

shapes = [Rectangle(10,2), Circle(5),Circle(10),Rectangle(2,11)]
for shape in shapes:
    print(f"{shape.type()} area: {shape.area():.2f} units")

# Ex 3  Is-a or Has-a? Write "inheritance" or "composition":
#       a) Dog / Animal   b) Library / Book   c) Manager / Employee
#.         is a.                has a.             is a OR has a 
#       d) Computer / CPU
#            has a


# Ex 4  Write a mixin DescribeMixin with describe() that prints
#       "<ClassName>: <the object's __dict__>". Mix it into a Laptop class.


class DescribeMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class Laptop(DescribeMixin):
    def __init__(self,model):
        self.model=model
    def describe(self):
        self.log(self.model)

newPC=Laptop("Dell")
newPC.describe()
