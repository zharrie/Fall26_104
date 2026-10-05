# =============================================================================
#  YOUR TURN 
#   1. From "<your-firstname>.<your-lastname>@montclair.edu", print the username and the domain
#      using find() and slicing.
#   2. Turn "portable network graphics" into the acronym "PNG".
#   3. Turn the date "2025-09-18" into "09/18/2025" using split() and join().
# =============================================================================

# 1
email = "rayan.nasir@montclair.edu"
username = email[:email.find("@")]

# 2
png = "portable network graphics"
png_abbrev = ""
for i in range(len(png)):
    if i==0:
        png_abbrev+=png[i]
    elif png[i]==" ":
        png_abbrev+=png[i+1]

png_abbrev = png_abbrev.upper()
print(png_abbrev)



# 3
raw_date = "2025-09-18"
date_arr = raw_date.split("-")
date_arr = [date_arr[1],date_arr[2],date_arr[0]]
cleaned_date = "/".join(date_arr)
print(cleaned_date)

