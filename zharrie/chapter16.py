"""
==============================================================================
 CHAPTER 16 - SEARCHING & SORTING ALGORITHMS
==============================================================================
   16.1 Linear search          16.6 Selection sort
   16.2 Binary search          16.7 Insertion sort
   16.3 Big O notation         16.8 Quicksort
   16.4 Algorithm analysis     16.9 Merge sort
   16.5 Sorting: introduction  Which algorithm when?
==============================================================================
"""
import random
import time


# =============================================================================
# 16.1  SEARCHING AND ALGORITHMS - LINEAR SEARCH
# =============================================================================
# ALGORITHM = a sequence of steps for accomplishing a task.
# SEARCHING = finding WHERE a value (the "search key") is in a list.
#
# LINEAR SEARCH
#   What     Check the elements one by one, from first to last, until the key
#            is found (return its index) or the list ends (return -1).
#   Analogy  Looking for your keys by checking every pocket, one at a time.
#   Use when the list is NOT sorted, is small, or is searched only once;
#            or you search by a condition ("first score below 60").
#   Avoid    a big list that is searched many times -> sort it once and use
#            binary search.
#   Used in  Python's  `x in my_list`,  my_list.index(x),  my_list.count(x)
#   Cost     best O(1) (key is first)   worst O(N) (key is last or missing)
#            -> a list of N elements needs at most N comparisons

def linear_search(numbers, key, show=False):
    for i in range(len(numbers)):
        if show:                                    # show=True prints each step
            print(f"  i={i}: is {numbers[i]} == {key}?")
        if numbers[i] == key:
            return i
    return -1  # not found


# EXAMPLE 1 - work it by hand first:  find 7 in [5, 2, 9, 7, 1]
#   5? no  ->  2? no  ->  9? no  ->  7? YES  => index 3, after 4 comparisons
print("Find 7  ->", linear_search([5, 2, 9, 7, 1], 7, show=True))

# EXAMPLE 2 - key NOT in the list: every element gets compared (Animation 16.1.1)
print("Find 11 ->", linear_search([6, 24, 16, 14, 5, 32, 63, 2], 11, show=True))

numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print("NUMBERS:", numbers)
for key in [10, 17]:
    key_index = linear_search(numbers, key)
    if key_index == -1:
        print(f"{key} was not found.")              # 17 was not found.
    else:
        print(f"Found {key} at index {key_index}.") # Found 10 at index 3.

# EXAMPLE - real world: an UNSORTED gradebook. Linear search is the right tool,
#   because the list isn't sorted and we search by a CONDITION, not one key.
gradebook = [("Maya", 91), ("Leo", 58), ("Ava", 74), ("Sam", 49), ("Noor", 88)]
for i in range(len(gradebook)):
    if gradebook[i][1] < 60:
        print("First student below 60:", gradebook[i], "at index", i)   # ('Leo', 58) at 1
        break

# RUNTIME - if one comparison takes 1 µs, the worst case for linear search is:
#   1 million items -> 1 s      10 million -> 10 s
#   Amazon, 200 million items -> 200 s = more than 3 minutes per search!


# =============================================================================
# 16.2  BINARY SEARCH
# =============================================================================
#   What     Search a SORTED list by checking the MIDDLE element and throwing
#            away the half that cannot contain the key. Repeat on what's left.
#   Analogy  A paper dictionary: open it in the middle, ask "before or after?",
#            and never look at the other half again.
#   How      low = 0, high = last index
#            while high >= low:
#                mid = (high + low) // 2
#                numbers[mid] == key -> found, return mid
#                numbers[mid] <  key -> key is on the RIGHT: low  = mid + 1
#                numbers[mid] >  key -> key is on the LEFT:  high = mid - 1
#            the window is empty -> return -1
#   Why fast Every check HALVES the search space: 32 -> 16 -> 8 -> 4 -> 2 -> 1 -> 0
#            Max steps for N elements = floor(log2 N) + 1   (1 million -> 20 steps)
#   Use when the data is sorted (or sorted once, then searched many times);
#            "find the boundary" problems (first bad version, guess a number).
#   Avoid    unsorted data that is searched only once.
#   Used in  phone contacts, dictionaries, database indexes
#   Cost     best O(1)   worst O(log N)


def binary_search(numbers, key, show=False):
    low = 0
    high = len(numbers) - 1
    while high >= low:
        mid = (high + low) // 2
        if show:
            print(f"  low={low} high={high} mid={mid} -> checking {numbers[mid]}")
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1  # not found


# EXAMPLE 1 - by hand first:  find 45 in [2, 4, 7, 10, 11, 32, 45, 87]
#   mid=3 -> 10 < 45, go right  |  mid=5 -> 32 < 45, go right  |  mid=6 -> 45 FOUND
#   3 checks (linear search would need 7)
print("Find 45 ->", binary_search([2, 4, 7, 10, 11, 32, 45, 87], 45, show=True))

# EXAMPLE 2 - the book's program: same main program, new search
for key in [10, 17]:
    key_index = binary_search(numbers, key)
    print(f"{key} was not found." if key_index == -1 else f"Found {key} at index {key_index}.")

