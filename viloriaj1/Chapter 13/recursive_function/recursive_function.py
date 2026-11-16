"""
IN-CLASS EXERCISES (use the two steps!)
  14.4-A  reverse_string(s) without slicing [::-1].     "abc" -> "cba"
  14.4-B  count_char(s, ch).                  count_char("banana", "a") -> 3
"""

def reverse_string(word, user_char, i, counter=0, new_word = ""):
    if i == len(word): # Base case
        return f"The reversed word is: {new_word} and there are {counter} of character {user_char}"
    if word[i] == user_char: # count specific character
        counter +=1
    new_word = word[i] + new_word # reverse word
    return reverse_string(word, user_char, i+1, counter, new_word) # Recursion

# user inputs word and character
user_input = input()
user_char = input()
print(reverse_string(user_input, user_char, 0))  # Output: reversed word and how many times the specific character is in the word.
    
