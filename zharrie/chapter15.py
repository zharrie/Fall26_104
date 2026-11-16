"""
=====================================================================================
 CHAPTER 15 - PYTHON FOR DATA SCIENCE
=====================================================================================
 15.1  Introduction to data science
 15.2  Data science life cycle
 15.3  Introduction to Python for DS
 15.4  Introduction to Jupyter Notebooks
 15.5  NumPy
 15.6  pandas
 15.7  Matplotlib
=====================================================================================
"""
import json
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 20)

# Shared sample datasets used throughout the lecture
penguins = pd.DataFrame({
    "species": ["Adelie", "Chinstrap", "Gentoo", "Adelie", "Gentoo", "Adelie", "Adelie",
                "Chinstrap", "Chinstrap", "Gentoo", "Gentoo", "Adelie", "Chinstrap", "Gentoo"],
    "island": ["Dream", "Dream", "Dream", "Biscoe", "Biscoe", "Torgersen", "Biscoe",
               "Dream", "Dream", "Biscoe", "Biscoe", "Torgersen", "Dream", "Biscoe"],
    "bill_length_mm": [36.5, 43.5, 48.7, 36.3, 45.3, 39.1, 38.8,
                       49.6, 50.9, 46.1, 50.0, 37.8, 46.5, 47.6],
    "bill_depth_mm": [18.0, 18.1, 15.7, 19.5, 13.7, 18.7, 17.2,
                      18.2, 19.1, 13.2, 15.2, 18.3, 17.9, 14.5],
    "flipper_length_mm": [182, 202, 208, 190, 210, 181, 180, 193, 196, 211, 218, 174, 192, 215],
    "body_mass_g": [3150, 3400, 5350, 3800, 4300, 3750, 3800,
                    3775, 3550, 4500, 5700, 3400, 3500, 5400],
    "sex": ["female", "female", "female", "male", "male", "male", "male",
            "male", "male", "female", "male", "female", "female", "male"],
})

country = pd.DataFrame({          # populations: rounded ~2023 estimates
    "Name": ["China", "India", "United States", "Indonesia", "Pakistan", "Nigeria", "Brazil",
             "Bangladesh", "Russia", "Mexico", "Japan", "Germany", "Norway", "Iceland"],
    "Continent": ["Asia", "Asia", "North America", "Asia", "Asia", "Africa", "South America",
                  "Asia", "Europe", "North America", "Asia", "Europe", "Europe", "Europe"],
    "Population": [1_425_000_000, 1_428_000_000, 340_000_000, 277_500_000, 240_500_000,
                   223_800_000, 216_400_000, 173_000_000, 144_400_000, 128_500_000,
                   123_300_000, 83_300_000, 5_500_000, 375_000],
})

taxis = pd.DataFrame({            # stand-in for the book's taxi.csv (NYC, March 2019)
    "passengers": [1, 1, 2, 1, 3, 1, 5, 2, 1, 6],
    "distance":   [1.60, 0.79, 7.70, 2.16, 9.80, 0.50, 3.10, 12.40, 1.10, 4.25],
    "fare":       [7.0, 5.0, 27.0, 9.0, 32.0, 4.5, 13.5, 36.5, 6.5, 16.0],
    "tip":        [2.15, 0.00, 6.00, 2.00, 0.00, 1.00, 3.35, 8.00, 0.00, 3.86],
    "tolls":      [0.0, 0.0, 0.0, 0.0, 5.76, 0.0, 0.0, 6.12, 0.0, 0.0],
    "total":      [12.95, 9.30, 36.30, 14.30, 41.06, 8.80, 20.15, 54.92, 10.30, 23.16],
})


##################################################################################
#    15.1  INTRODUCTION TO DATA SCIENCE
#####################################################################################
# CONCEPTS
#   * Data science: an interdisciplinary field that discovers patterns and describes
#     relationships using data. It combines COMPUTER SCIENCE and STATISTICS.
#   * Data model: a representation of a real-life system that organizes data elements
#     and how they relate (e.g. the FBI's Most Wanted list). It predicts for new data.
#   * Roles:
#       Computer scientist -> software, websites, security, data storage tools, algorithms
#       Statistician       -> design experiments, derive models, analyze with models
#       Data scientist     -> format datasets, build dynamic plots, interpret results
#   * Dataset = FEATURES (variables -> columns) recorded for INSTANCES
#     (observations / data points -> rows).
#   * Big data = the 3 Vs:
#       VOLUME   very large      -> Spark, Hadoop, Cloudera, cloud (AWS, Google, Azure)
#       VELOCITY updated quickly -> reproducible code, automation, version control
#       VARIETY  many formats    -> tables, images, video, sound, text
# ------------------------------------------------------------------------------------

# Example 1: features vs instances (the 5 penguins shown in the book)
book_penguins = penguins.head(5)
print(book_penguins)
print("Instances (rows):", book_penguins.shape[0], "| Features (columns):", book_penguins.shape[1])
print("One instance (row 2):", book_penguins.iloc[2].to_dict())
print("One feature (bill length):", book_penguins["bill_length_mm"].tolist())

# Example 2: VOLUME - how big is big data?   1 EB = 10**18 bytes = 1,000,000 TB
global_data_eb = {1986: 2.6, 1993: 15.8, 2000: 54.5, 2007: 295, 2020: 6800}
for year, eb in global_data_eb.items():
    print(f"{year}: {eb:>7,} EB = {eb * 1_000_000:>15,.0f} one-TB laptops")
print(f"Growth 1986 -> 2020: x{6800 / 2.6:,.0f}")
print(f"Twitter: 12 TB/day x 365 = {12 * 365 / 1000:.2f} PB/year")


# Example 3: VELOCITY - code is reproducible: new data arrives, re-run one line
# A simple rule identifies tumors larger than the threshold. Because the code is
# written once and reused, adding more patient records updates the answer instantly.
def flag_tumors(sizes_mm, threshold=20):
    return sum(size > threshold for size in sizes_mm)


scans = [12, 25, 8, 31, 18, 22, 9, 15, 27, 11]
print("Flagged (10 scans):", flag_tumors(scans))
scans += [35, 14, 19, 40]                                # new scans arrive
print("Flagged (14 scans):", flag_tumors(scans))

