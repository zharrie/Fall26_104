"""
==========================================================================
 CHAPTER 11 - MODULES
==========================================================================
"""

shutil.rmtree(DEMO, ignore_errors=True)
sys.path.insert(1, str(DEMO))                 # sys.path is a plain list: we add our demo folder

write("my_funcs.py", '''
    def factorial(num):
        """Calculates and returns the factorial (num!)"""
        x = 1
        for i in range(1, num + 1):
            x *= i
        return x

    def squared(num):
        return num * num
''')

write("shapes.py", '''
    cr = "#"

    def draw_square(size):
        for h in range(size):
            for w in range(size):
                print(cr, end="")
            print()

    def draw_rect(height, width):
        for h in range(height):
            for w in range(width):
                print(cr, end="")
            print()
''')

write("HTTPServer.py", '''
    print("  [HTTPServer.py is running]")     # demo only: shows WHEN this file runs
    import webpage
    address = "192.168.0.10"
''')

write("webpage.py", '''
    print("  [webpage.py is running]")        # demo only: shows WHEN this file runs

    def disp(ip):
        print(f"Displaying web page from {ip}")
''')

write("check_address.py", "import HTTPServer\nprint(HTTPServer.address)\n")
write("who_am_i.py", 'print("  inside who_am_i.py  __name__ =", repr(__name__))\n')

# Stand-ins for zyBooks Challenge modules (the PDF does not show their code)
write("pie_shop.py", 'def order_banana_pie(name, qty):\n    print(f"{name} ordered {qty} banana pie(s).")\n')
write("banana_pie.py", 'def make(qty):\n    print(f"Baking {qty} banana pie(s)...")\n')
write("airline_kiosk.py", 'def check_in(name, bags):\n    print(f"{name} checked in with {bags} bag(s).")\n')
write("airline_luggage.py", 'def deposit(bags):\n    print(f"{bags} bag(s) deposited.")\n')

# WebSearch: offline stand-in for the book's googlesearch version (same structure)
WEB_FUNCS = r'''
FAKE_WEB = {   # offline "search results", so the demo needs no internet / pip install
    "music videos": ["https://www.youtube.com/a", "https://vimeo.com/b",
                     "https://www.youtube.com/c", "https://www.forbes.com/d"],
    "statue of liberty": ["https://www.nps.gov/stli", "https://en.wikipedia.org/wiki/Liberty"],
    "mount rushmore": ["https://www.nps.gov/moru", "https://www.mtrushmorenationalmemorial.com/"],
}

def searchTerm(term):
    print(f"Searching for '{term}' ...")
    return FAKE_WEB.get(term.lower(), [])

def stringifyResult(term, urls, domainString):
    found = 0
    for url in urls:
        domain = url.split("//")[1].split("/")[0]
        if domain not in domainString:
            domainString = domainString + "\n" + domain
            found = found + 1
    print(f"{found} domain(s) found for search term '{term}'.")
    return domainString
'''
WEB_UI = r'''
print("Welcome to Web Search")
term = input("Enter search term: ")
result = searchTerm(term)
resultString = stringifyResult(term, result, "")
print(resultString)
print("\nEnd of Web Search")
'''
write("WebSearchOld.py", "# WebSearchOld.py - NO main guard\n" + WEB_FUNCS + "\n# user interface\n" + WEB_UI)
write("WebSearch.py", "# WebSearch.py - fixed with a main guard\n" + WEB_FUNCS
      + '\nif __name__ == "__main__":' + textwrap.indent(WEB_UI, "    "))
write("MultipleWebSearch.py", '''
    import WebSearch as ws

    print("Welcome to Multiple Web Search")
    term = input('Enter search term ("q" to quit): ')
    terms = 0
    resultString = ""
    while term != "q":
        terms = terms + 1
        result = ws.searchTerm(term)
        resultString = ws.stringifyResult(term, result, resultString)
        term = input('Enter search term ("q" to quit): ')
    if terms == 0:
        print("No search terms entered.")
    else:
        if terms == 1:
            print("Results for the one search term entered:")
        else:
            print("Results for the", terms, "search terms entered:")
        print(resultString)
    print("\\nEnd of Multiple Web Search")
''')



