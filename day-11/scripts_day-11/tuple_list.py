tuple_list = [(1, 2), (3, 4), (5, 6)]

# Convert each tuple to a list using a list comprehension
list_of_lists = [list(i) for i in tuple_list]

print(list_of_lists)