"""
===============================================================================
CHAPTER 7: STRINGS
===============================================================================
"""
import math

# =============================================================================
#  7.1  STRING SLICING
# =============================================================================
#    * s[i] reads ONE character.  s[start:end] reads a SLICE -> a NEW string
#    * START is included, END is NOT
#    * Negative indices count from the end:  s[-1] is the last character
#
#        s = "Boggle"     | B | o | g | g | l | e |
#                         0   1   2   3   4   5   6     <- think of indices as
#                        -6  -5  -4  -3  -2  -1            fences between letters
# =============================================================================
s = "Boggle"
print(f"{s[0]=}   {s[-1]=}   {s[0:3]=}")

url = "http://en.wikipedia.org/wiki/Turing"              
print(f"{url[7:23]=}")

name = "John Doe"
print(f"{name[0:4]=}")        # 'John'  -> the space at index 4 is NOT included
print(f"{name[4:7]=}")        # ' Do'   -> this time the space IS included
print(f"{name[5:10]=}")       # 'Doe'   -> an end past the string is fine
print(f"{'Jane Doe!?'[0:-2]=}")

# A slice is a NEW object - changing the original later does not change it
sentence = "The cat jumped the brown cow"
animal = sentence[4:7]
sentence = "The fox jumped the brown llama"
print(f"The animal is still a {animal}")

# Omit start -> from the beginning.  Omit end -> to the end.  Variables work too.
greet = "Hey folks!"
x, y = 1, 5
print(f"{greet[:5]=}   {greet[5:]=}   {greet[:]=}   {greet[x:y]=}")
print(f"{greet[2:1]=}   {greet[50:]=}")     # empty string '' - never an error

# Common slicing operations
wiki = "http://en.wikipedia.org/wiki/Nasa/"
print(f"{wiki[10:19]=}")      # indices 10-18
print(f"{wiki[10:-5]=}")      # 10 up to the 5th-from-last
print(f"{wiki[8:]=}")         # index 8 to the end
print(f"{wiki[:23]=}")        # everything before index 23
print(f"{wiki[:-1]=}")        # all but the last character

# THE STRIDE:  s[start:end:stride] - how far to jump after each character
numbers = "0123456789"
print(f"{numbers[::2]=}   {numbers[1:9:3]=}   {numbers[::-1]=}")   # [::-1] reverses!

# ---- Examples ----------------------------
quiz = "The cat in the hat"
reddit = "http://reddit.com/r/python"
protocol = "http://"
secret = "Agt2t3afc2kjMhagrds!"
print(f"{quiz[0:3]=}")                     # 'The'
print(f"{quiz[3:7]=}")                     # ' cat'  (leading space!)
print(f"{reddit[17:]=}")                   # '/r/python'
print(f"{reddit[len(protocol):]=}")        # 'reddit.com/r/python'  (no magic numbers)
print(f"{secret[0:5:1]=}")                 # 'Agt2t'
print(f"{secret[::2]=}")                   # 'AttackMars'  <- a hidden message!

# ---- COMMON MISTAKES ---------------------------------------------------------
#   x  Expecting END to be included:  "Boggle"[0:3] is "Bog", not "Bogg"
#   x  greet[99]  -> IndexError  (but the slice greet[1:99] is fine)
#   x  greet[0] = "J"  -> TypeError: strings are IMMUTABLE. Build a new one:
print(f"{'J' + greet[1:]=}")

# =============================================================================
#  7.2  ADVANCED STRING FORMATTING
# =============================================================================
#  The format specification goes after a colon inside { }
#
#        f"{value : [fill] [align] [width] [.precision f] }"
#
#    width      MINIMUM characters. Long values are never cut off.
#    align      <  left     >  right     ^  center
#               default: strings LEFT, numbers RIGHT
#    fill       padding character (default space). Needs an align: {n:0>4}
#    .Nf        N digits after the decimal point: pads with 0s or ROUNDS
#
#  Brackets [ ] in the demos below make the spaces visible.
# =============================================================================
print(f"[{'Bob':10}]   [{42:10}]   [{'Christopher':5}]")   # default alignment