# 11.1 Modules
    # A) WHY MODULES?  SCRIPT vs. MODULE
    #    Code typed in the interactive interpreter (>>>) is lost when it closes,
    #    so we save code in a file and pass it to the interpreter:
    #        python report.py        -> report.py is a SCRIPT (a file you RUN)
    #    Problem: the same functions end up copied into many scripts, and long
    #    scripts get hard to maintain (fix a bug in one copy, the others keep it).
    #    MODULE = a .py file of code that can be IMPORTED and used by scripts,
    #             other modules, or the interactive interpreter.
    #    IMPORT = execute the module's code and make its definitions
    #             (functions, variables, classes) available to the importer.
    #
    #      WITHOUT a module                  WITH a module
    #      script1.py: def fct, def sq       funcs.py  : def fct, def sq  (ONCE)
    #      script2.py: def fct, def sq       script1.py: import funcs -> funcs.fct()
    #      (written twice)                   script2.py: import funcs -> funcs.fct()
    # -----------------------------------------------------------------------

    # Figure 11.1.2: a script that uses factorial() from my_funcs.py
    import my_funcs

    for answer in ["5", "3"]:
        with typed(answer):
            n = int(input("Enter number: "))
            fact = my_funcs.factorial(n)
            for i in range(1, n + 1):
                print(i, end=" ")
                if i != n:
                    print("*", end=" ")
            print(f"= {fact}")
    check(my_funcs.factorial(5), 120)

    # B) RULES OF  import module_name
    #    - The file name ends in .py; the import uses the name WITHOUT .py
    #          file HTTPServer.py   ->   import HTTPServer
    #    - Case-sensitive:  import ABC  and  import aBc  are different modules.
    #    - Python must FIND the file. Simplest: keep the module in the same folder
    #      as the script (11.2 explains the full search).
    #    - Good practice: imports at the TOP of the file, so a reader sees at once
    #      which modules the program needs. A module a program needs in order to
    #      run is called a DEPENDENCY.
    # -----------------------------------------------------------------------
    oops("import my_funcs.py")                 # don't write the extension
    oops("import My_Funcs")                    # capitalization matters

  
    # C) WHAT HAPPENS WHEN  import HTTPServer  RUNS
    #    sys.modules   = a dictionary of every module already loaded
    #    module object = a namespace (container) that holds a module's names
    #      1. Is HTTPServer in sys.modules?  YES -> reuse that module. Done.
    #      2. NO -> create a new module object, insert it in sys.modules
    #      3. Execute HTTPServer.py INSIDE that object: its defs and variables
    #         become names in the module's namespace (a nested "import webpage"
    #         goes through the same steps)
    #      4. Add the name HTTPServer to the importer's namespace
    #    => A module's code runs only ONCE per program, however many times
    #       (and from however many files) it is imported.
    # -----------------------------------------------------------------------

    import HTTPServer                          # runs HTTPServer.py, which imports webpage
    import webpage

    # D) USING AN IMPORTED MODULE:  module_name.name  (attribute reference)
    #        my_ip = HTTPServer.address      read a module variable
    #        webpage.disp(my_ip)             call a module function
    #    Definitions can be overwritten:  HTTPServer.address = "www.yahoo.com"
    #    The change is TEMPORARY: only in the running program. The file is not
    #    edited, so the next run imports the original value again.
    # -----------------------------------------------------------------------

    my_ip = HTTPServer.address
    webpage.disp(my_ip)
    HTTPServer.address = "www.yahoo.com"
    print("  A new run of Python (check_address.py prints HTTPServer.address):")

    # COMMON MISTAKES
    #   - writing .py in the import / wrong capitalization (shown above)
    #   - calling factorial(5) after  import my_funcs  (the prefix is required)

# 11.2 Finding modules
    # A) THE SEARCH ORDER
    #    import x  starts a search for x on the computer:
    #      1. BUILT-IN modules first (compiled into Python: sys, time, ...)
    #      2. otherwise the folders in  sys.path  (a list in the sys module),
    #         in this order:
    #           a. the folder of the executing script
    #           b. the folders listed in the environment variable PYTHONPATH
    #           c. the folder where Python is installed
    #    The FIRST match wins. No match anywhere -> ModuleNotFoundError.
    #
    #      import x -> built-in? -yes-> load it
    #                    | no
    #                 script folder -> PYTHONPATH folders -> Python install
    #                    | not found
    #                 ModuleNotFoundError
    # -----------------------------------------------------------------------
   
    # B) PYTHONPATH - modules kept in OTHER folders
    #    Small program: put the module next to the script.
    #    Large projects (tens/hundreds of modules, third-party modules) keep
    #    modules elsewhere -> tell Python where with the environment variable
    #    PYTHONPATH. An ENVIRONMENT VARIABLE is like a Python variable, but it is
    #    stored by the operating system and every program can read it.
    #      Windows (cmd) : set PYTHONPATH=c:\dir1;c:\other\directory
    #      macOS / Linux : export PYTHONPATH=/dir1:/other/directory
    #    'set' lasts for that terminal window only (Control Panel = permanent).
 

    # C) NEVER REUSE THE NAME OF AN EXISTING MODULE
    #    The search stops at the FIRST match, so file names matter:
    #      your own sys.py    -> ignored: built-in sys is found first
    #      your own random.py -> found in the script folder BEFORE the real
    #                            random module, which is now hidden -> errors
    #    Never name files math.py, random.py, time.py, string.py ...
    # COMMON MISTAKES
    #   - your file random.py hides the real random  (shown above)
    #   - module saved in another folder -> ModuleNotFoundError
    #       fix: move it next to the script, or add its folder to PYTHONPATH


