# task: total = 5
# Write a while loop that prints total while it is <= 25, doubling it each time. 
# What are the three numbers printed?"
total = 5
while total<=25:
    print(total)
    total*=2


#task("num_insects = 8. Write a while loop that runs while num_insects"
#  "\n     is <= 100: print it, then double it. (8 16 32 64)")
num_insects = 8
while num_insects <= 100:
    print(num_insects)
    num_insects *= 2

#task("temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]."
#         "\n     Use a for loop to count how many are below freezing (< 0).")
temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
count = 0
for temp in temperatures:
    if temp < 0:
        count += 1
print(count)

count = 0
for temp in range(len(temperatures)):
    if temp < 0:
        count += 1
print(count)

# task("Write the SIMPLEST range() for each:"
#          "\n     (a) every integer 0 to 500   (b) every integer 10 to 20"
#          "\n     (c) every 2nd integer 10 to 20  (d) every integer 5 down to -5")
for i in range(0,501,1):
    print(i)
for i in range(10,21,1):
    print(i)
for i in range(10,21,2):
    print(i)
for i in range(5,-6,-1):
    print(i)
for i in reversed(range(-5,6,1)):
    print(i)

# task("'Simon says': compare simon = 'RRGBRYYBGY' to user = 'RRGBBRYBGY'"
#      "\n     one index at a time. Add 1 point per match, break on the"
#      "\n     first mismatch, then print the score.")
simon = 'RRGBRYYBGY' ; user = 'RRGBBRYBGY'
output = "Different string"
if len(simon) == len(user):
    for char in range(len(simon)):
        if(simon[char]==user[char]):
            continue
        else:
            output += f" @ index: {char}. {simon[char]}!={user[char]}"
            break
    else:
        output = "Same string"


print(output)


# make an infinite for loop
list1 = ["",""]
for item in list1:
    list1.append("")
    print(count)

