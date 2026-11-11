"""
==========================================================================
 Working with Files in Python: File I/O
==========================================================================
"""
import os
import sys
import csv
import struct

LIVE = True

# ---- Setup: sandbox folder + sample files (`with` is explained in Part 7) ----
os.makedirs("io_demo", exist_ok=True)
os.chdir("io_demo")

with open("myfile.txt", "w") as f:
    f.write("Gotham is quiet tonight.\nThe signal is on.\nTime to go.\n")
with open("numbers.txt", "w") as f:
    f.write("10\n20.5\n30\n")


# ==========================================================================
# PART 1: READING DATA FROM FILES
# ==========================================================================
# Key ideas
#   * open(path) returns a file object. Default mode is "r" (read).
#       open("myfile.txt")                          -> same folder as script
#       open("C:\\Users\\BWayne\\tax_return.txt")   -> full path (escape \)
#   * Always call file.close() when done. A closed file can't be used.
#   * Three ways to read (all stop at end-of-file, EOF):
#       file.read()       -> whole file as ONE string   (read(n): n characters)
#       file.readlines()  -> LIST of strings, one per line
#       file.readline()   -> ONE line per call; returns "" at EOF
#   * Lines keep their trailing "\n". Use .strip() to remove it.
#   * A file object is iterable: for line in file:  (memory-friendly)
print("\n===== PART 1: Reading =====")

# read(): everything as one string
file = open("myfile.txt")
contents = file.read()
file.close()
print(f"{contents=}")

# read(n): in text mode, n = number of characters; reading resumes where it stopped
file = open("myfile.txt")
print(f"{file.read(9)=}")
print(f"{file.read(6)=}")
file.close()

# readlines(): list of lines
file = open("myfile.txt")
lines = file.readlines()
file.close()
print(f"{lines=}")
print(f"{lines[0]=}")
print(f"{len(lines)=}")

# readline(): one line at a time (good for large files)
file = open("myfile.txt")
print(f"{file.readline()=}")
print(f"{file.readline()=}")
print(f"{file.readline()=}")
print(f"{file.readline()=}")      # '' -> EOF reached
file.close()

# Iterating directly over the file object
file = open("myfile.txt")
for line in file:
    print(line.strip())
file.close()

# Typical workflow: 1) read  2) iterate over lines  3) compute a result
file = open("numbers.txt")
total = 0
count = 0
for line in file:
    number = float(line)          # float() ignores surrounding whitespace/"\n"
    total += number
    count += 1
file.close()
print(f"Count = {count}, Total = {total}, Average = {total / count:.2f}")

# Common mistakes
#   * Forgetting file.close()           * Forgetting that lines end with "\n"
#   * Reading the same file twice and getting ''  (already at EOF)
#   * FileNotFoundError: the script runs from a different folder than expected


# ==========================================================================
# PART 2: WRITING DATA TO FILES & FILE MODES
# ==========================================================================
# Key ideas
#   * file.write(s) writes a STRING. Convert numbers first: str(5.75)
#   * write() does NOT add "\n" - add it yourself.
#   * The mode is the 2nd argument of open():
#
#     Mode | Purpose   | Read | Write | Creates file? | Overwrites?
#     -----+-----------+------+-------+---------------+------------
#     "r"  | reading   | Yes  | No    | No (error)    | No
#     "w"  | writing   | No   | Yes   | Yes           | YES
#     "a"  | appending | No   | Yes   | Yes           | No (adds to end)
#
#   * Add "+" for update modes: "r+" read & write, "w+" read & write
#     (still overwrites).
#   * Buffering: write() stores data in memory first; it reaches the disk
#     later. file.flush() forces it out; close() flushes automatically.
#     (Some systems also need os.fsync(file.fileno()) for a physical write.)
#       buffering=0    -> no buffering (binary mode only)
#       buffering=1    -> line-buffered (text mode): written at each "\n"
#       buffering=100  -> custom buffer size (bytes)
#     Note: for regular disk files the default is a block buffer
#     (io.DEFAULT_BUFFER_SIZE, typically 8192 bytes); line buffering is the
#     default for interactive terminals.
print("\n===== PART 2: Writing =====")

file = open("output.txt", "w")
file.write("Hello, world!\n")
file.write(str(5.75) + "\n")      # number -> string first
chars = file.write("Done")        # write() returns the number of characters
file.close()
print(f"{chars=}")
# file.write(5.75)   # TypeError: write() argument must be str, not float

file = open("output.txt")
print(f"{file.read()=}")
file.close()

# "w" overwrites
file = open("log.txt", "w"); file.write("first\n"); file.close()
file = open("log.txt", "w"); file.write("second\n"); file.close()
file = open("log.txt"); print(f"after 'w' twice: {file.read()=}"); file.close()