# Example 4: VARIETY - semi-structured (JSON) and unstructured (text) -> structured
post = json.loads('{"user": "ana", "likes": 12, "tags": ["#bigdata", "#python"]}')
print("Parsed JSON:", post)
review = "Loved the phone, battery is great but the camera is bad."
words = review.lower().replace(",", "").replace(".", "").split()
print("Text -> features:", {"n_words": len(words), "great": words.count("great"),
                            "bad": words.count("bad")})

# CHECK YOUR UNDERSTANDING (book participation activities)
#   Q: Interactive graph of 18 months of sales?           A: Data scientist
#   Q: UI for a data storage system?                      A: Computer scientist
#   Q: Experiment comparing 3 marketing strategies?       A: Statistician
#   Q: Transactions / Sales amount / Type of store?       A: Instance / Feature / Feature
#   Q: Health records with measurements, scans, notes?    A: Variety
#   Q: Smartwatches continuously tracking heart rate?     A: Velocity
#   Q: Records and claims for every insured customer?     A: Volume
#   Q: Why specialized big-data tools?    A: Datasets may be too large for a personal computer
#   Q: Cloud storage helps by...          A: Spreading portions across locations and servers
#   Q: Plan for high-velocity data?       A: Write code to complete analyses
#   Q: Task to automate with code?        A: Generating a weekly report
#   Q: How to deal with variety?          A: Use tools from multiple disciplines
#
# COMMON MISTAKES
#   * Thinking big data means only VOLUME (velocity and variety count too).
#   * Mixing up rows and columns: rows = instances, columns = features.

# ---------------------------- EXERCISES 15.1 ----------------------------------------
# Exercise 15.1.1: For the cars list below, print the number of instances, the number
#                  of features, the feature names, and the mpg of every car.
cars = [{"model": "Civic", "mpg": 36, "cylinders": 4},
        {"model": "Mustang", "mpg": 22, "cylinders": 8},
        {"model": "Prius", "mpg": 52, "cylinders": 4}]
# Solution:
print("\nEx 15.1.1:", len(cars), "instances |", len(cars[0]), "features |",
      list(cars[0]), "| mpg:", [car["mpg"] for car in cars])

# Exercise 15.1.2: How many 2-TB laptops are needed to store 6800 EB (2020)?
# Solution:
print(f"Ex 15.1.2: {6800 * 1_000_000 / 2:,.0f} laptops")

# Exercise 15.1.3: Which V?  (a) 5,000 card transactions per second  (b) X-rays, doctor
#                  notes and lab tables  (c) 20 years of sales totaling 900 TB
# Solution:
print("Ex 15.1.3:", {"a": "Velocity", "b": "Variety", "c": "Volume"})


# %% #################################################################################
#    15.2  DATA SCIENCE LIFE CYCLE
# ####################################################################################
# CONCEPTS
#   Step 1 GATHER    find relevant data; gather new data if needed
#   Step 2 CLEAN     reformat, create new features, handle missing values (NaN)
#   Step 3 EXPLORE   plots + summary statistics (mean, median) to find patterns
#   Step 4 MODEL     fit/evaluate models, measure relationships, predict
#   Step 5 INTERPRET communicate results (reports, presentations); steps may repeat
#
#   * Structured: predefined format, rows/columns (tables, spreadsheets, databases)
#     Semi-structured: some structure (JSON, XML, emails, social media, web tables)
#     Unstructured: no predefined format (images, audio, video, free text)
#   * SUPERVISED models predict a known feature:
#       CLASSIFICATION -> categorical output (species, fraud yes/no)
#       REGRESSION     -> numeric output (body mass, price)
#     UNSUPERVISED models find hidden groups or patterns (no target feature).
# ------------------------------------------------------------------------------------
print("\n========== 15.2 DATA SCIENCE LIFE CYCLE ==========")

# Example 1: the full life cycle on credit card fraud
# STEP 1 - GATHER: combine two sources
source_a = pd.DataFrame({"Transaction": [141143, 141144, 141145, 141146],
                         "Amount": [86.79, 226.32, 104.77, 86.95],
                         "StoreType": ["Gas", "Clothing", "Grocery", "Gas"],
                         "Fraud": ["No", "No", "No", "Yes"]})
source_b = pd.DataFrame({"Transaction": [141147, 141148, 141149, 141150, 141151, 141152],
                         "Amount": [34.37, 245.10, 51.20, np.nan, 310.00, 212.75],
                         "StoreType": ["Restaurant", "Gas", "Gas", "Gas", "Gas", "Gas"],
                         "Fraud": ["Yes", "Yes", "No", "No", "Yes", "Yes"]})
transactions = pd.concat([source_a, source_b], ignore_index=True)

# STEP 2 - CLEAN: keep gas stations, encode Fraud as 1/0, drop the missing amount
gas = transactions[transactions["StoreType"] == "Gas"].copy()
gas["Fraud01"] = gas["Fraud"].map({"Yes": 1, "No": 0})
print("Missing amounts:", gas["Amount"].isna().sum())
gas = gas.dropna(subset=["Amount"])
print(gas)

# STEP 3 - EXPLORE
print("Mean amount by fraud status:\n", gas.groupby("Fraud01")["Amount"].mean().round(2))

# STEP 4 - MODEL: a simple rule -> "Amount over $200 means fraud"
gas["Predicted"] = (gas["Amount"] > 200).astype(int)
accuracy = (gas["Predicted"] == gas["Fraud01"]).mean()

# STEP 5 - INTERPRET
print(f"Large gas-station transactions are often fraud; the $200 rule is {accuracy:.0%} accurate.")

# Example 2: cleaning - NaN, a new feature, filtering instances
peng = penguins.head(5).copy()
peng.loc[[1, 3], "bill_length_mm"] = np.nan                 # missing observations
peng["sex01"] = (peng["sex"] == "female").astype(int)       # new feature: 1 = female
print("\nMissing values:\n", peng.isna().sum())
print(peng[peng["species"] != "Chinstrap"])                 # filter out Chinstrap

# Example 3: exploring - summary statistics, box plot, and scatter plot
print(penguins.groupby("species")["bill_length_mm"].agg(["mean", "median"]).round(2))
species_names = ["Adelie", "Chinstrap", "Gentoo"]
plt.figure(figsize=[10, 4])
plt.subplot(1, 2, 1)
plt.boxplot([penguins.loc[penguins["species"] == s, "bill_length_mm"] for s in species_names])
plt.xticks([1, 2, 3], species_names)
plt.title("Bill length by species")
plt.subplot(1, 2, 2)
for s in species_names:
    part = penguins[penguins["species"] == s]
    plt.scatter(part["bill_length_mm"], part["bill_depth_mm"], label=s)
