temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
counter = 0

for below_temperature in temperatures:
    if below_temperature < 0:
        counter += 1

print(f"total: {counter}")


print(" range(5)           -->", list(range(5)))
print(" range(3, 7)        -->", list(range(3, 7)))
print(" range(-7, -3)        -->", list(range(-7, -3)))
print(" range(0, 50, 10)        -->", list(range(0, 50, 10)))   

savings = 1000
for year in range(1,4):
    savings += savings * 0.05
    print(f" year {year} the savings were ${savings:.2f}")

print("==================================================")
print("\n")

for i in range(5):
    for j in range(3):
        print(i, ':' ,j)

print("\n")
print("==================================================")
print("\n")

user_input = input()

while user_input != "stop":
    print(f"I will continue and I don't care.")
    user_input = input()

print("Fine! I will stop!")