# "a" appends
file = open("log.txt", "a"); file.write("third\n"); file.close()
file = open("log.txt"); print(f"after 'a':       {file.read()=}"); file.close()

# "r+" read and write (writes go where the file position is: here, the end)
file = open("log.txt", "r+")
print(f"{file.read()=}")
file.write("fourth\n")
file.close()

# Buffering in action (os.path.getsize = file size on disk, see Part 3)
file = open("buffer_demo.txt", "w")
file.write("Still in memory")
print(f"before flush: {os.path.getsize('buffer_demo.txt')=}")   # 0
file.flush()
print(f"after flush:  {os.path.getsize('buffer_demo.txt')=}")   # 15
file.close()

file = open("line_buffered.txt", "w", buffering=1)
file.write("Written at newline\n")
print(f"line-buffered: {os.path.getsize('line_buffered.txt')=}")  # 19
file.close()

# Common mistakes
#   * Using "w" when you meant "a" -> data lost
#   * Passing a number to write()  -> TypeError
#   * Forgetting "\n"              -> everything on one line
#   * Not closing/flushing         -> data may not be on disk yet


# ==========================================================================
# PART 3: NAVIGATING THE FILE SYSTEM WITH THE os MODULE
# ==========================================================================
# Key ideas
#   * import os -> interface to operating-system functions.
#   * Path separators differ:  Windows "subdir\\bat_mobile.jpg"
#                              Mac/Linux "subdir/bat_mobile.jpg"
#   * os.path.join(...) builds a path with the correct separator -> portable.
#   * os.path.sep holds the separator of the current OS.
#   * Useful functions:
#       os.path.exists(p)  os.path.isfile(p)  os.path.isdir(p)
#       os.path.getsize(p) os.path.splitext(p) os.path.basename(p)
#       os.getcwd()  os.listdir(p)  os.makedirs(p)  os.remove(p)  os.rmdir(p)
#   * os.walk(top) visits every directory in a tree and yields a 3-tuple:
#       (dirname, subdirs, files)
print("\n===== PART 3: os module =====")

# Hardcoded (Windows only):  path = "subdir\\bat_mobile.jpg"   <- avoid
path = os.path.join("subdir", "bat_mobile.jpg")
print(f"{path=}")                 # separator depends on the OS running this
print(f"{os.path.sep=}")
# On Windows: os.path.join("C:\\", "subdir1", "myfile.txt") -> 'C:\\subdir1\\myfile.txt'

# Splitting a path into its components
full = os.path.join("Users", "BWayne", "tax_return.txt")
print(f"{full.split(os.path.sep)=}")

# Inspecting paths
print(f"{os.getcwd()=}")
print(f"{os.path.exists('myfile.txt')=}")
print(f"{os.path.isfile('myfile.txt')=}")
print(f"{os.path.isdir('myfile.txt')=}")
print(f"{os.path.getsize('myfile.txt')=}")          # bytes
print(f"{os.path.splitext('report.final.pdf')=}")   # ('report.final', '.pdf')
print(f"{os.path.basename(full)=}")

# Creating directories and files
os.makedirs(os.path.join("cave", "gadgets"), exist_ok=True)
os.makedirs(os.path.join("cave", "vehicles"), exist_ok=True)
open(os.path.join("cave", "notes.txt"), "w").close()               # empty file
open(os.path.join("cave", "gadgets", "batarang.txt"), "w").close()
open(os.path.join("cave", "gadgets", "grapple.pdf"), "w").close()
open(os.path.join("cave", "vehicles", "batmobile.txt"), "w").close()
print(f"{sorted(os.listdir('cave'))=}")

# Deleting
open("temp.txt", "w").close()
os.remove("temp.txt")
print(f"{os.path.exists('temp.txt')=}")

# Walking a directory tree
for dirname, subdirs, files in os.walk("cave"):
    print(f"Directory: {dirname:<16} Subdirs: {subdirs}  Files: {files}")

# Use case: find files by extension
for dirname, subdirs, files in os.walk("cave"):
    for name in files:
        if name.endswith(".txt"):
            print("Found:", os.path.join(dirname, name))

# Common mistakes
#   * Hardcoding "\\" or "/" in paths
#   * Single backslashes in Windows strings: "C:\new" -> "\n" is a newline!
#     Use "C:\\new" or a raw string r"C:\new"
#   * os.rmdir() on a non-empty directory -> OSError


# ==========================================================================
# PART 4: WORKING WITH BINARY DATA
# ==========================================================================
# Key ideas
#   * Images, videos, PDFs store raw BYTES, not readable text. A text editor
#     shows garbage because it interprets bytes as characters.
#   * A bytes object is an immutable sequence of byte values (0-255).
#       bytes("A text string", "ascii")  bytes(100)  bytes([12, 15, 20])
#       b"\x31\x32\x33"   -> \x + two hex digits = one byte
#   * Binary modes: "rb", "wb", "ab"
#       read()  returns bytes      write() expects bytes
#   * On Windows, binary mode prevents "\n" -> "\r\n" conversion, which
#     would corrupt binary data.
print("\n===== PART 4: Binary data =====")