plt.xlabel("Bill length (mm)")
plt.ylabel("Bill depth (mm)")
plt.legend()
plt.show()

# Example 4: modeling
# Classification: predict the species whose average bill length is closest to 38 mm
species_means = penguins.groupby("species")["bill_length_mm"].mean()
print("\nClassification: 38 mm bill ->", (species_means - 38).abs().idxmin())
# Regression: fit a straight line, body mass ~ flipper length
slope, intercept = np.polyfit(penguins["flipper_length_mm"], penguins["body_mass_g"], 1)
print(f"Regression: 200 mm flipper -> {slope * 200 + intercept:,.0f} g")
# Unsupervised: no target, just group penguins by size
size_group = np.where(penguins["body_mass_g"] > penguins["body_mass_g"].mean(), "Large", "Small")
print("Unsupervised groups:", pd.Series(size_group).value_counts().to_dict())

# CHECK YOUR UNDERSTANDING
#   Q: Tumor project - collect records / plot blood work / remove missing values and IDs /
#      conference presentation / test several models?
#   A: Gathering / Exploring / Cleaning / Interpreting / Modeling
#   Q: Structured?      A: Customer mailing addresses
#   Q: Unstructured?    A: Historical letters
#   Q: Semi-structured? A: A Wikipedia table of weekly box office sales
#   Q: Why is clean data important?  A: It is formatted for building models and visuals
#   Q: Patients have missing data?   A: Investigate WHY values are missing first
#   Q: Exploratory analysis is for?  A: Recognizing patterns and relationships
#   Q: Classification?  A: Whether a house sells in under 30 days
#   Q: Unsupervised?    A: Grouping cities by weather patterns
#   Q: Regression?      A: Length of a flight delay
#   Q: Audiences - administrators / data scientists / clinicians?
#   A: Short non-technical talk / technical report with code / presentation with applications
#
# COMMON MISTAKES
#   * Deleting rows with missing values without asking why they are missing.
#   * Calling every prediction "regression": categorical output = classification.

# ---------------------------- EXERCISES 15.2 ----------------------------------------
# Exercise 15.2.1: Clean this dataset: count missing values, add 'passed01'
#                  (1 = pass), keep only CS students, and drop missing scores.
students = pd.DataFrame({"name": ["Ana", "Ben", "Cy", "Di", "Ed"],
                         "course": ["CS", "CS", "Art", "CS", "CS"],
                         "score": [88, np.nan, 75, 92, 61],
                         "result": ["pass", "pass", "pass", "pass", "fail"]})
# Solution:
print("\nEx 15.2.1 missing:", students.isna().sum().to_dict())
students["passed01"] = (students["result"] == "pass").astype(int)
print(students[students["course"] == "CS"].dropna(subset=["score"]))

# Exercise 15.2.2: Fit a line to hours vs scores, predict the score for 5.5 hours,
#                  and write a one-sentence interpretation.
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [52, 55, 61, 64, 70, 74, 79, 85]
# Solution:
m, b = np.polyfit(hours, scores, 1)
print(f"Ex 15.2.2: prediction = {m * 5.5 + b:.1f}; each extra hour adds about {m:.1f} points.")

# Exercise 15.2.3: Classification, regression, or unsupervised?
#                  (a) next month's spending  (b) spam or not  (c) group similar songs
# Solution:
print("Ex 15.2.3:", {"a": "Regression", "b": "Classification", "c": "Unsupervised"})


# %% #################################################################################
#    15.3  INTRODUCTION TO PYTHON FOR DATA SCIENCE
# ####################################################################################
# CONCEPTS
#   ADVANTAGES                          DISADVANTAGES
#   Readability (reads like English)    Consistency (libraries differ in conventions)
#   Popularity (many resources)         Memory (uses more than other languages)
#   Innovation (new models added fast)  Speed (e.g. Julia can be faster)
#
#   Package            Alias      Purpose
#   numpy              np         numerical computation (used by most other packages)
#   pandas             pd         tabular and time-series data
#   sklearn            sk         machine learning (scikit-learn)
#   matplotlib.pyplot  plt        visualization (expects NumPy arrays)
#   seaborn            sns        visualization (works well with DataFrames)
#   scipy.stats        sp.stats   scientific algorithms and statistics
#   statsmodels        sm         statistical models and inference
# ------------------------------------------------------------------------------------
print("\n========== 15.3 PYTHON FOR DATA SCIENCE ==========")

# Example 1: SPEED - Python loop vs NumPy (compiled code)
values = list(range(1_000_000))
start = time.perf_counter()
squares_list = [v * v for v in values]
list_time = time.perf_counter() - start
start = time.perf_counter()
squares_array = np.arange(1_000_000) ** 2
numpy_time = time.perf_counter() - start
print(f"List: {list_time * 1000:.1f} ms | NumPy: {numpy_time * 1000:.1f} ms")

# Example 2: CONSISTENCY - same function name, different default
data = [2, 4, 4, 4, 5, 5, 7, 9]
print("np.std:", np.std(data), "| pandas std:", round(pd.Series(data).std(), 4))
# NumPy uses ddof=0 (population); pandas uses ddof=1 (sample). Read the docs!

# CHECK YOUR UNDERSTANDING
#   Q: Python is harder to read than most languages?        A: False
#   Q: Good choice when performance is the priority?        A: False
#   Q: Good choice when using packages from other DS?       A: True
#   Q: Read/manipulate datasets?  A: pandas    Q: Visualize?  A: seaborn
#   Q: Build and evaluate a machine learning model?         A: scikit-learn
#
# COMMON MISTAKES
#   * import matplotlib as plt        -> use: import matplotlib.pyplot as plt
#   * import scikit-learn             -> the import name is sklearn

# ---------------------------- EXERCISES 15.3 ----------------------------------------
# Exercise 15.3.1: Name the package: (a) t-test p-value  (b) remove duplicate rows
#                  (c) train a classifier  (d) multiply matrices  (e) line plot
# Solution:
print("\nEx 15.3.1:", {"a": "scipy.stats", "b": "pandas", "c": "scikit-learn",
                       "d": "numpy", "e": "matplotlib.pyplot"})

