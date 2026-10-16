color_names = input()
insert_index = int(input())

#sienna;yellow;orange
""" Your code goes here """
word_token = (";")
color_list = color_names.split(word_token)
color_list.insert(insert_index, "lilac")

print(color_list)