# A formatted table (widths + alignment + precision)
players = [("Sadio Mane", 22, 36), ("Mohamed Salah", 22, 38),
           ("Sergio Aguero", 21, 33), ("Jamie Vardy", 18, 34),
           ("Gabriel Jesus", 7, 29)]
print(f"\n{'Player Name':<16}{'Goals':>6}{'Games':>7}{'Per Game':>10}")
print("-" * 39)
for player, goals, games in players:
    print(f"{player:<16}{goals:>6}{games:>7}{goals / games:>10.2f}")
# Practice: change every < and > above to ^ and run again.

# Fill characters
score = 9
print(f"\n[{score:4}]   [{score:0>4}]   [{18:0>4}]   [{18:0^4}]")
player_name, goal_total = "Wayne Rooney", 36
print(f"{player_name:<16}{goal_total:>6}")          # default space fill
print(f"{player_name:<16}{goal_total:0>6}")         # '0' fill
print(f"{player_name:_<16}{goal_total:0>6}")        # '_' fill

# Precision
approximate_pi = 22.0 / 7.0
print(f"\npi is {math.pi}")
print(f"22/7 is {approximate_pi}")
print(f"22/7 looks better like {approximate_pi:.2f}")

# ---- Examples ----------------------------
print(f"[{'Bob':<5}]")            # [Bob  ]
print(f"[{'Bob':>5}]")            # [  Bob]
print(f"[{'Bob':^5}]")            # [ Bob ]
print(f"[{'Bob':<5}{1:<2}]")      # [Bob  1 ]
print(f"[{'Bob':<5}{1:>2}]")      # [Bob   1]
print(f"[{'Sally':@>8}]")         # [@@@Sally]     fill in {score:*>4} is '*'
print(f"[{5:.1f}]  [{5:.3f}]  [{5.25:.3f}]  [{5.2589:.3f}]  [{5:4.1f}]")
#        5.0        5.000      5.250         5.259 (rounded)    ' 5.0' (width 4)

# ---- COMMON MISTAKES ---------------------------------------------------------
#   x  Forgetting the colon:           {name10}   ->  {name:10}
#   x  Fill without an alignment:      {name:*10} ->  {name:*<10}   (ValueError)
#   x  Using .2f on a string                                        (ValueError)


# =============================================================================
#  7.3  STRING METHODS
# =============================================================================
#    * Strings are IMMUTABLE. A method never changes the string - it RETURNS
#      a new one, so SAVE the result:     phrase = phrase.replace("a", "b")
#
#    FIND      find(x[, start[, end]])   rfind(x)   count(x)   (find: -1 = not found)
#    REPLACE   replace(old, new[, count])
#    TEST      isalnum  isdigit  islower  isupper  isspace  startswith  endswith
#    CHANGE    capitalize  lower  upper  strip  title
# =============================================================================

# --- Finding and replacing ---
phrase = "Someday I will have three goats, six horses, and nine llamas."
phrase = phrase.replace("three", "tres")
phrase = phrase.replace("six", "seis")
phrase = phrase.replace("nine", "nueve")
print("Translation:", phrase)
print(f"{'aaaa'.replace('a', 'b', 2)=}")      # only the first 2

word = "cat"
word.replace("c", "b")                        # result thrown away!
print(f"{word=}")                             # still 'cat'
word = word.replace("c", "b")
print(f"{word=}")                             # 'bat'

boo = "Boo Hoo!"
print(f"{boo.find('!')=}   {boo.find('Boo')=}   {boo.find('oo')=}")
print(f"{boo.find('oo', 2)=}   {boo.find('oo', 2, 4)=}")
print(f"{boo.rfind('oo')=}   {boo.count('oo')=}")