# Exercise 15.3.2: Make np.std match pandas' .std() for the data below.
# Solution:
data = [10, 12, 23, 23, 16, 23, 21, 16]
print("Ex 15.3.2:", round(np.std(data, ddof=1), 4), "==", round(pd.Series(data).std(), 4))

# Exercise 15.3.3: Convert 1,000,000 Celsius values to Fahrenheit with a list
#                  comprehension and with NumPy. Which is faster?
# Solution:
celsius = np.random.default_rng(1).uniform(-30, 45, 1_000_000)
start = time.perf_counter()
fahrenheit_list = [c * 9 / 5 + 32 for c in celsius.tolist()]
middle = time.perf_counter()
fahrenheit_array = celsius * 9 / 5 + 32
end = time.perf_counter()
print(f"Ex 15.3.3: list {(middle - start) * 1000:.0f} ms vs NumPy {(end - middle) * 1000:.0f} ms")


# %% #################################################################################
#    15.4  INTRODUCTION TO JUPYTER NOTEBOOKS
# ####################################################################################
# CONCEPTS
#   * Jupyter: an interactive development environment (IDE). Code lives in a notebook
#     (.ipynb) made of CELLS, and each cell runs independently.
#       Code cell     -> labeled In [n]
#       Markdown cell -> formatted text, not labeled
#       Raw cell      -> output, labeled Out [n]
#   * KERNEL: the interpreter that runs code and remembers every variable created.
#   * Toolbar: + (new cell below) | copy/paste | up/down arrows (move cell) |
#     Run (current cell) | Restart kernel | >> (restart AND run all) | cell type
#   * File > Download as -> save the notebook as .ipynb, PDF, or HTML.
#   * Jupyter supports multiple languages through kernels.
# ------------------------------------------------------------------------------------
print("\n========== 15.4 JUPYTER NOTEBOOKS ==========")

# Example 1: the kernel remembers the ORDER cells were run (hidden state)
cells = {1: "x = 10", 2: "x = x * 2"}
for run_order in ([1, 2], [1, 2, 2]):          # second time, cell 2 was clicked twice
    kernel = {}
    for cell_number in run_order:
        exec(cells[cell_number], {}, kernel)
    print(f"Cells run in order {run_order} -> x = {kernel['x']}")
# Fix: Restart & Run All (>>) always gives a clean top-to-bottom result.

# Example 2: Try 15.4.1 - load mpg data, scatter plot, summary statistics
mpg = pd.DataFrame({
    "mpg":        [18, 15, 36, 26, 32, 14, 24, 22, 31, 17, 29, 13],
    "cylinders":  [8, 8, 4, 4, 4, 8, 4, 6, 4, 6, 4, 8],
    "horsepower": [130, 165, 58, 79, 65, 215, 95, 100, 67, 110, 70, 175],
    "weight":     [3504, 3693, 1835, 2234, 2045, 4312, 2372, 2789, 1965, 3329, 2130, 4464],
})
points = plt.scatter(mpg["weight"], mpg["mpg"], c=mpg["cylinders"])
plt.colorbar(points, label="cylinders")
plt.xlabel("weight")
plt.ylabel("mpg")
plt.show()
print(mpg["weight"].describe().round(1))

# Example 3: a notebook is just JSON, so we can write one
notebook = {"nbformat": 4, "nbformat_minor": 5, "metadata": {}, "cells": [
    {"cell_type": "markdown", "id": "c0", "metadata": {}, "source": ["# Miles per gallon"]},
    {"cell_type": "code", "id": "c1", "metadata": {}, "execution_count": None,
     "outputs": [], "source": ["print('Hello from Jupyter')"]}]}
with open("demo_notebook.ipynb", "w") as file:
    json.dump(notebook, file, indent=1)
print("Created demo_notebook.ipynb - open it in Jupyter or VS Code")

# CHECK YOUR UNDERSTANDING
#   Q: Small segments of code and output are called?  A: Cells
#   Q: The Run button executes...?                    A: Selected code (the current cell)
#   Q: Jupyter runs code in...?                       A: Multiple languages
#   Q: Selectable cell type?                          A: Markdown
#   Q: Double right triangle (>>)?                    A: Restart kernel and run all cells
#   Q: The + button?                                  A: Adds a new cell below the current one
#
# COMMON MISTAKES
#   * Running cells out of order -> results nobody can reproduce. Use Restart & Run All.
#   * Typing code into a Markdown cell (it shows as text and never runs).

# ---------------------------- EXERCISES 15.4 ----------------------------------------
# Exercise 15.4.1: Cells {1: "total = 0", 2: "total = total + 5"}. What is total
#                  after running 1, 2, 2? Verify with exec().
# Solution:
kernel = {}
for cell_code in ["total = 0", "total = total + 5", "total = total + 5"]:
    exec(cell_code, {}, kernel)
print("\nEx 15.4.1: total =", kernel["total"], "(cell 2 ran twice)")

# Exercise 15.4.2 (Try 15.4.1 step 4): Copy the weight summary but use horsepower.
# Solution:
print("Ex 15.4.2:\n", mpg["horsepower"].describe().round(1))

# Exercise 15.4.3: Add a markdown cell "## Summary" to the notebook above and save it
#                  as my_notebook.ipynb.
# Solution:
notebook["cells"].append({"cell_type": "markdown", "id": "c2", "metadata": {},
                          "source": ["## Summary"]})
with open("my_notebook.ipynb", "w") as file:
    json.dump(notebook, file, indent=1)
print("Ex 15.4.3: saved my_notebook.ipynb with", len(notebook["cells"]), "cells")


# %% #################################################################################
#    15.5  NUMPY
# ####################################################################################
# CONCEPTS
#   * NumPy provides fast math: linear algebra, Fourier transforms, statistics.
#     import numpy as np
#   * ndarray: an N-dimensional array of elements of the SAME type. It is faster than
#     a list because it wraps compiled native code.
#       0-D scalar: 2   1-D: [2, 4, 6, 8]   2-D: [[2, 4, 6, 8], [12, 14, 16, 18]]
#   * shape = length of each dimension, e.g. (2, 4); size = total elements, e.g. 8
#   * Axes: axis 0 runs DOWN the rows, axis 1 runs ACROSS the columns.
#   * Arrays are mutable but have a fixed shape; shape changes return a NEW array.
#
#                axis 1 ------->
#   axis 0 |  [[12, 23, 10],
#          |   [57, 45, 94],
#          v   [68, 32, 89]]
# ------------------------------------------------------------------------------------
print("\n========== 15.5 NUMPY ==========")

