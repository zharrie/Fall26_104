total = 5
while total <= 25:
    print(total)
    total *= 2
5
10
20

import random
animals = ["goat", "cat", "lion", "pigeon", "ant", "giraffe", "snake"]
for count in range(23):
    number = random.randint(1, 99)
    animal = random.choice(animals)
    print(number, animal)



temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
counter=0
i=0
for item in range(len(temperatures)):
    temperatures.append(i)
    print(len(temperatures))

#practice 5 chapt 8
scores = {"Peter": 45, "Michael": 90, "Cy": 55, "leslie": 76}
top_two = sorted(scores, key=scores.get, reverse=True)[:2]
print(f"5. {top_two=}")


# =====================================================================
# Practice
# =====================================================================
# Ex 1  Create class Vehicle with __init__(self, make, year) and
#       describe() that prints "2020 Ford". Create Truck(Vehicle) that
#       adds payload and EXTENDS describe() to also print the payload.

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
        print(f"Payload: {self.payload}")


truck = Truck("Ford", 2020, "2 tons")
truck.describe()

# 2020 Ford
# Payload: 2 tons
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
