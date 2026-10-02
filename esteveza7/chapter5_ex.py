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
