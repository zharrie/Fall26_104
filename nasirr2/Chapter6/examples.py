# Task:
#   a) Write compute_sum(num1, num2) that returns num1 + num2.
#   b) Write compute_cube(num) that returns num * num * num.
#   c) get_pattern() returns "*****". Call it twice to print 2 lines of stars.

def compute_sum(num1,num2):
    return num1+num2

def compute_cube(num):
    return num * num * num

def get_pattern():
    return "*****"

get_pattern()
get_pattern()

compute_cube(3) # 27
compute_sum(1,2) # 3


# Task (predict first!):
#   def get_birthday_age(user_age): return user_age + 1
#   print(get_birthday_age(42), get_birthday_age(20))   # -> ?
#   Is  def my_fct(user_num + 5):  a valid definition? No: parameters must be plain names
def get_birthday_age(user_age):
    return user_age+1

print(get_birthday_age(42),get_birthday_age(20)) # 43 21


# Task:
#   a) Write celsius_to_fahrenheit(c): F = C * 9/5 + 32.   Test: 50 -> 122
def celsius_to_farenheit(c):
    f = c * 9/5 + 32
    return f
    
celsius_to_farenheit(50) # 122


# Task: print_negatives(numbers)

def print_negative(numbers):
    for num in numbers:
        if num < 0:
            print(num)

num_to_print_neg = [1,2,-1,-2,30,-40,-70,-90,100,-200]
print_negative(num_to_print_neg)