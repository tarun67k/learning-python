# List of tuples
tuple_list = [(1, 3), (4, 1), (2, 2)]

# Sort the list based on the second element of each tuple
sorted_list = sorted(tuple_list, key=lambda x: x[1])

print(sorted_list)

