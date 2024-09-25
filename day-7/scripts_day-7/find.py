text = "Hello world! Welcome to the world of Python."
substring = "to"
index = text.find(substring)

if index != -1:
    print(f"The first occurrence of '{substring}' is at index {index}.")
else:
    print(f"'{substring}' not found in the string.")