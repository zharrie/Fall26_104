
def ex1(party_size):
    if party_size == 1:
        return "counter"
    elif party_size == 2:
        return "small table"
    else:
        return "large table"

def ex2(n):
    return "even" if n % 2 == 0 else "odd"

def ex3(user_age):
    if user_age < 6:
        return "No teams"
    elif user_age < 8:
        return "U8 team"
    elif user_age < 10:
        return "U10 team"
    elif user_age < 12:
        return "U12 team"
    else:
        return "No teams"
    
def ex4(x):
    if(x>=1 and x<=99):
        return True
    return False

def ex5(age):
    if age <=12:
        return "$"+str(11)
    elif age >= 65:
        return "$"+str(12)
    else:
        return "$"+str(14)

def ex6(year):
    if (year >= 1955):
        print("carries several people")
    if (year < 1960):
        print("few safety features")
    if (year > 1994):
        print("has traction control")

def ex7(n):
    if (n in [-99,0,44]):
        return True 
    else:
        return False