# Don't need the position? Use `in` - simpler and clearer
superhero_name = "The batman returns"
if "batman" in superhero_name:
    print("Found batman!")

# Try - Hangman
secret_word = "onomatopoeia"
guessed = ""
for guess in "oxatpmnei":                     # live: guess = input("Letter: ")
    guessed += guess
    board = ""
    for letter in secret_word:
        if letter in guessed:
            board += letter
        else:
            board += "-"
    print(f"guess {guess}: {board}")

# --- Comparing strings ---
#   Python compares character by character using ASCII/Unicode values and
#   stops at the FIRST difference.   'A'=65 ... 'Z'=90   <   'a'=97 ... 'z'=122
print(f"\n{'Hello' == 'Hello!'=}")
print(f"{'Yankee Sierra' > 'Amy Wise'=}")         # 'Y' > 'A'
print(f"{'Yankee Sierra' > 'Yankee Zulu'=}")      # 'S' < 'Z'
print(f"{'seph' in 'Joseph'=}   {'jo' in 'Joseph'=}")   # case-sensitive
print(f"{'Jo' < 'Joseph'=}")                      # shorter string is less
print(f"{'Banana' < 'apple'=}")                   # 'B'(66) < 'a'(97) - surprise!
print(f"{'Kay, Jo' > 'Kay, Amy'=}   {ord('J')=}  {ord('A')=}")   # Participation 7.3.1

# `is` checks SAME OBJECT, not same VALUE. Always use ==.
first = "Amy"
student_name = first + " Adams"                   # built at runtime, like input()
teacher_name = "Amy Adams"
print(f"{student_name == teacher_name=}   {student_name is teacher_name=}")

# --- Methods that return True / False ---
print(f"\n{'abc?'.islower()=}")                   # ignores non-letters
print(f"{'report.pdf'.endswith('.pdf')=}")

# --- Methods that create new strings ---
messy = "   hELLO wORLD   "
print(f"{messy.strip()=}")
print(f"{messy.strip().capitalize()=}")          # methods can be CHAINED
print(f"{messy.strip().title()=}")
print(f"{messy.lower()=}   {messy.upper()=}")

# Good practice: clean input the moment you read it:  name = input().strip().lower()
# Try - passenger database: "Amy Adams" and "  AMY ADAMS " are the same person
passengers = []
for raw_name in ["Amy Adams", "  AMY ADAMS ", "bob lee"]:
    clean = raw_name.strip().lower()
    if clean in passengers:
        print(f"{clean.title()} is already booked")
    else:
        passengers.append(clean)
print(passengers)

# ---- Examples - True or False? -------------------------
blank_lines = "\n \n"
print(f"{'HTTPS://google.com'.isalnum()=}")              # False  (: / .)
print(f"{'HTTPS://google.com'.startswith('HTTP')=}")     # True
print(f"{blank_lines.isspace()=}")                       # True
print(f"{'1 2 3 4 5'.isdigit()=}")                       # False  (spaces)
print(f"{'LINCOLN, ABRAHAM'.isupper()=}")                # True

# ---- COMMON MISTAKES ---------------------------------------------------------
#   x  Calling a method but not saving the result (immutability)
#   x  name.upper  without ()  -> that is the method itself, not the result
#   x  Using `is` instead of ==
#   x  if s.find("Boo"):   -> a match at index 0 returns 0, which counts as False!
print(f"{bool('Boo Hoo!'.find('Boo'))=}   {'Boo' in 'Boo Hoo!'=}")

# =============================================================================
#  7.4  SPLITTING AND JOINING STRINGS
# =============================================================================
#    split():  ONE string  ->  LIST of tokens      "a#b#c".split("#")
#              no argument = split on any whitespace, never gives ''
#              the separator is removed from the tokens
#    join():   LIST of strings  ->  ONE string     "/".join(tokens)
#              called on the SEPARATOR, not on the list
#    Pattern:  split  ->  change the tokens  ->  join
# =============================================================================
print(f"{'Martin Luther King Jr.'.split()=}")
print(f"{'Music/artist/song.mp3'.split('/')=}")