# 11.3 Importing specific names: from ... import ... 
    # A) import module   vs.   from module import name
    #        from module_name import name1, name2, ...
    #    import my_mod             adds ONE name, my_mod, to your namespace;
    #                              reach the rest through it:  my_mod.calc(y)
    #    from my_mod import calc   COPIES only calc into your namespace:
    #                              calc(y)   (the name my_mod is NOT defined)
    #
    #      your names    my_mod's names           your names    my_mod's names
    #      my_mod -----> x = 55, def calc         calc <-copy-- x = 55, def calc
    #      z = my_mod.calc(y)                     z = calc(y)
    #
    #    Table 11.3.1  import HTTPServer              print(HTTPServer.address)
    #                  from HTTPServer import address print(address)
  
    # B) from module import *   copies ALL names of the module into yours.
    #    In a script it hides where names come from and what the program depends
    #    on. Good practice: use import * only in the interactive interpreter.
    # -----------------------------------------------------------------------
    from shapes import *              # works, but where does draw_rect come from?
    draw_rect(1, 6)

    # COMMON MISTAKES
    #   - from-import silently REPLACES a name you already had
    #   - import * in scripts hides where names come from

    def sqrt(x):
        return "my own sqrt"

    from math import sqrt            # replaces our sqrt without warning
    show("sqrt(16)")


# 11.4 Executing modules as scripts
    # A) THE PROBLEM: import runs ALL the module's global code
    #    Statements at the top level of a module (print, input, ...) execute when
    #    the module is imported -> an unwanted SIDE EFFECT.
    #    We want ONE file that works two ways:
    #      run as a script  -> show its user interface
    #      imported         -> just provide its functions, no side effects
    #    import X as Y : import module X but call it Y  (ws.searchTerm(...))

    print("\n  (offline stand-in for the book's googlesearch version: same structure)")
    print("\n>>> import WebSearchOld as ws      # we only wanted the functions...")
    with typed("Music videos"):
        import WebSearchOld as ws             # ...but the whole user interface runs

    # B) THE SPECIAL VARIABLE  __name__   (2 underscores each side)
    #    Python sets it automatically in every module:
    #      file RUN as a script  ->  __name__ == "__main__"
    #      file IMPORTED         ->  __name__ == the module name ("WebSearch")
  
    # C) THE FIX:   if __name__ == "__main__":
    #                   ...user interface...     runs ONLY when the file is run
    #    defs and classes stay OUTSIDE the if, so importers can still use them.
    # COMMON MISTAKES
    #   - no guard -> importing the file starts its prompts
    #   - defs placed INSIDE the guard -> importers can't use them
    #   - typo: "main" instead of "__main__" -> the branch never runs
    show('__name__ == "main"', '__name__ == "__main__"')


# 11.5 Reloading modules
    # A) WHY RELOAD?
    #    A module runs only ONCE. If its file is edited while the program runs,
    #    the program keeps the OLD version, and  import  again does nothing
    #    (the module is already in sys.modules).
    #        from importlib import reload
    #        reload(module)   re-runs the module's file and updates the SAME
    #                         module object IN PLACE (module must be imported)
    #
    #    import config      edit config.py      import config     reload(config)
    #    "Hello"            -> "Hi there"       still "Hello"     now "Hi there"

    # B) BOOK EXAMPLE: send_coupons.py e-mails thousands of customers. Stopping
    #    and restarting could e-mail some people twice, so after each e-mail it
    #    checks whether send_gmail.py changed, and reloads it if so.
    #      module.__file__          path of the module's file
    #      os.path.getmtime(path)   time the file was last modified
    #    newer time than the saved one -> file changed -> reload

    # C) reload does NOT update names copied with  from module import name
    #    reload updates the module object; a from-imported name is YOUR copy
    #    and keeps the old value -> if you plan to reload, use module.name.
    #    When is reload worth it? Long-running programs where restarting is
    #    costly, e.g. a web server: reload one module, keep clients connected.

    # COMMON MISTAKES
    #   - passing a string instead of the module      - forgetting to import reload
    #   - expecting from-imported names to update (they don't)