# Example 1 (Figure 15.5.1): lists concatenate, arrays add element-wise
list1, list2 = [15.5, 25.11, 19.0], [12.2, 1.3, 6.38]
array1, array2 = np.array(list1), np.array(list2)
print("list1 + list2   =", list1 + list2)
print("loop over lists =", [round(a + b, 2) for a, b in zip(list1, list2)])
print("array1 + array2 =", array1 + array2)

# Example 2: dimensions, shape, size
for arr in [np.array(2), np.array([2, 4, 6, 8]),
            np.array([[2, 4, 6, 8], [12, 14, 16, 18]]),
            np.array([[[1, 2, 9], [3, 2, 6]], [[8, 8, 4], [9, 8, 7]]])]:
    print(f"ndim={arr.ndim}  shape={arr.shape}  size={arr.size}")
try:
    np.array([[10, 20, 30, 40], [50, 60, 70]])     # rows of different lengths
except ValueError:
    print("[[10, 20, 30, 40], [50, 60, 70]] -> invalid array")

# Example 3: axes with np.delete() and sort()
grid = np.array([[12, 23, 10], [57, 45, 94], [68, 32, 89], [72, 26, 41]])
print("delete column 1 (axis=1):\n", np.delete(grid, 1, axis=1))
print("delete row 1 (axis=0):\n", np.delete(grid, 1, axis=0))
sorted_columns = grid.copy()
sorted_columns.sort(axis=0)            # each column sorted downward
print("sort(axis=0):\n", sorted_columns)
sorted_rows = grid.copy()
sorted_rows.sort(axis=1)               # each row sorted across (the default)
print("sort(axis=1):\n", sorted_rows)

# Example 4 (Table 15.5.1): creating and modifying arrays
array_1d = np.array([1, 2, 3, 4])
array_2d = np.array([[1, 2], [3, 4]])
print("zeros:", np.zeros((1, 3)), "| ones:", np.ones((1, 3)), "| full:", np.full((2, 2), 6).tolist())
print("array_2d[1, 0] =", array_2d[1, 0])
print("ravel     :", np.array([[7, 7], [7, 7]]).ravel())
reshaped = array_1d.reshape((2, 2))
print("reshape   :", reshaped.tolist(), "| transpose:", reshaped.transpose().tolist())

# Example 5 (Table 15.5.2 / Figure 15.5.2): math operations are element-wise
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print("a + b =", a + b, "| a - b =", a - b, "| a * b =", a * b, "| a / b =", a / b)
print("dot =", np.dot(a, b), "| sqrt =", np.sqrt(a).round(2), "| min/max =", a.min(), a.max())
print("median =", np.median(a), "| std =", round(np.std(a), 2), "| var =", np.var(a))
print("matmul =", np.matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]).tolist(),
      "| cross =", np.cross([1, 0, 0], [0, 1, 0]))
print("a > 15 ->", a > 15)                                  # comparisons work too
print("column means:", np.array([[70, 80], [60, 90]]).mean(axis=0))

# CHECK YOUR UNDERSTANDING
#   Q: Benefit of NumPy over lists?           A: Faster mathematical operations
#   Q: Not done with NumPy?                   A: List concatenation
#   Q: In "import numpy as np", the alias?    A: np
#   Q: Shapes: ["a","b","c","d"] -> (4,) | 3-D example -> (2, 2, 3) | 4 pairs -> (4, 2) |
#      3.1415 -> () | ragged rows -> invalid | 2 rows of 4 -> (2, 4) | [3.1415] -> (1,)
#   Q: Axes in a 3-D array?  A: 3     Q: Second axis in 2-D?  A: 1     Q: Axis 0 runs along?  A: rows
#   Q: Fill in the blanks (Participation 15.5.5): delete | ravel | sort | 1
#   Q: All NumPy math functions take a scalar?  A: False (np.cross needs arrays)
#   Q: <, >, == can compare arrays?             A: True (element by element)
#   Q: min() returns a 1-D array?               A: False (it returns one value)
#
# Challenge 15.5.1: create the 2-D array [[11, 18, 7], [5, 9, 14]]
my_array = np.array([[11, 18, 7], [5, 9, 14]])
print(my_array)

# COMMON MISTAKES
#   * np.array(1, 2, 3)      -> pass ONE list: np.array([1, 2, 3])
#   * result = arr.sort()    -> sort() works in place and returns None
#   * reshape must keep the same size: 4 elements cannot become (3, 3)

# ---------------------------- EXERCISES 15.5 ----------------------------------------
temps = np.array([[71, 75, 68, 80],      # 3 cities x 4 weeks
                  [55, 52, 60, 58],
                  [88, 90, 85, 91]])
# Exercise 15.5.1: Print the shape and size of temps, delete week index 1, then
#                  flatten temps and reshape it to (4, 3).
# Solution:
print("\nEx 15.5.1:", temps.shape, temps.size, "|", np.delete(temps, 1, axis=1).tolist(),
      "|", temps.ravel().reshape((4, 3)).tolist())

# Exercise 15.5.2: Find the mean of each week (axis=0) and the max of each city (axis=1).
# Solution:
print("Ex 15.5.2: weekly means", temps.mean(axis=0).round(1), "| city max", temps.max(axis=1))

# Exercise 15.5.3: prices [2.5, 1.25, 4, 3.1] x quantities [10, 4, 2, 7]: revenue per
#                  item, total revenue (np.dot), and the number of items over $15.
# Solution:
prices = np.array([2.5, 1.25, 4, 3.1])
quantities = np.array([10, 4, 2, 7])
revenue = prices * quantities
print("Ex 15.5.3:", revenue, "| total", np.dot(prices, quantities), "| over $15:", (revenue > 15).sum())


# %% #################################################################################
#    15.6  PANDAS
# ####################################################################################
# CONCEPTS
#   * pandas stores and manipulates 2-D datasets; it is built on NumPy.
#     import pandas as pd
#   * DataFrame: columns = features, rows = instances.
#       row labels = INDEX (usually 0, 1, 2 ...)   column labels = COLUMNS (strings)
#   * DataFrame vs array: both are indexed, ordered, mutable, and have .shape. But a
#     DataFrame is always 2-D, its columns can have different types, and its labels
#     can be strings.
#   * Subsetting:
#       df["col"]            one column (Series)    df[["a", "b"]]  DataFrame
#       df[2:6]              rows 2-5 (end EXCLUDED)
#       df.iloc[r, c]        by POSITION (end EXCLUDED)
#       df.loc[r, ["a"]]     by LABEL    (end INCLUDED)
#   * Filtering: df[df["Population"] > 100000]
#       logical operators: & (and)  | (or)  ~ (not); wrap each condition in ( )
#   * Methods: drop, drop_duplicates, insert, replace, sort_values. By default they
#     return a NEW DataFrame (inplace=False).
# ------------------------------------------------------------------------------------
print("\n========== 15.6 PANDAS ==========")