# CLASS EXERCISES - predict the midpoints and result before running the code

# EXERCISE 1 - an exact match near the end
#   For [3, 8, 12, 20, 26, 38, 42, 57, 61], find 57.
#   1. What index is checked first?
#   2. Which direction should the search move?
#   3. How many elements are checked?
print("Exercise 1 - Find 57")
print("index:", binary_search([3, 8, 12, 20, 26, 38, 42, 57, 61], 57, show=True))

# EXERCISE 2 - a key that is not present
#   For [10, 15, 22, 29, 33, 40, 48], find 36.
#   1. Predict the sequence of mid indices.
#   2. What result should binary_search return?
#   3. Which sorted-list condition should hold after the search stops?
print("Exercise 2 - Find 36")
print("index:", binary_search([10, 15, 22, 29, 33, 40, 48], 36, show=True))

# EXERCISE 3 - the first repeated value
#   For [1, 3, 3, 3, 3, 5, 8], find 3.
#   Ordinary binary search finds an occurrence, but it may not find index 1.
#   By hand, decide how to continue LEFT after each match.
#   After that, use the starter below to implement first_occurrence.
def first_occurrence(numbers, key):
    low = 0
    high = len(numbers) - 1
    result = -1
    while high >= low:
        mid = (high + low) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            result = mid
            # TODO: keep searching LEFT instead of stopping here
            break
    return result

print("Exercise 3 - First occurrence of 3:", first_occurrence([1, 3, 3, 3, 3, 5, 8], 3))

# EFFICIENCY 
# Binary search doubles the amount of data but adds only roughly one comparison because 
# it eliminates half the remaining elements each time:
# 1 million items -> about log₂(1,000,000) + 1 -> 20 comparisons
# 2 million items -> about 21 comparisons
# 4 million items -> about 22 comparisons
# 200 million items -> about 28 comparisons

# Therefore, searching 200 million items takes approximately:

# 28 comparisons × 1 µs/comparison = 28 µs

# A linear search could check all 200 million items:

# 200,000,000 comparisons × 1 µs/comparison
# = 200,000,000 µs
# = 200 seconds

# The comparison is:

# 200 seconds / 28 microseconds
# ≈ 7.1 million times faster

# This is a worst-case comparison: binary search is fast here, while linear search must examine every item.

# “Doubling data adds only one step” is not always exact due to specific element counts, but it follows the logarithmic pattern:

# Doubling N: log₂(2N) = log₂(N) + 1

# So every doubling can add approximately one additional comparison.

# COMMON MISTAKES
#   * List not sorted -> wrong answer:
print("Unsorted list, find 9 ->", binary_search([9, 2, 7, 4, 1], 9), "(9 IS there, at index 0!)")
#   * mid = (high + low) / 2  -> a float -> TypeError. Use // .
#   * while high > low  -> misses the last 1-element window. Use >= .
#   * low = mid instead of mid + 1 -> can loop forever.


# =============================================================================
# 16.3  BIG O NOTATION
# =============================================================================
#   What     A way to describe how an algorithm's runtime GROWS as the input
#            size N grows. It ignores the computer's speed and small details.
#   Why      "It takes 2 seconds" depends on the machine.
#            "It is O(N^2)" means: double the data -> 4x the time, on ANY machine.
#   Analogy  Handing back tests: calling each student once grows like N;
#            comparing every PAIR of students grows like N^2.
#   How      1. Write the number of steps as a function f(N)
#            2. Rule 1: keep only the highest-order (fastest-growing) term
#            3. Rule 2: drop constant factors
#            f(N) = 5 + 13N + 7N^2  ->  7N^2  ->  O(N^2)   "Oh N squared"
#   Composite rules (c = a constant):
#            c * O(f) = O(f)          c + O(f) = O(f)
#            g * O(f) = O(g * f)      g + O(f) = O(g + f)
#   Common growth rates, fastest to slowest:
#            O(1)        constant      find_min(x, y)
#            O(log N)    logarithmic   binary search
#            O(N)        linear        linear search
#            O(N log N)  log-linear    merge sort, quicksort (typical)
#            O(N^2)      quadratic     selection sort, insertion sort
#            O(c^N)      exponential   recursive fibonacci

# EXAMPLE 1 - why Rule 1 works: as N grows, the 7N^2 term is almost all of f(N)
for n in [1, 10, 100, 1000]:
    f = 5 + 13 * n + 7 * n * n
    print(f"N={n:<5} f(N)={f:<10,} 7N^2 is {7 * n * n / f:.0%} of it")

# EXAMPLE 2 - growth rates side by side: number of steps for each function
#   Book Table 16.3.1 (1 µs per step): N^2 at N=100,000 -> 2.7 hours;
#   N^3 at N=10,000 -> 11.57 days; 2^N at N=50 -> 35.7 years.
print(f"{'N':>6} {'log2 N':>7} {'N':>7} {'N log2 N':>10} {'N^2':>12} {'2^N':>10}")
for n in [10, 20, 50, 100]:
    log_n = n.bit_length() - 1                       # whole-number log2
    print(f"{n:>6} {log_n:>7} {n:>7} {n * log_n:>10} {n * n:>12,} {2 ** n:>10.1e}")

