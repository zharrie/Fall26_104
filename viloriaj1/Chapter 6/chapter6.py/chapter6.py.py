#   a) Write compute_sum(num1, num2) that returns num1 + num2.

def compute_sum(num1, num2):
    return num1 + num2

print("Please enter a value: ", end="")
user_input1 = int(input())
print("Please enter a value: ", end="")
user_input2 = int(input())

print(f"The sum of the two numbers is:  {compute_sum(user_input1, user_input2)}")
print()


#   b) Write compute_cube(num) that returns num * num * num.

def compute_cube(num):
    return num * num * num

print("Please enter a value: ", end="")
user_input3 = int(input())
print(f"The cube is:  {compute_cube(user_input3)}")

# Task (predict first!):
#   def get_birthday_age(user_age): return user_age + 1
#   print(get_birthday_age(42), get_birthday_age(20))   # -> ?
#   Is  def my_fct(user_num + 5):  a valid definition? (No: parameters must be plain names)

def get_birthday_age(user_age):
    return user_age + 1

print(get_birthday_age(42), get_birthday_age(20))