b1 = bytes("A text string", "ascii")
b2 = bytes(100)
b3 = bytes([12, 15, 20])
print(f"{b1=}")
print(f"{len(b2)=}, {b2[:5]=}")
print(f"{b3=}")                   # values < 32 are shown as \x escapes
print(f"{b3[0]=}")                # indexing bytes gives an int
raw_bytes = b"\x31\x32\x33"
print(f"{raw_bytes=}")            # b'123' (0x31 is ASCII '1')

# Extra: str <-> bytes with encode()/decode()
print(f"{'Hi'.encode('ascii')=}, {b'Hi'.decode('ascii')=}")

# Write and read binary
file = open("data.bin", "wb")
file.write(bytes([0, 65, 66, 255]))
file.close()
# file.write("text")   # TypeError: a bytes-like object is required, not 'str'

file = open("data.bin", "rb")
data = file.read()
file.close()
print(f"{data=}, {type(data)=}, {list(data)=}")

# Real file: the first 4 bytes of every PDF are b'%PDF'
file = open("fake.pdf", "wb")
file.write(b"%PDF-1.7 ...")
file.close()
file = open("fake.pdf", "rb")
print(f"{file.read(4)=}")         # in binary mode, read(n) reads n BYTES
file.close()

# Common mistakes
#   * Opening images/PDFs in text mode -> UnicodeDecodeError or corrupted data
#   * Writing str to a binary file (or bytes to a text file) -> TypeError


# ==========================================================================
# PART 5: THE struct MODULE
# ==========================================================================
# Key ideas
#   * struct converts values <-> bytes.
#       struct.pack(format, v1, v2, ...)  -> bytes
#       struct.unpack(format, data)       -> ALWAYS a tuple
#   * Byte order:  "<" little-endian (least significant byte first)
#                  ">" big-endian    (most significant byte first)
#   * Format characters:
#       "b" 1-byte int (-128..127)   "h" 2-byte int   "I" 4-byte unsigned int
#       "s" bytes string - put the length before it: "4s" = 4 bytes
#   * struct.calcsize(format) -> number of bytes the format needs
print("\n===== PART 5: struct =====")

packed = struct.pack("<h", 1234)          # 1234 = 0x04D2
print(f"{packed=}")                       # b'\xd2\x04'  low byte first
print(f"{struct.pack('>h', 1234)=}")      # b'\x04\xd2'  high byte first
print(f"{struct.calcsize('<h')=}")

result = struct.unpack("<h", packed)
print(f"{result=}")                       # (1234,)  <- a tuple!
value = result[0]
print(f"{value=}")

# Multiple values
packed = struct.pack("<hh4s", 100, 200, b"text")
print(f"{packed=}, {len(packed)=}")
print(f"{struct.unpack('<hh4s', packed)=}")

# Careful: "s" without a count means ONE byte -> the string is truncated
print(f"{struct.pack('<hhs', 100, 200, b'text')=}")   # only b't' is kept

# Wrong byte order -> wrong value
print(f"{struct.unpack('>h', struct.pack('<h', 1234))=}")   # (-11772,)

# Round trip through a binary file: a small "record"
file = open("record.bin", "wb")
file.write(struct.pack("<I5sh", 42, b"Bruce", 37))
file.close()
file = open("record.bin", "rb")
record_id, name, age = struct.unpack("<I5sh", file.read())
file.close()
print(f"{record_id=}, {name=}, {age=}")

# Common mistakes
#   * Forgetting that unpack() returns a tuple -> use [0] or unpacking
#   * Mixing "<" and ">" between pack and unpack
#   * Using "s" instead of "4s" for a 4-byte string


# ==========================================================================
# PART 6: COMMAND-LINE ARGUMENTS
# ==========================================================================
# Key ideas
#   * Let the user choose the input file when running the program:
#         python myscript.py myfile1.txt
#   * sys.argv is a list of strings:
#         sys.argv[0] -> script name     sys.argv[1] -> first argument ...
#   * Always check len(sys.argv) before using an argument.
print("\n===== PART 6: Command-line arguments =====")

print(f"{sys.argv=}")
if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
    filename = sys.argv[1]
else:
    print("No valid filename provided -> using default 'myfile.txt'")
    filename = "myfile.txt"

file = open(filename)
print(f"{filename} has {len(file.readlines())} lines")
file.close()
# Try it from a terminal:  python file_io_lecture.py numbers.txt
# (the script works inside io_demo, so pass a file name from that folder)

# Common mistakes
#   * Accessing sys.argv[1] without checking len(sys.argv) -> IndexError
#   * Forgetting that arguments are strings: int(sys.argv[2]) for numbers