# EXAMPLE 3 - exponential growth: count the calls made by recursive fibonacci
fib_calls = 0


def fibonacci(N):                       # book's O(c^N) example
    global fib_calls
    fib_calls += 1
    if (1 == N) or (2 == N):
        return N
    return fibonacci(N - 1) + fibonacci(N - 2)


for n in [10, 15, 20, 25]:
    fib_calls = 0
    fibonacci(n)
    print(f"fibonacci({n}) makes {fib_calls:,} calls")   # 109 / 1,219 / 13,529 / 150,049

# EXAMPLE 4 - real world: "will my program scale?"
#   A report takes 2 s for 10,000 records. With 100,000 records (10x more):
#     O(N)     -> 20 s        O(N^2) -> 200 s (100x slower!)
#
# PREDICT (16.3.2)  O(N + 9999) = O(N)    O(734N) = O(N)    O(12N^2 + 6N + 1000) = O(N^2)
# PREDICT (16.3.3)  10*O(N^2) = O(N^2)    10 + O(N^2) = O(N^2)    3N*O(N^2) = O(N^3)
#                   2N^3 + O(N^2) = O(N^3)    log2 N = O(log N)
# PREDICT (16.3.5)  O(5): constant    O(N log N): log-linear    O(N + N^2): quadratic
#                   linear search: O(N)    selection sort: O(N^2)


# =============================================================================
# 16.4  ALGORITHM ANALYSIS
# =============================================================================
#   What     Finding an algorithm's Big O by COUNTING the operations it runs.
#   Which case?  WORST case (the slowest input) is the default: it's a guarantee.
#            Best case = luckiest input. Average case needs knowledge of typical data.
#   How      1. Count operations: assignment, comparison, + ... = 1 each
#            2. Multiply by how many times each loop runs
#            3. Add up -> f(N) -> take Big O
#   Example  max_val = numbers[0]        1 operation
#            for num in numbers:         N iterations, each: num = ... (1)
#                if num > max_val:           compare (1)
#                    max_val = num           assign (1, worst case)
#            f(N) = 1 + N(1 + 2) = 1 + 3N  ->  O(N)
#   Shortcuts
#            * any FIXED number of simple statements          -> O(1)
#            * one loop over N items, O(1) work inside        -> O(N)
#            * a loop over N inside a loop over N             -> O(N^2)
#            * a loop that halves N each time                 -> O(log N)
#            * nested loops in general: ADD UP the inner loop's work:
#              selection sort: (N-1) + (N-2) + ... + 1 = N(N-1)/2 -> O(N^2)

# EXAMPLE 1 - count nested-loop work, then DOUBLE N and see what happens
for n in [100, 200]:
    count = 0
    for i in range(n):
        for j in range(i + 1, n):       # selection sort's loop shape
            count += 1
    print(f"N={n}: inner loop runs {count:,} times  (N(N-1)/2 = {n * (n - 1) // 2:,})")
#   N doubles -> work x4  => quadratic, O(N^2)

# EXAMPLE 2 - the halving loop: steps grow by only 1 when N doubles -> O(log N)
for n in [8, 16, 1024]:
    n_val, steps = n, 0
    while n_val > 0:
        n_val = n_val // 2
        steps = steps + 1
    print(f"N={n}: {steps} steps")      # 4, 5, 11

# EXAMPLE 3 - real world: two ways to check for a duplicate student ID.
#   A) compare every pair (nested loops)        -> O(N^2)
#   B) sort first, then compare neighbours only -> O(N log N) + O(N) = O(N log N)
def has_duplicate_pairs(ids):
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if ids[i] == ids[j]:
                return True
    return False


def has_duplicate_sorted(ids):
    ordered = sorted(ids)
    for i in range(len(ordered) - 1):
        if ordered[i] == ordered[i + 1]:
            return True
    return False


for n in [1000, 2000, 4000]:
    ids = random.sample(range(10_000_000), n)    # no duplicates = worst case
    start = time.perf_counter()
    has_duplicate_pairs(ids)
    a = time.perf_counter() - start
    start = time.perf_counter()
    has_duplicate_sorted(ids)
    b = time.perf_counter() - start
    print(f"N={n}: A {a * 1000:6.1f} ms   B {b * 1000:5.2f} ms")
#   A grows ~4x each time N doubles; B hardly changes. The analysis predicted it.

# PREDICT (16.4.2)  sum loop: f(N) = 2N + 1    count negatives: O(N)
#                   loop with if i % 2 == 0: O(N)    halving loop: O(log N)
#                   loop that may stop at the first element, BEST case: O(1)
# PREDICT (16.4.4)  all True: a simple for loop is O(N); an if/elif toll chain is
#                   O(1); a loop of exactly 24 iterations is O(1) (24 is a constant)
# PREDICT (16.4.6)  1) N x N: O(N^2)  2) N x (N-1): O(N^2)  3) N/2 x N/2: O(N^2)
#                   4) j from i to N-1: O(N^2)  5) three nested loops: O(N^3)