# Example 1 (Participation 15.6.3): constructing a DataFrame
small = pd.DataFrame(data=[["China", "Asia", 9572900], ["Bangladesh", "Asia", 143998],
                           ["Brazil", "South America", 8547403], ["Norway", "Europe", 358207]],
                     columns=["Country", "Continent", "Population"],
                     index=[0, 1, 2, 3])
print(small)
print("shape:", small.shape, "| dtypes:", small.dtypes.astype(str).to_dict())

# Example 2: subsetting the 14-country dataset
print(type(country["Name"]).__name__, "vs", type(country[["Name"]]).__name__)
print("iloc[0, 1] =", country.iloc[0, 1])
print("country[2:6]:\n", country[2:6])
print("iloc[:5, 1:3]:\n", country.iloc[:5, 1:3])
print("loc[:6, ['Continent', 'Population']] (includes row 6):\n",
      country.loc[:6, ["Continent", "Population"]])

# Example 3: filtering with comparison and logical operators
print("Asia AND > 250 million:\n",
      country[(country["Continent"] == "Asia") & (country["Population"] > 250_000_000)])
print("Africa OR < 100 million:\n",
      country[(country["Continent"] == "Africa") | (country["Population"] < 100_000_000)])
print("NOT Asia:", country[~(country["Continent"] == "Asia")]["Name"].tolist())

# Challenge 15.6.1: subset the distance column  (book: taxisNY = pd.read_csv("taxi.csv"))
distance = taxis["distance"]
print(distance.head(3))

# Example 4 (Table 15.6.2): other DataFrame methods
df = country.head(5).copy()
df.insert(1, "Code", ["CN", "IN", "US", "ID", "PK"])                  # insert a column
print(df.sort_values(by="Population", ascending=False))               # sort rows
print(df.drop(labels="Code", axis=1).columns.tolist())                # drop a column
print(df.replace(to_replace="North America", value="N. America")["Continent"].tolist())
print("drop_duplicates(subset='Continent'):", country.drop_duplicates(subset="Continent")["Name"].tolist())
print("at[1, 'Continent'] =", country.at[1, "Continent"])
print("loc[1:3, 'Continent':'Population']:\n", country.loc[1:3, "Continent":"Population"])
df = df.sort_values(by="Name")       # reassign (inplace=True is being phased out)

# Example 5: missing values
tips = taxis["tip"].copy()
tips[[2, 7]] = np.nan
print("missing:", tips.isna().sum(), "| filled with median:", tips.fillna(tips.median()).tolist())

# CHECK YOUR UNDERSTANDING
#   Q: A, B, C, D in pandas.A(B=..., C=..., D=...)?   A: DataFrame, data, columns, index
#   Q: Column labels / identifier / pandas type / row labels?
#   A: columns / label / DataFrame / index
#   Q: Select Name as a DataFrame?        A: country[["Name"]]
#   Q: First 8 rows?                      A: country[0:8]
#   Q: First 5 rows, Name & Population?   A: country.loc[0:4, ["Name", "Population"]]
#   Q: Countries in Europe?               A: country[country["Continent"] == "Europe"]
#   Q: Population at least 1,000,000?     A: country[country["Population"] >= 1000000]
#   Q: Asia AND > 250 million?            A: use & with each condition in parentheses
#
# COMMON MISTAKES
#   * Using "and"/"or" instead of &/| -> ValueError: truth value of a Series is ambiguous
#   * Forgetting the parentheses around each condition (& binds tighter than ==)
#   * Expecting loc[0:4] to stop at 3: loc INCLUDES the end, iloc does not
#   * Calling df.sort_values(...) without assigning the result

# ---------------------------- EXERCISES 15.6 ----------------------------------------
# Exercise 15.6.1: Build a DataFrame of 3 cars (Make, Model, MPG) with index 101-103.
#                  Print it and its shape.
# Solution:
cars_df = pd.DataFrame(data=[["Honda", "Civic", 36], ["Ford", "Mustang", 22],
                             ["Toyota", "Prius", 52]],
                       columns=["Make", "Model", "MPG"], index=[101, 102, 103])
print("\nEx 15.6.1:\n", cars_df, cars_df.shape)

# Exercise 15.6.2: From taxis, select rides that are longer than 5 miles OR paid tolls,
#                  then rides with 2+ passengers AND no tip.
# Solution:
print("Ex 15.6.2:\n", taxis[(taxis["distance"] > 5) | (taxis["tolls"] > 0)])
print(taxis[(taxis["passengers"] >= 2) & (taxis["tip"] == 0)])

# Exercise 15.6.3: Insert a 'tip_pct' column (tip / fare * 100) after 'tip', sort by it
#                  in descending order, and show the top 3 rides.
# Solution:
taxis_pct = taxis.copy()
taxis_pct.insert(taxis_pct.columns.get_loc("tip") + 1, "tip_pct",
                 (taxis_pct["tip"] / taxis_pct["fare"] * 100).round(1))
print("Ex 15.6.3:\n", taxis_pct.sort_values(by="tip_pct", ascending=False).head(3))


# %% #################################################################################
#    15.7  MATPLOTLIB
# ####################################################################################
# CONCEPTS
#   * Matplotlib makes static, dynamic, and interactive plots (seaborn is built on it).
#     Advantages: versatility, familiarity (MATLAB style), portability, customizability.
#   * pyplot: a state-based interface where each line adds an element to the figure.
#     import matplotlib.pyplot as plt
#   * plot(x, y) line | scatter(x, y) points | figure(figsize=[w, h]) (default 6.4 x 4.8
#     inches) | show() needed in scripts | savefig("f.png") needed in zyBooks labs
#   * Labels: title, xlabel, ylabel, text(x, y, s), annotate(s, xy, xytext), legend(loc)
#     LaTeX math: r"$...$"
#   * Style: "ro" = red circles, or color= / marker= / linestyle=
#     colors b g r w k y m | lines - : -- -. | markers . , o + x X v ^ < > * p s D d h H
#   * grid(axis=, color=, linestyle=, linewidth=); styles cannot be combined in one string
#   * subplot(nrows, ncols, index); index starts at 1 | suptitle() = whole-figure title
# ------------------------------------------------------------------------------------
print("\n========== 15.7 MATPLOTLIB ==========")