# ==========================================================================
# PART 7: THE with STATEMENT (BEST PRACTICE)
# ==========================================================================
# Key ideas
#   * with open(...) as f:  closes the file automatically at the end of the
#     block - even if an error occurs.
#   * It is a context manager:  1) set up (open)  2) use  3) tear down (close)
#   * Why it matters: an unclosed file may block other programs, lose
#     buffered data, and waste system resources.
#   * Several files in one statement: with open(a) as f1, open(b, "w") as f2:
print("\n===== PART 7: with statement =====")

with open("myfile.txt") as myfile:
    contents = myfile.read()
    print(f"inside:  {myfile.closed=}")
print(f"outside: {myfile.closed=}")

# Multiple files: read one, write an uppercase copy
with open("myfile.txt") as infile, open("upper.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())

with open("upper.txt") as f:
    print(f.read())

# Compare: the same task without `with` needs two close() calls
# infile = open("myfile.txt"); outfile = open("upper.txt", "w")
# outfile.write(infile.read().upper())
# infile.close(); outfile.close()

# From now on, use `with` for every file you open.


# ==========================================================================
# PART 8: WORKING WITH CSV FILES
# ==========================================================================
# Key ideas
#   * CSV = comma-separated values: each line is a row, commas separate
#     fields (columns), the first row is often a header.
#   * import csv
#       csv.reader(file)  -> iterate: each row is a LIST OF STRINGS
#       next(reader)      -> read (skip) the header row
#       csv.reader(file, delimiter=";")  -> other separators
#   * A field containing a comma: use another delimiter or quotes:
#       Little, Petr;9;8;85;78        or     "Little, Petr",9,8,85,78
#   * Fields are strings -> convert with int()/float() before math.
#   * csv.writer(file): writerow(list), writerows(list_of_lists)
#   * Open CSV files for writing with newline="" (avoids blank lines on Windows).
print("\n===== PART 8: CSV files =====")

with open("students.csv", "w") as f:
    f.write("name,hw1,hw2,midterm,final\n"
            "Petr Little,9,8,85,78\n"
            "Sam Tarley,10,9,90,92\n"
            "Joff King,4,5,60,55\n")

# Reading: each row is a list of strings
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Accessing specific fields + converting + skipping the header
with open("students.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"{header=}")
    for row in reader:
        name = row[0]
        hw1 = int(row[1])
        hw2 = int(row[2])
        midterm = int(row[3])
        final = int(row[4])
        average = (hw1 + hw2 + midterm + final) / 4
        print(f"{name:<12} Average = {average:6.2f}")

# Different delimiter
with open("students_semicolon.csv", "w") as f:
    f.write("name;hw1;final\nLittle, Petr;9;78\n")
with open("students_semicolon.csv") as file:
    for row in csv.reader(file, delimiter=";"):
        print(row)

# Quoted field: csv handles it, a plain split(",") does not
line = '"Little, Petr",9,8,85,78'
print(f"{line.split(',')=}")                 # wrong: 6 pieces
print(f"{next(csv.reader([line]))=}")        # right: 5 fields

# Writing CSV
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score", "grade"])
    writer.writerows([
        ["Alice", 95, "A"],                  # numbers are converted for you
        ["Bob", 87, "B"],
        ["Wayne, Bruce", 92, "A"],           # comma -> quoted automatically
    ])

with open("output.csv") as f:
    print(f.read())

# Common mistakes
#   * Doing math on strings          * Forgetting to skip the header
#   * Using line.split(",") on files with quoted fields
#   * Missing newline="" when writing -> blank lines between rows on Windows


# ==========================================================================
# RECAP
# ==========================================================================
#  READ     with open("f.txt") as f:      f.read() | f.readlines() | f.readline()
#                                         for line in f: line.strip()
#  WRITE    with open("f.txt", "w") as f: f.write("text\n"); f.write(str(123))
#  MODES    "r" read | "w" overwrite | "a" append | "+" update | "b" binary
#  BUFFER   f.flush() forces data to disk; close() flushes automatically
#  PATHS    os.path.join("a", "b.txt")   os.path.sep   os.path.exists/isfile/
#           isdir/getsize/splitext       os.walk(top) -> (dirname, subdirs, files)
#  BINARY   open(p, "rb"/"wb") -> bytes; bytes([1, 2]); b"\x41"
#  STRUCT   struct.pack("<h", 1234) -> bytes; struct.unpack(fmt, data) -> tuple
#  ARGS     sys.argv[0] script name, sys.argv[1:] arguments (strings)
#  WITH     closes files automatically - always use it
#  CSV      csv.reader(f) -> rows as lists of str; next(reader) skips header
#           csv.writer(f).writerow([...]) / writerows([[...], ...]); newline=""