# =============================================================================
# 16.5  SORTING: INTRODUCTION
# =============================================================================
#   What     Rearranging elements into ascending (or descending) order:
#            [17, 3, 44, 6, 9]  ->  [3, 6, 9, 17, 44]
#   Why sort?
#            * it enables binary search: O(log N) instead of O(N)
#            * duplicates end up next to each other
#            * ranking: top 10, leaderboards, median, min/max
#            * readable output: alphabetical rosters, dates in order
#   How      A program can't "see" the whole list. It compares TWO elements at a
#            time and SWAPS them when they are in the wrong order. Each sorting
#            algorithm is a different plan for which pairs to compare.
#   Terms    in place = sorts inside the same list (no copy)
#            stable   = equal items keep their original order
#   Python   my_list.sort()  sorts in place, returns None
#            sorted(my_list) returns a NEW sorted list
print("\n" + "=" * 70 + "\n16.5  SORTING: INTRODUCTION\n" + "=" * 70)

# EXAMPLE 1 - the basic move of every sort: swapping two values
a, b = 3, 9
temp = a            # book style: use a temporary variable
a = b
b = temp
print("after swap:", a, b)              # 9 3
a, b = b, a         # Python shortcut, same result
print("swap again:", a, b)              # 3 9

# EXAMPLE 2 - real world: what sorting makes easy
scores = [72, 95, 88, 61, 95, 79, 84, 58, 90]
ordered = sorted(scores)
print("sorted:", ordered)
print("top 3: ", sorted(scores, reverse=True)[:3])          # [95, 95, 90]
print("median:", ordered[len(ordered) // 2])                # 84
print("index of 84 by binary search:", binary_search(ordered, 84))

# PREDICT (16.5.2)  [3, 9, 44, 18, 76] ascending? False
#   [20, 15, 10, 5, 0] descending? True     [99.87, 99.02, 67.93, 44.10] descending? True
#   ["F", "D", "C", "B", "A"] descending? True
#   ["chopsticks", "forks", "knives", "spork"] ascending? True
#   ["great", "greater", "greatest"] ascending? True (a shorter prefix comes first)

# COMMON MISTAKES
#   * scores = scores.sort()  -> scores becomes None (sort() returns None)
#   * uppercase sorts before lowercase:
print(sorted(["banana", "apple", "Cherry"]))                # ['Cherry', 'apple', 'banana']


# =============================================================================
# 16.6  SELECTION SORT
# =============================================================================
#   What     Split the list into a SORTED part (left) and an UNSORTED part
#            (right). Repeatedly SELECT the smallest unsorted value and swap it
#            to position i, the end of the sorted part.
#   Analogy  Lining students up by height: find the shortest, send them to the
#            front; find the shortest of the rest, send them next; and so on.
#   How      for i in range(len(numbers) - 1):     # i = dividing point
#                index_smallest = index of the smallest value from i onward
#                swap numbers[i] and numbers[index_smallest]
#   Use when small lists; simple code; swaps are expensive (at most N-1 swaps)
#   Avoid    large lists; nearly sorted data (it can't take advantage of it)
#   Cost     ALWAYS O(N^2): N-1 passes x about N/2 comparisons each
#            (best case = worst case)    in place
print("\n" + "=" * 70 + "\n16.6  SELECTION SORT\n" + "=" * 70)


def selection_sort(numbers, show=False):            # Figure 16.6.1
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        if show:
            print(f"  i={i}: selected {numbers[i]:<3} -> {numbers[:i + 1]} | {numbers[i + 1:]}")


# EXAMPLE 1 - by hand first:  [29, 10, 14, 37, 13]
#   i=0 smallest 10 -> [10] | [29, 14, 37, 13]
#   i=1 smallest 13 -> [10, 13] | [14, 37, 29]
#   i=2 smallest 14 -> [10, 13, 14] | [37, 29]
#   i=3 smallest 29 -> [10, 13, 14, 29] | [37]        done
selection_sort([29, 10, 14, 37, 13], show=True)

# EXAMPLE 2 - the book's program (Figure 16.6.1)
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print("UNSORTED:", numbers)
selection_sort(numbers)
print("SORTED:  ", numbers)             # [2, 4, 7, 10, 11, 32, 45, 78]

# EXAMPLE 3 - real world: 100 m race results -> podium.
#   Each pass "selects" the next fastest runner. We swap the names too,
#   so each name stays with its time.
times = [12.41, 11.87, 12.05, 11.62, 12.90, 11.95]
runners = ["Ana", "Ben", "Cai", "Dee", "Eli", "Fay"]
for i in range(len(times) - 1):
    index_smallest = i
    for j in range(i + 1, len(times)):
        if times[j] < times[index_smallest]:
            index_smallest = j
    times[i], times[index_smallest] = times[index_smallest], times[i]
    runners[i], runners[index_smallest] = runners[index_smallest], runners[i]
print("Gold:", runners[0], times[0], "| Silver:", runners[1], times[1], "| Bronze:", runners[2], times[2])

# PREDICT (16.6.2)  [9, 8, 7, 6, 5]: value at index 0 after pass i=0?  A: 5
#                   swaps during that pass?  A: 1 (one swap per pass)
#                   [5, 9, 8, 7, 6] after pass i=1?  A: [5, 6, 8, 7, 9]
# PREDICT (16.6.3)  50 elements: index_smallest assigned at least ___ times?  A: 49
#                   20 vs 10 elements: x4 longer.  500 vs 50: x100 longer (O(N^2))
# COMMON MISTAKES   swapping INSIDE the inner loop; starting the inner loop at 0
#                   instead of i + 1.


# =============================================================================
# 16.7  INSERTION SORT
# =============================================================================
#   What     Split into SORTED (left) and UNSORTED (right). Take the next unsorted
#            value and INSERT it into its correct place in the sorted part by
#            swapping it to the left while it is smaller than its neighbour.
#   Analogy  Sorting playing cards in your hand: pick up the next card and
#            slide it left until it fits.
#   How      for i in range(1, len(numbers)):     # element 0 counts as sorted
#                j = i
#                while j > 0 and numbers[j] < numbers[j - 1]:
#                    swap numbers[j] and numbers[j - 1];  j = j - 1
#   Use when small lists; data that is SORTED or NEARLY sorted; items that
#            arrive one at a time and the list must stay sorted.
#   Avoid    large, randomly ordered lists
#   Used in  Python's built-in sort uses insertion sort for small pieces
#   Cost     best O(N) (already sorted)   typical/worst O(N^2)   in place, stable
print("\n" + "=" * 70 + "\n16.7  INSERTION SORT\n" + "=" * 70)


def insertion_sort(numbers, show=False):            # Figure 16.7.1
    comparisons = 0                     # added: counts comparisons, so we can see O(N)
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part, stopping once it is in position
        while j > 0 and numbers[j] < numbers[j - 1]:
            comparisons += 1
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j = j - 1
        if j > 0:
            comparisons += 1            # the comparison that stopped the loop
        if show:
            print(f"  i={i}: inserted {numbers[j]:<3} -> {numbers[:i + 1]} | {numbers[i + 1:]}")
    return comparisons


# EXAMPLE 1 - by hand first:  [29, 10, 14, 37, 13]
#   i=1 insert 10 -> [10, 29] | [14, 37, 13]
#   i=2 insert 14 -> [10, 14, 29] | [37, 13]
#   i=3 insert 37 -> [10, 14, 29, 37] | [13]     (1 comparison: already fits)
#   i=4 insert 13 -> [10, 13, 14, 29, 37]        done
insertion_sort([29, 10, 14, 37, 13], show=True)

# EXAMPLE 2 - the book's program (Figure 16.7.1)
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
insertion_sort(numbers)
print("SORTED:", numbers)

# EXAMPLE 3 - nearly sorted input is FAST: an element already in place costs 1
#   comparison. With only C elements out of place: O((N - C) * 1 + C * N) = O(N)
nearly = list(range(1000))
nearly[500], nearly[700] = nearly[700], nearly[500]
print("N=1000 sorted:       ", insertion_sort(list(range(1000))), "comparisons")
print("N=1000 nearly sorted:", insertion_sort(nearly), "comparisons")
print("N=1000 reversed:     ", insertion_sort(list(range(1000, 0, -1))), "comparisons")

# EXAMPLE 4 - real world: a live leaderboard. Scores arrive one at a time; each
#   new score is appended and slides left into place (highest first).
leaderboard = []
for new_score in [420, 380, 510, 395, 600, 450]:
    leaderboard.append(new_score)
    j = len(leaderboard) - 1
    while j > 0 and leaderboard[j] > leaderboard[j - 1]:
        leaderboard[j], leaderboard[j - 1] = leaderboard[j - 1], leaderboard[j]
        j -= 1
    print(f"  new score {new_score}: {leaderboard}")

# PREDICT (16.7.2)  [20, 14, 85, 3, 9]: index 0 after pass i=1?  A: 14
#                   [10, 20, 6, 14, 7] after pass i=2?  A: [6, 10, 20, 14, 7]
#                   [1, 9, 17, 18, 2]: swaps in pass i=4?  A: 3
# PREDICT (16.7.3)  worst case, 10 elements, 1 µs each?  A: 45 µs (10*9/2)
#                   20 vs 10 elements: x4 longer
# PREDICT (16.7.4)  [6, 14, 85, 102, 102, 151] sorted
#                   [23, 24, 36, 48, 19, 50, 101] nearly sorted (only 19 is out of place)
#                   [15, 19, 21, 24, 2, 3, 6, 11] unsorted
# PREDICT (16.7.6)  [10..15]: comparisons in pass i=3?  A: 1
#                   [10, 11, 12, 13, 14, 7]: comparisons in pass i=5?  A: 5
# COMMON MISTAKE    write  j > 0 and ...  FIRST, so numbers[j - 1] is never
#                   checked when j is 0.


# =============================================================================
# 16.8  QUICKSORT
# =============================================================================
#   What     Divide and conquer. Pick a PIVOT (the book uses the middle value),
#            PARTITION the list into a low part (<= pivot) and a high part
#            (>= pivot), then quicksort each part recursively. The parts are
#            NOT sorted after partitioning; recursion finishes the job.
#   Analogy  A teacher sorting a class by height: "shorter than Sam go left,
#            taller go right", then repeats the trick inside each group.
#   How      partition(numbers, i, k):
#                pivot = numbers[i + (k - i) // 2]
#                l moves right while numbers[l] < pivot
#                h moves left  while pivot < numbers[h]
#                swap numbers[l] and numbers[h]; repeat until l >= h; return h
#            quicksort(numbers, i, k):
#                if i >= k: return               # 0 or 1 element: sorted
#                j = partition(numbers, i, k)    # j = last index of low part
#                quicksort(numbers, i, j)  and  quicksort(numbers, j + 1, k)
#   Use when general-purpose sorting in memory (usually fastest in practice);
#            memory is tight (sorts in place, no temporary list)
#   Avoid    when you need a guaranteed worst case, or a stable sort
#   Cost     typical O(N log N): log N levels x N comparisons per level
#            worst O(N^2): pivot always the smallest/largest -> N-1 levels (rare)
print("\n" + "=" * 70 + "\n16.8  QUICKSORT\n" + "=" * 70)


def partition(numbers, i, k):                       # Figure 16.8.1
    # Pick middle element as pivot
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]
    done = False
    l = i
    h = k
    while not done:
        # Increment l while numbers[l] < pivot
        while numbers[l] < pivot:
            l = l + 1
        # Decrement h while pivot < numbers[h]
        while pivot < numbers[h]:
            h = h - 1
        # Zero or one items remaining: all numbers are partitioned. Return h
        if l >= h:
            done = True
        else:
            # Swap numbers[l] and numbers[h], update l and h
            temp = numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp
            l = l + 1
            h = h - 1
    return h


def quicksort(numbers, i, k, show=False):           # Figure 16.8.1
    # Base case: one or zero entries, partition is already sorted
    if i >= k:
        return
    if show:
        before, pivot = numbers[i:k + 1], numbers[i + (k - i) // 2]
    # j = location of the last item in the low partition
    j = partition(numbers, i, k)
    if show:
        print(f"  {before} pivot {pivot} -> low {numbers[i:j + 1]} | high {numbers[j + 1:k + 1]}")
    # Recursively sort low partition (i to j) and high partition (j + 1 to k)
    quicksort(numbers, i, j, show)
    quicksort(numbers, j + 1, k, show)


# EXAMPLE 1 - one partition step (from the book): [4, 34, 10, 25, 1], pivot = 10
nums = [4, 34, 10, 25, 1]
h = partition(nums, 0, 4)
print("after partition:", nums, "-> low", nums[:h + 1], "| high", nums[h + 1:])
#   low [4, 1, 10] (all <= 10) | high [25, 34] (all >= 10). Not sorted yet!

# EXAMPLE 2 - by hand first:  [6, 9, 4, 1, 8]
#   [6, 9, 4, 1, 8] pivot 4 -> low [1, 4] | high [9, 6, 8]
#   [1, 4]          pivot 1 -> low [1]    | high [4]
#   [9, 6, 8]       pivot 6 -> low [6]    | high [9, 8]
#   [9, 8]          pivot 9 -> low [8]    | high [9]        result [1, 4, 6, 8, 9]
nums = [6, 9, 4, 1, 8]
quicksort(nums, 0, len(nums) - 1, show=True)
print("sorted:", nums)

# EXAMPLE 3 - the book's program (Figure 16.8.1)
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
quicksort(numbers, 0, len(numbers) - 1)
print("SORTED:", numbers)

# EXAMPLE 4 - real world: the median home price (sort, then take the middle)
prices = [315_000, 289_900, 450_000, 199_500, 375_250, 520_000, 260_000, 410_000, 335_000]
quicksort(prices, 0, len(prices) - 1)
print("median price:", prices[len(prices) // 2])          # 335000

# PREDICT (16.8.2)  midpoint, pivot:
#   [1, 2, 3, 4, 5], i=0, k=4 -> 2, 3        [200, 11, 38, 9], i=0, k=3 -> 1, 11
#   [55, 7, 81, 26, 0, 34, 68, 125], i=3, k=7 -> 5, 34
# PREDICT (16.8.3)  a partition is correct if every value in low <= pivot and
#   every value in high >= pivot.  e.g. pivot 35: [1, 4, 35] | [62, 98] -> True
#   pivot 65: [29, 17, 65] | [39, 84] -> False (39 < 65 is in the high part)
# PREDICT (16.8.6)  equal halves: 8 elements -> 3 levels, 1024 -> 10 levels
# PREDICT (16.8.7)  pivot always the SMALLEST: [7, 4, 2, 25, 19] low partition = [2]
#   5 elements -> 4 levels, 1024 -> 1023 levels => O(N^2)
# COMMON MISTAKES   midpoint = (k - i) // 2 forgets "+ i";
#                   recursing on (i, j - 1) loses element j; no base case -> RecursionError


# ============================================================================
# 16.9  MERGE SORT
# =============================================================================
#   What     Divide and conquer. Split the list in half, merge sort each half
#            recursively, then MERGE the two sorted halves into one sorted list.
#            A list of 1 element is already sorted (the base case).
#   Analogy  Two piles of exams, each already sorted by name. To combine them,
#            compare the top exam of each pile and take the one that comes
#            first. Repeat until both piles are used up.
#   How      merge_sort(numbers, i, k):
#                if i < k:
#                    j = (i + k) // 2                 # midpoint
#                    merge_sort(numbers, i, j)        # left half  i..j
#                    merge_sort(numbers, j + 1, k)    # right half j+1..k
#                    merge(numbers, i, j, k)          # combine
#            merge: take the smaller front element (<=) into a temporary list;
#            when one side is empty, copy the rest; copy back into numbers.
#   Use when you need a GUARANTEED O(N log N); a STABLE sort; data too big for
#            memory (sort chunks, then merge them); combining sorted lists.
#   Avoid    memory is tight: it needs O(N) extra space for the temporary list
#   Used in  Python's sort() and sorted() are based on merge sort (Timsort)
#   Cost     best = typical = worst = O(N log N): log N levels x N per level
print("\n" + "=" * 70 + "\n16.9  MERGE SORT\n" + "=" * 70)


def merge(numbers, i, j, k, show=False):            # Figure 16.9.1
    merged_size = k - i + 1                  # Size of merged partition
    merged_numbers = [0] * merged_size       # Temporary list for merged numbers
    merge_pos = 0                            # Position to insert merged number
    left_pos = i                             # Initialize left partition position
    right_pos = j + 1                        # Initialize right partition position
    # Add smallest element from left or right partition to merged numbers
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            if show:
                print(f"  {numbers[left_pos]} <= {numbers[right_pos]} -> take {numbers[left_pos]}")
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            if show:
                print(f"  {numbers[left_pos]} > {numbers[right_pos]} -> take {numbers[right_pos]}")
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    if show:
        print(f"  one side is empty -> copy the rest: {numbers[left_pos:j + 1] + numbers[right_pos:k + 1]}")
    # If left partition is not empty, add remaining elements to merged numbers
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1
    # If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    # Copy merged numbers back to numbers
    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]


def merge_sort(numbers, i, k, show=False):          # Figure 16.9.1
    if i < k:
        j = (i + k) // 2                     # Find the midpoint in the partition
        if show:
            print(f"  split {numbers[i:k + 1]} -> {numbers[i:j + 1]} {numbers[j + 1:k + 1]}")
        # Recursively sort left and right partitions
        merge_sort(numbers, i, j, show)
        merge_sort(numbers, j + 1, k, show)
        # Merge left and right partition in sorted order
        merge(numbers, i, j, k)
        if show:
            print(f"  merge -> {numbers[i:k + 1]}")


# EXAMPLE 1 - by hand first:  [38, 27, 43, 3]
#   split [38, 27, 43, 3] -> [38, 27] [43, 3] -> [38] [27] and [43] [3]
#   merge [38] + [27] -> [27, 38];  [43] + [3] -> [3, 43]
#   merge [27, 38] + [3, 43] -> [3, 27, 38, 43]
nums = [38, 27, 43, 3]
merge_sort(nums, 0, len(nums) - 1, show=True)

# EXAMPLE 2 - one merge step (Animation 16.9.3): left [3, 8, 11], right [4, 18, 25]
#   3 vs 4 -> 3 | 8 vs 4 -> 4 | 8 vs 18 -> 8 | 11 vs 18 -> 11 | left empty -> 18, 25
nums = [3, 8, 11, 4, 18, 25]
merge(nums, 0, 2, 5, show=True)
print("merged:", nums)

# EXAMPLE 3 - the book's program (Figure 16.9.1)
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
merge_sort(numbers, 0, len(numbers) - 1)
print("SORTED:", numbers)

# EXAMPLE 4 - real world: combine two sorted class rosters. The halves are
#   already sorted, so only the MERGE step is needed: one pass, O(N).
roster = ["Ava", "Diego", "Maya", "Sam"] + ["Ben", "Chloe", "Noor", "Zoe"]
merge(roster, 0, 3, 7)
print("combined roster:", roster)

# PREDICT (16.9.2)  [1, 2, 3, 4, 5], i=0, k=4 -> j=2, left [1, 2, 3], right [4, 5]
#                   [34, 78, 14, 23, 8, 35], i=3, k=5 -> j=4, left [23, 8], right [35]
# PREDICT (16.9.4)  merge [14, 18, 35 | 17, 38, 49]: values added in order
#                   14, 17, 18, 35, 38, 49   (run it below to check)
# PREDICT (16.9.5)  8 elements -> 3 levels; 2048 -> 11 levels;
#                   merging two partitions of 250 -> temporary list of 500
merge([14, 18, 35, 17, 38, 49], 0, 2, 5, show=True)
# COMMON MISTAKES   j = (i + k) / 2 is a float -> use //;  forgetting to copy the
#                   temporary list back;  using < instead of <= makes it unstable.


# =============================================================================
# WHICH ALGORITHM WHEN?  + a race
# =============================================================================
#   SEARCH   unsorted, or searched once ............ linear search   O(N)
#            sorted, searched many times ........... binary search   O(log N)
#   SORT     tiny list, simplest code .............. selection / insertion sort
#            nearly sorted / one item at a time .... insertion sort  (O(N) here)
#            general purpose, little spare memory .. quicksort       O(N log N) typical
#            guaranteed speed, stable, huge data ... merge sort      O(N log N) always
#            everyday Python code .................. sorted() / list.sort()
#
#   Algorithm        Best         Typical      Worst        Extra memory
#   Linear search    O(1)         O(N)         O(N)         -
#   Binary search    O(1)         O(log N)     O(log N)     -
#   Selection sort   O(N^2)       O(N^2)       O(N^2)       none (in place)
#   Insertion sort   O(N)         O(N^2)       O(N^2)       none (in place)
#   Quicksort        O(N log N)   O(N log N)   O(N^2)       none (in place)
#   Merge sort       O(N log N)   O(N log N)   O(N log N)   O(N)
print("\n" + "=" * 70 + "\nTHE RACE: sorting 3,000 random numbers\n" + "=" * 70)

data = [random.randint(0, 99_999) for _ in range(3000)]
for name in ["selection sort", "insertion sort", "quicksort", "merge sort", "sorted()"]:
    nums = data[:]                       # every algorithm gets the same copy
    start = time.perf_counter()
    if name == "selection sort":
        selection_sort(nums)
    elif name == "insertion sort":
        insertion_sort(nums)
    elif name == "quicksort":
        quicksort(nums, 0, len(nums) - 1)
    elif name == "merge sort":
        merge_sort(nums, 0, len(nums) - 1)
    else:
        nums = sorted(nums)
    print(f"  {name:<15} {(time.perf_counter() - start) * 1000:8.1f} ms")
#   The O(N^2) sorts are about 100x slower than the O(N log N) ones.
#   (Selection vs insertion: same Big O, different constants. Big O describes
#    how time GROWS, not the exact time.)


# ==========================================================================
# PRACTICE
# =============================================================================
print("\n" + "=" * 70 + "\nPRACTICE\n" + "=" * 70)

# P1 - Guess my number (1-100). The computer guesses with binary search.
#      What is the most guesses it will ever need?   A: 7  (floor(log2 100) + 1)
secret, low, high, guesses = 73, 1, 100, 0
while True:
    guess = (low + high) // 2
    guesses += 1
    if guess < secret:
        print(f"  guess {guess}: higher")
        low = guess + 1
    elif guess > secret:
        print(f"  guess {guess}: lower")
        high = guess - 1
    else:
        print(f"  guess {guess}: correct after {guesses} guesses")
        break

# P2 - Find the FIRST 3 in [1, 3, 3, 3, 3, 5, 8]. The book's binary search
#      returns index 3 (any 3). Fix: when found, remember mid and keep looking LEFT.
data = [1, 3, 3, 3, 3, 5, 8]
low, high, found = 0, len(data) - 1, -1
while high >= low:
    mid = (high + low) // 2
    if data[mid] < 3:
        low = mid + 1
    elif data[mid] > 3:
        high = mid - 1
    else:
        found = mid
        high = mid - 1
print("first 3 is at index", found)                        # 1

# P3 - Sort (name, score) records from highest to lowest score with insertion sort.
#      Ben and Dee tie at 95. Why does Ben stay first?
#      A: we only swap when strictly greater, so equal items never swap -> STABLE
records = [("Ana", 88), ("Ben", 95), ("Cai", 72), ("Dee", 95), ("Eli", 88)]
for i in range(1, len(records)):
    j = i
    while j > 0 and records[j][1] > records[j - 1][1]:     # compare the scores
        records[j], records[j - 1] = records[j - 1], records[j]
        j -= 1
print(records)

# P4 - Name the Big O:
#      for x in a: ...  then  for y in a: ...   -> O(N)    (N + N = 2N)
#      for x in a:  for y in a: ...             -> O(N^2)
#      for x in a:  for y in range(10): ...     -> O(N)    (10 is a constant)
#      while n > 1: n = n // 2                  -> O(log N)

# P5 - 1,000 numbers, nearly sorted (one pair swapped). Insertion or selection?
#      A: insertion: about 1,000 comparisons. Selection: always 499,500.
nearly = list(range(1000))
nearly[500], nearly[501] = nearly[501], nearly[500]
print("insertion sort comparisons:", insertion_sort(nearly))   # 1000