#11.6 Packages
    # A) WHAT IS A PACKAGE?
    #    PACKAGE    = a FOLDER of related modules, marked by a file __init__.py
    #    SUBPACKAGE = a package inside a package
    #    Large projects group related modules this way; dots follow the folders:
    #        import game.sound              game.sound.speech.talk()
    #    __init__.py is often empty, but may import the package's modules.
    #    Packages are found like modules: through the folders in sys.path.
    #    (Python 3.3+ tolerates a missing __init__.py, but always include it.)
    #
    #      game/                 <- package
    #        __init__.py
    #        sound/              <- subpackage: music.py effects.py speech.py
    #        graphics/           <- subpackage: models.py textures.py terrain.py

    # B) FOUR WAYS TO IMPORT FROM A PACKAGE
    #    import ASCIIArt                        the package only
    #    import ASCIIArt.canvas                 a module -> FULL path every time:
    #                                             ASCIIArt.canvas.draw_canvas()
    #    from ASCIIArt.figures import cow       a module -> short name: cow.draw()
    #    from ASCIIArt.figures.cow import draw  one function -> draw()

    # C) TWO RULES
    #    1. import a.b.c       -> c must be a package, subpackage or MODULE
    #       from a.b import c  -> c may ALSO be a function, class or variable
    #    2. Packages avoid name collisions: ASCIIArt.canvas and Graphics3D.canvas
    #       are different modules. But two from-imports of the same name
    #       OVERWRITE each other -> rename with  as.
    #       (Book: "3DGraphics" - a Python name can't start with a digit, so here
    #        it is Graphics3D.)

# 11.7 Standard library
    # A) THE STANDARD LIBRARY = modules that come WITH Python: just import them.
    #    Good practice: before writing code yourself, check whether the standard
    #    library (or the internet) already offers it.
    #    Full list: https://docs.python.org/3/library/
    #      datetime  dates and times              random  random numbers
    #      copy      complete copies of objects   time    current time, sleep
    #      math      mathematical functions       os      operating-system helpers
    #      sys       system / interpreter info    pdb     the interactive debugger
    #      urllib    URLs, e.g. requesting web pages
    # -----------------------------------------------------------------------
    import copy, datetime, math, os, random, urllib.parse

    random.seed(7)                            # same "random" results every run
    grid = [[1, 2], [3, 4]]
    clone = copy.deepcopy(grid)               # complete copy: inner lists copied too
    clone[0][0] = 99
    show("math.sqrt(49)", "math.cos(0)", "random.randint(1, 6)",
         "random.choice(['rock', 'paper', 'scissors'])", "grid", "clone",
         "round(time.time())", "os.name", "sys.version.split()[0]",
         "urllib.parse.urlparse('https://docs.python.org/3/library/').netloc")
    time.sleep(0.5)                           # pause half a second
    # urllib.request.urlopen("https://zybooks.com") would download that page
    # pdb: put  breakpoint()  in a program to pause there and inspect it
    #      (n = next line, p x = print x, c = continue, q = quit)

    # B) datetime
    #    datetime.date(2016, 5, 30)    a date  (datetime.date.today() = today)
    #    datetime.timedelta(days=30)   a DURATION;  date + timedelta -> new date
    #    date2 - date1                 a timedelta; .days = number of days
    #    d.strftime(format)            date -> text: %A weekday  %B month name
    #                                  %d day  %m month number  %Y year

    # a date N days from now
    today = datetime.date(2016, 5, 30)        # book's "today"; real: datetime.date.today()
    with typed("30"):
        days_from_now = int(input("Enter number of days from now: "))
        day_difference = datetime.timedelta(days=days_from_now)
        future_date = today + day_difference
        print(f"{days_from_now} days from now is {future_date.strftime('%B %d, %Y')}")
    check(future_date, datetime.date(2016, 6, 29))

    # C) random
    #    random.randint(a, b)   random integer from a to b (BOTH included)
    #    random.choice(lst)     a random item         random.shuffle(lst) in place
    #    random.seed(n)         numbers are PSEUDOrandom: same seed -> same
    #                           sequence every run -> repeatable tests (labs!)

    random.seed(1)
    first = [random.randint(1, 6) for _ in range(5)]
    random.seed(1)
    second = [random.randint(1, 6) for _ in range(5)]
    show("first", "second", "first == second")

    # Figure 11.7.2: draw cards until an ace
    random.seed(18)                           # added for a repeatable demo; remove to play
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
    random.shuffle(deck)
    num_drawn = 0
    game_over = False
    with typed("g", "g", "g", "g", "g"):
        user_input = input('Press any key to draw a card ("q" to quit): ')
        while user_input != "q" and not game_over:
            card = random.choice(deck)        # draw a random card...
            deck.remove(card)                 # ...and remove it from the deck
            num_drawn += 1
            print(f"\nCard drawn: {card}")
            if card == "A":
                game_over = True
            else:
                user_input = input('Press any key to draw a card ("q" to quit): ')
    if user_input == "q":
        print("\nGame was quit")
    else:
        print(f"{num_drawn} card(s) were drawn to find an ace.")
    check(num_drawn, 5)
