print("\n=== End-of-class examples ===")

# 1. Count how many times each word appears.
def word_counts(text):
    arr = text.split()
    uniques=[]
    for word in arr:
        if word not in uniques:
            uniques.append(word)
    return len(uniques)

print(f"1. {word_counts('The cat and the hat')=}")

# 2. Remove duplicates but keep the original order.
def unique(items):
    uniques = []
    for num in items:
        if num not in uniques:
            uniques.append(num)
    return uniques
    
print(f"2. {unique([3, 1, 3, 2, 1])=}")

# 3. Sum each column of a 2-D list.
def column_sums(table):
    r = 0
    sumC = [0] * len(table[0])
    for row in table:
        c=0
        for cell in row:
            sumC[c]+=cell
            c+=1
    return sumC

print(f"3. {column_sums([[1, 2, 3], [4, 5, 6]])=}")

# 4. Squares of the odd numbers only (comprehension).
def oddsq(*vals):
    output = []
    for val in vals:
        if val % 2 == 1:
            output.append(val*val)
    return output

# 5. Names of the top 2 scores, best first.
scores = {"Ann": 91, "Bo": 78, "Cy": 99, "Di": 85}
top_two = sorted(scores, key=scores.get, reverse=True)[:2]
print(f"5. {top_two=}")
