# ═══════════════════════════════════════════════════════════════════════════
#
#                           PART C · MODULES  (Ch. 11)
#
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# C1 · MODULES AND import                                              (11.1)
# • A SCRIPT is a .py file you RUN directly:  python report.py
#   A MODULE is a .py file whose code you want to REUSE. Instead of running
#   it, another file "imports" it to borrow its functions and classes.
#   Write useful code once, then import it wherever you need it.
# • To use a module, write:  import fractions
#   (just the file name "fractions", no ".py", and the spelling must match
#   exactly - Fractions would not work.)
# • What Python does the first time you  import fractions :
#     - it finds and runs the fractions file once, then remembers it, so
#       importing it again later does nothing (the code won't run twice).
# • After importing, reach inside it with a dot:  fractions.Fraction(1, 2)
#   (module name, then a dot, then the thing you want).
# • Put your imports at the TOP of the file. A module your program relies on
#   is called a DEPENDENCY.
#
#   A module is just a .py file. If our BankAccount (Parts A & B) lived in a
#   file called bank.py, we would write  import bank  and then use
#   bank.BankAccount("Cy", 10). Below we use Python's built-in "fractions"
#   module to show how importing works, so there's nothing extra to install.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C1 Modules and import ===")
print(f"{'fractions' in sys.modules=}")         # False: not loaded yet
import fractions                                # 1st import: runs + caches it
import fractions                                # 2nd import: nothing runs again
print(f"{'fractions' in sys.modules=}")         # True: loaded exactly once
half = fractions.Fraction(1, 2)                 # dot notation reaches its names
print(f"{half + fractions.Fraction(1, 3)=}")

# Import errors are exceptions too (Part B):
try:
    import bank                                 # no bank.py here -> fails
except ModuleNotFoundError as err:
    print(f"import bank -> ModuleNotFoundError: {err}")

# ───────────────────────────────────────────────────────────────────────────
# C2 · FINDING MODULES                                                 (11.2)
# • Search order for  import x :
#     1. BUILT-IN modules (compiled into Python: sys, time, ...)
#     2. the folders in sys.path (a plain list), in order:
#          a. the folder of the executing script
#          b. folders in the environment variable PYTHONPATH
#               Windows:      set PYTHONPATH=c:\dir1;c:\other\directory
#               macOS/Linux:  export PYTHONPATH=/dir1:/other/directory
#          c. the folder where Python is installed
#   First match wins. Nothing found -> ModuleNotFoundError.
# • NEVER name your file like an existing module (random.py, math.py ...):
#   yours is found in the script folder FIRST and hides the real one.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C2 Finding modules ===")
print(f"{'sys' in sys.builtin_module_names=}  {'fractions' in sys.builtin_module_names=}")
print(f"{sys.path[0]=}   <- the running script's folder, searched first")
print(f"{fractions.__file__=}   <- where Python found the module")

# ───────────────────────────────────────────────────────────────────────────
# C3 · from ... import ...   AND   import ... as ...                   (11.3)
# • import math                      -> one name, math; use math.sqrt
# • from math import sqrt            -> copies only that name; use sqrt
#                                       (the name math is NOT created)
# • import math as m                 -> import math but call it m
# • from module import *             -> copies ALL names; interpreter only
# • A from-import silently REPLACES a name you already had.
#   (If BankAccount lived in bank.py you would write
#    `from bank import BankAccount, InsufficientFundsError` to use them by
#    their short names - exactly the names we already defined in Part B.)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C3 from ... import ... / import ... as ... ===")
import math
from math import sqrt                           # copies just sqrt
import math as m                                # alias for the module
print(f"{sqrt(16)=}  {m.pi=}  {math.factorial(5)=}")
print(f"{m is math=}  (import ... as makes an alias, not a copy)")

# ───────────────────────────────────────────────────────────────────────────
# C4 · EXECUTING MODULES AS SCRIPTS: __name__                          (11.4)
# • The problem: importing a file RUNS everything in it. So if a file prints
#   something or asks for input at the top level, that happens the moment you
#   import it - usually not what you want. You wanted its functions, not its
#   test code.
# • Python's clue: every file has a built-in variable called __name__ that
#   tells the file HOW it was started:
#       - run directly (python bank.py)  ->  __name__ is "__main__"
#       - imported by another file       ->  __name__ is the file's name ("bank")
# • The fix: wrap your test code in an "if" that checks for that clue:
#       if __name__ == "__main__":
#           ...test code goes here...
#   This code runs only when the file is RUN directly, and is SKIPPED when the
#   file is imported. Keep your functions and classes OUTSIDE the if, so other
#   files can still import and use them.
#
#   # bank.py would end like this:
#   #     if __name__ == "__main__":        # runs only with:  python bank.py
#   #         test = BankAccount("Test", 100)
#   #         test.withdraw(30)
#   #         print(test)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C4 __name__ and the main guard ===")
print(f"{__name__=}   <- this file is being run directly")
print(f"{math.__name__=}   <- imported, so its name is the module name")
print("A main guard keeps a module's test code from running on import.")

# ───────────────────────────────────────────────────────────────────────────
# C5 · PACKAGES                                                        (11.6)
# • PACKAGE = a folder of related modules, marked by a file __init__.py
#   (often empty). Subpackage = a package inside a package. Dots follow the
#   folders:   urllib/                     (a real standard-library package)
#                __init__.py
#                parse.py   -> def quote(text), def urlparse(text), ...
# • Three ways to import, all shown below:
#     import urllib.parse               -> urllib.parse.quote("a b")
#     from urllib import parse          -> parse.quote("a b")
#     from urllib.parse import quote    -> quote("a b")
# • import a.b.c -> c must be a package or MODULE (not a function).
#   (A package of your own, e.g. school/grades.py, imports the same way:
#    import school.grades  /  from school import grades  /
#    from school.grades import letter.)
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C5 Packages ===")
import urllib.parse
from urllib import parse
from urllib.parse import quote
print(f"{urllib.parse.quote('a b')=}")
print(f"{parse.quote('x/y')=}  {quote('p q')=}")

# ───────────────────────────────────────────────────────────────────────────
# C6 · THE STANDARD LIBRARY                                            (11.7)
# • Modules that come WITH Python - just import them. Check here before
#   writing code yourself:  https://docs.python.org/3/library/
#     math  random  datetime  time  copy  os  sys  urllib  pdb ...
# • This file uses several: os, sys, csv, struct, math, fractions, urllib.
# ───────────────────────────────────────────────────────────────────────────
print("\n=== C6 Standard library ===")
import datetime
import random
random.seed(1)                  # same "random" numbers every run
print(f"{random.randint(1, 6)=}  {datetime.date(2026, 12, 25).strftime('%A')=}")

# Common mistakes
#   * import bank.py  /  import Bank   (wrong name or extension)
#   * Test code without the main guard -> runs on every import
#   * Classes/defs placed INSIDE the guard -> importers can't use them
#   * Naming files math.py, random.py, csv.py ...
