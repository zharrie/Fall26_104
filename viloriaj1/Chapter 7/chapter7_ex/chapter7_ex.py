
""" Chapter 7 execises for Python
Strings
"""

print("Please enter a word:")
spring_to_slice = input()

counter = 0

for index_num in range(len(spring_to_slice)):
    letter_index = spring_to_slice[index_num]
    print(f"the index is: {counter} for the following letter {letter_index}")
    counter += 1

print(f"Index is: {spring_to_slice[0:-2]}")
print(f"Index is: {spring_to_slice[:-2]}")
print(f"Index is: {spring_to_slice[::2]}")

#=========================================================================================================================================

try:
    """ String Methods"""
    print(f"Find Method: {spring_to_slice.find("D")}")
    print(f"is all Capital? Letter: {spring_to_slice.isupper()}")
    print(f"Capital Letter: {spring_to_slice.upper()}")
    print(f"lower Letter: {spring_to_slice.lower()}")
    print(f"Clean Letter: {spring_to_slice.strip()}")
    print(f"Title Letter: {spring_to_slice.title()}")
    print(f"Split: {spring_to_slice.split()}")
    print(f"Split: {spring_to_slice.split('/')}")
except:
    print(f"The error found")

print("==========================================================================")
print()

# =============================================================================
#  YOUR TURN 
#   1. From "<your-firstname>.<your-lastname>@montclair.edu", print the username and the domain
#      using find() and slicing.
#   2. Turn "portable network graphics" into the acronym "PNG".
#   3. Turn the date "2025-09-18" into "09/18/2025" using split() and join().
# =============================================================================

print("==========================================================================")
print("Please enter your email: ", end="")
user_email = input()
user_name, domain_name = user_email.split("@")
print("Username is: ", user_name)
print("Domain is: ", domain_name)
print()
print("====================================================================")
acronym_name = "portable network graphics"
acronym_name_1, acronym_name_2, acronym_name_3 = acronym_name.split()
acronym_name_1 = acronym_name_1.replace(acronym_name_1, "P")
acronym_name_2 = acronym_name_2.replace(acronym_name_2, "N")
acronym_name_3 = acronym_name_3.replace(acronym_name_3, "G")
network_graphic_extension = acronym_name_1 + acronym_name_2 + acronym_name_3
print(network_graphic_extension)
print()
print("===================================================================")
print("Please enter date in the format (2025-05-05): ", end="")
date_input = input()

year, month, day = date_input.split("-")

new_date_format = month + "/" + day + "/" + year

print(new_date_format)