# '' appears when the string starts/ends with the separator or has two in a row
url1 = "http://en.wikipedia.org/wiki/Lucille_ball"
url2 = "en.wikipedia.org/wiki/ethernet/"
print(f"{url1.split('/')=}")
print(f"{url2.split('/')=}")
print(f"{url1.split('//')=}")                   # Try: a two-character separator

# join
print(f"{'@'.join(['billgates', 'microsoft'])=}")
web_path = ["www.website.com", "profile", "settings"]
print(f"{'/'.join(web_path)=}")
print(f"{''.join(['http://', 'www.', 'ebay', '.com'])=}")

# join vs. a loop - same result, one line
phrases = ["To be, ", "or not to be.\n", "That is the question."]
sentence = ""
for p in phrases:
    sentence += p
print(sentence)
print("".join(phrases))

# split + join together: replace separators
path = "C:/Users/Wolfman/Documents/report.pdf"
tokens = path.split("/")
print("\\\\".join(tokens))

# split + join together: edit tokens
for wiki_url in ["http://en.wikipedia.org/wiki/Rome", "http://en.wikipedia.org/Rome"]:
    tokens = wiki_url.split("/")               
    if "wiki" != tokens[3]:
        tokens.insert(3, "wiki")
        new_url = "/".join(tokens)
        print(f"{wiki_url} is not a valid address.")
        print(f"Redirecting to {new_url}")
    else:
        print(f"Loading {wiki_url}")

# ---- Examples ----------------------------
song = "I scream; you scream; we all scream, for ice cream.\n"
print(song.split())               # words only - the \n disappears
print(song.split("\n"))           # [sentence, '']
print(song.split("scream"))       # "cream." stays - it isn't "scream"
print(".".join(["images", "google", "com"]))     # images.google.com
print("".join(["New", "York"]))                  # NewYork
title = "Python-Lab-Warmup"
tokens = title.split("-")
title = ":".join(tokens)
print(title)                                    

# ---- COMMON MISTAKES ---------------------------------------------------------
#   x  ["a", "b"].join("-")    -> AttributeError. Write "-".join(["a", "b"])
#   x  "-".join([1, 2, 3])     -> TypeError. Items must be strings:
print("-".join([str(n) for n in [1, 2, 3]]))
#   x  s.split(" ") on text with double spaces -> '' tokens. Use s.split()

# =============================================================================
#  YOUR TURN 
#   1. From "<your-firstname>.<your-lastname>@montclair.edu", print the username and the domain
#      using find() and slicing.
#   2. Turn "portable network graphics" into the acronym "PNG".
#   3. Turn the date "2025-09-18" into "09/18/2025" using split() and join().
# =============================================================================


# =============================================================================
#  RECAP - CHAPTER 7
# -----------------------------------------------------------------------------
#  SLICE     s[start:end:stride]   end excluded  |  s[:n]  s[n:]  s[:]  s[::-1]
#  FORMAT    f"{v:[fill][align][width][.prec]f}"   < > ^   {x:0>4}  {p:8.2f}
#  FIND      find  rfind  count  replace          (use `in` for yes / no)
#  TEST      isalnum  isdigit  islower  isupper  isspace  startswith  endswith
#  CHANGE    lower  upper  capitalize  title  strip   -> RETURN a new string
#  COMPARE   ==  (never `is`)  |  by ASCII, case-sensitive: 'Z'(90) < 'a'(97)
#  SPLIT     s.split()  s.split(sep) -> list     JOIN   sep.join(list) -> string
#  REMEMBER  Strings are IMMUTABLE:   s = s.upper()
# =============================================================================