# Example 1 (Try 15.7.1-15.7.3): line plots with a custom size, plus a scatter plot
x = np.linspace(-5, 5, 50)
plt.figure(figsize=[9, 4])
plt.subplot(1, 2, 1)
plt.plot(x, -4 * x - 4, label="y = -4x - 4")
plt.plot(x, -3 * x - 2, label="y = -3x - 2")
plt.legend()
plt.subplot(1, 2, 2)
rng = np.random.default_rng(7)
heights = rng.normal(170, 8, 40)
plt.scatter(heights, 0.9 * heights - 85 + rng.normal(0, 6, 40))
plt.show()

# Example 2: labeling - title, axis labels, LaTeX, text, annotate, legend
years = np.arange(1975, 2001)
total = 45000 - 250 * (years - 1975) + 3000 * np.sin((years - 1975) / 4)
alcohol = 26000 - 520 * (years - 1975)
plt.figure(figsize=[9, 5])
plt.plot(years, total, label="Total")
plt.plot(years, alcohol, label="Alcohol-related")
plt.title("Highway fatalities (illustrative data)", fontsize=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Fatalities", fontsize=14)
plt.annotate("Drinking age changed to 21", xy=(1984, 21320), xytext=(1986, 30000),
             arrowprops=dict())
plt.text(1976, 15000, r"LaTeX works too: $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$")
plt.legend(loc="upper right")
plt.show()

# Example 3: styling with format strings, plus grid lines
x = np.arange(1, 11)
plt.figure(figsize=[9, 4])
for i, fmt in enumerate(["r:", "rd", "r--", "mD", "b^", "gX-."]):
    plt.plot(x, x + 3 * i, fmt, label=fmt)      # same as color=, marker=, linestyle=
plt.legend(ncol=3)
plt.grid(axis="y", color="blue", linestyle=":", linewidth=1)
plt.title('Format strings | plt.grid(axis="y", color="blue", linestyle=":")')
plt.show()

# Example 4 (Try 15.7.9): multiple plots with subplot() and suptitle()
x = np.linspace(0, 2 * np.pi, 100)
plt.figure(figsize=[10, 3.5])
plt.subplot(1, 3, 1)
plt.plot(x, np.sin(x))
plt.title("subplot(1, 3, 1)")
plt.subplot(1, 3, 3)
plt.plot(x, np.cos(x), "r")
plt.title("subplot(1, 3, 3)")
plt.suptitle("One figure, two subplots")
plt.show()

# CHECK YOUR UNDERSTANDING
#   Q: Matplotlib can...?         A: Display static and dynamic plots
#   Q: Works across platforms?    A: True
#   Q: What can be adjusted?      A: Both axis labels and tick marks
#   Q: Code that creates a figure?   A: plt.figure()
#   Q: Save as photo.png?            A: plt.savefig("photo.png")
#   Q: When is plt.figure() needed?  A: To change the size from the default
#                                       (e.g. 6.4 x 4.8 CENTIMETERS, not inches)
#   Q: Title, size 18?         A: plt.title("Old Faithful eruptions", fontsize=18)
#   Q: Text at (3, 4)?         A: plt.text(3, 4, "Scatter plot")
#   Q: Legend in lower right?  A: plt.legend(loc="lower right")
#   Q: "r:" / "rd" / "r--"?    A: red dotted line / red thin diamonds / red dashed line
#   Q: Vertical grid lines?    A: plt.grid(axis="x")
#   Q: Dashed grid lines?      A: plt.grid(linestyle="--")
#   Q: Blue dotted grid lines? A: plt.grid(color="blue", linestyle=":")
#   Q: Title for the whole figure?   A: plt.suptitle("...")
#   Q: Row 1, column 2 of a 2x2 grid?  A: plt.subplot(2, 2, 2)
#
# COMMON MISTAKES
#   * plt.figure without ()  |  plt.savefig(photo.png) without quotes
#   * Calling savefig() AFTER show() -> the saved file may be empty
#   * plt.subplot(2, 1, 0) -> ValueError (the index starts at 1)
#   * plt.grid("b:") -> grid styles must use keywords

# ---------------------------- EXERCISES 15.7 ----------------------------------------
# Exercise 15.7.1: Scatter plot of hours vs scores (from 15.2) with a title (size 16),
#                  axis labels, an annotation pointing to (8, 85), and a legend.
# Solution:
plt.scatter(hours, scores, label="students")
plt.title("Study time vs score", fontsize=16)
plt.xlabel("Hours studied")
plt.ylabel("Score")
plt.annotate("Top student", xy=(8, 85), xytext=(5.5, 86), arrowprops=dict())
plt.legend(loc="upper left")
plt.show()

# Exercise 15.7.2: Plot monthly sales [12, 15, 14, 18, 21, 19] as a green line with
#                  circle markers, with dashed cyan horizontal grid lines only.
# Solution:
plt.plot(range(1, 7), [12, 15, 14, 18, 21, 19], "go-")
plt.grid(axis="y", color="c", linestyle="--")
plt.show()

# Exercise 15.7.3: One figure with 2 subplots side by side: a histogram of penguin body
#                  mass and a bar chart of penguins per species, plus a suptitle.
# Solution:
counts = penguins["species"].value_counts()
plt.figure(figsize=[10, 4])
plt.subplot(1, 2, 1)
plt.hist(penguins["body_mass_g"], bins=6)
plt.title("Body mass")
plt.subplot(1, 2, 2)
plt.bar(counts.index, counts.values)
plt.title("Penguins per species")
plt.suptitle("Penguin overview")
plt.show()


# %% #################################################################################
#    LABS 15.8 - 15.13
# ####################################################################################
# Each lab uses a hard-coded input so it runs here. The zyBooks input() line is
# shown in a comment above it - swap it in when submitting.
# Sample data files are written first so the labs can read them.
print("\n========== LABS 15.8 - 15.13 ==========")
pd.Series([59, 84, 73, 57, 87, 62, 56, 77, 62, 89, 68, 81, 89, 72, 87, 74, 89, 74, 66,
           84, 88, 70, 58, 63, 64]).to_frame().T.to_csv("scores.txt", sep=" ",
                                                          header=False, index=False)
pd.DataFrame({"Name": ["Barrett", "Wolfe", "Adams", "Nguyen", "Kim", "Patel"],
              "Midterm1": [94, 82, 73, 88, 91, 67], "Midterm2": [89, 76, 81, 92, 85, 72],
              "Final": [93, 80, 70, 95, 88, 65]}).to_csv("StudentInfo.tsv", sep="\t", index=False)
pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
              "Cancelled": [310, 280, 190, 150, 140, 210, 260, 240, 130, 120, 170, 330],
              "Delayed": [3200, 2900, 3100, 2800, 3300, 3900, 4400, 4200, 2700, 2600, 3000, 3800],
              "Diverted": [25, 18, 20, 15, 22, 30, 35, 33, 16, 14, 19, 28],
              "On Time": [14500, 13800, 15600, 15200, 15900, 15100, 15000, 15300,
                          14800, 15400, 14600, 14200]}).to_csv("LAX.csv", index=False)
