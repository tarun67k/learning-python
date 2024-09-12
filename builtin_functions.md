# Python Built-in Functions Examples.

# 1. print() - Prints the given object(s) to the console
print("Hello, World!")

# 2. len() - Returns the length of an object (string, list, etc.)
my_string = "Python"
print("Length of my_string:", len(my_string))

# 3. type() - Returns the type of an object
print("Type of my_string:", type(my_string))

# 4. int() - Converts a value to an integer
number = "10"
print("String to integer:", int(number))

# 5. float() - Converts a value to a float (decimal)
print("Integer to float:", float(number))

# 6. str() - Converts a value to a string
print("Float to string:", str(10.5))

# 7. max() - Returns the largest item in an iterable or two+ arguments
numbers = [1, 5, 3, 9, 2]
print("Maximum number in list:", max(numbers))

# 8. min() - Returns the smallest item in an iterable or two+ arguments
print("Minimum number in list:", min(numbers))

# 9. sum() - Returns the sum of all items in an iterable
print("Sum of numbers in list:", sum(numbers))

# 10. abs() - Returns the absolute value of a number
print("Absolute value of -10:", abs(-10))

# 11. round() - Rounds a number to the nearest integer or specified number of decimals
print("Rounded 5.678 to 2 decimals:", round(5.678, 2))

# 12. sorted() - Returns a sorted list of items from an iterable
print("Sorted numbers:", sorted(numbers))

# 13. input() - Accepts user input as a string
# Uncomment below lines to take input from user
# name = input("Enter your name: ")
# print("Hello", name)

# 14. isinstance() - Checks if an object is an instance of a specific type/class
print("Is 5 an instance of int?", isinstance(5, int))

# 15. all() - Returns True if all elements of an iterable are true
print("All elements in [1, True, 'Python'] are true:", all([1, True, 'Python']))

# 16. any() - Returns True if any element of an iterable is true
print("Any element in [0, False, ''] is true:", any([0, False, '']))

# 17. range() - Generates a sequence of numbers
print("Numbers from 0 to 4:", list(range(5)))

# 18. zip() - Combines multiple iterables element-wise into tuples
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("Zipped names and scores:", list(zip(names, scores)))

# 19. map() - Applies a function to all items in an iterable
print("Squares of numbers:", list(map(lambda x: x**2, numbers)))

# 20. filter() - Filters items from an iterable based on a condition
print("Numbers greater than 5:", list(filter(lambda x: x > 5, numbers)))

# 21. eval() - Evaluates and executes an expression from a string
expression = "3 + 4"
print("Result of eval(expression):", eval(expression))

# 22. help() - Displays the documentation for an object or function
# Uncomment to see help for a function
# help(print)