pd.DataFrame({"Show": list("ABCDEFGH"), "Capacity": [86.2, 91.7, 70.5, 57.0, 80.7, 61.6, 87.3, 98.9],
              "Gross Potential": [77.1, 94.4, 49.8, 57.6, 67.5, 48.1, 77.4, 99.0]
              }).to_csv("broadway_july.csv", index=False)
pd.DataFrame({"Show": list("ABCDEFGH"), "Capacity": [89.4, 90.3, 71.3, 81.5, 66.2, 91.0, 66.6, 85.3],
              "Gross Potential": [70.7, 69.6, 50.9, 66.8, 57.2, 77.0, 67.6, 62.4]
              }).to_csv("broadway_december.csv", index=False)

# ---- 15.8 LAB: Average exam scores (NumPy arrays basic) ----------------------------
# Expected: Average scores: [81.5 82.5 70.  88.5 82.5] / ... 80 and above: 4
exam1 = np.array("75 80 65 82 92".split(), dtype=int)      # zyBooks: input().split()
exam2 = np.array("88 85 75 95 73".split(), dtype=int)      # zyBooks: input().split()
averages = (exam1 + exam2) / 2
print("Average scores:", averages)
print("Number of students who received 80 and above:", np.sum(averages >= 80))

# ---- 15.9 LAB: Curve student scores ------------------------------------------------
# Expected: Median = 73.00 / Average = 73.32 / Curved scores = [ 70  95  84 ...]
filename = "scores.txt"                                    # zyBooks: filename = input()
student_scores = np.loadtxt(filename, dtype=int)
print(f"Median = {np.median(student_scores):.2f}")
print(f"Average = {np.mean(student_scores):.2f}")
print("Curved scores =", student_scores + (100 - student_scores.max()))

# ---- 15.10 LAB: Course grade statistics (pandas) -----------------------------------
# NOTE: check the heading text against the zyBooks example output.
grades = pd.read_csv("StudentInfo.tsv", sep="\t")          # zyBooks: input() for the name
print(grades.sort_values(by="Final", ascending=False))
print("Max Scores:\n" + grades.max(numeric_only=True).to_string())
print("Median Scores:\n" + grades.median(numeric_only=True).to_string())
print("Average Scores:\n" + grades.mean(numeric_only=True).to_string())
print("Standard Deviations:\n" + grades.std(numeric_only=True).to_string())

# ---- 15.11 LAB: Flight status (line plot) ------------------------------------------
# NOTE: check the wording of the two average lines against the zyBooks example.
flights = pd.read_csv("LAX.csv")                           # zyBooks: input() for the name
print(f"Average flight delays: {flights['Delayed'].mean():.2f}")
print(f"Average flight cancellations: {flights['Cancelled'].mean():.2f}")
plt.plot(flights["Month"], flights["Delayed"], label="Delays")
plt.plot(flights["Month"], flights["Cancelled"], label="Cancellations")
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight status at LAX", fontsize=14)
plt.legend()
plt.savefig("output_fig.png")
plt.show()

# ---- 15.12 LAB: Broadway show scatter plot -----------------------------------------
shows = pd.read_csv("broadway_july.csv")                   # zyBooks: input() for the name
shows.insert(len(shows.columns), "Size", shows["Gross Potential"] / 2)
print(shows)
plt.scatter(shows["Capacity"], shows["Gross Potential"], marker="x", color="orange", s=shows["Size"])
plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)
plt.grid(linestyle="--")
plt.savefig("output_fig.png")
plt.show()

# ---- 15.13 LAB: Broadway show multiple plots ---------------------------------------
july = pd.read_csv("broadway_july.csv")
december = pd.read_csv("broadway_december.csv")
print(july)
print(december)
plt.figure(figsize=[10, 4])
for position, (month_df, month_title) in enumerate([(july, "July 2002"),
                                                    (december, "December 2002")], start=1):
    plt.subplot(1, 2, position)
    plt.scatter(month_df["Gross Potential"], month_df["Capacity"])
    plt.title(month_title)
    plt.xlabel("Gross Potential")
    plt.ylabel("Capacity")
plt.suptitle("Capacity vs. Gross Potential")
plt.savefig("subplots.png")
plt.show()


# %% #################################################################################
#    CHEAT SHEET
# ####################################################################################
# LIFE CYCLE  gather -> clean -> explore -> model -> interpret
# MODELS      classification (category) | regression (number) | unsupervised (groups)
# NUMPY       np.array .shape .size | zeros ones full | a[r, c] | np.delete(a, obj, axis)
#             a.sort(axis) | ravel reshape transpose | + - * / | dot matmul sqrt std
#             axis 0 = down the rows (per column), axis 1 = across (per row)
# PANDAS      pd.DataFrame(data=, columns=, index=) | df["c"] vs df[["c"]] | df[2:6]
#             iloc = position (end excluded) | loc = label (end included)
#             df[(c1) & (c2)]  |  ~ | drop drop_duplicates insert replace sort_values
# MATPLOTLIB  figure(figsize=) plot scatter | title xlabel ylabel text annotate legend
#             "ro" "b--" | grid(axis=, linestyle=) | subplot(r, c, i>=1) suptitle
#             savefig before show
print("\nEnd of Chapter 15 lecture.")
