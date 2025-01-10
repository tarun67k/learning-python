# Example dictionary
my_dict = {"name": "Tarun", "age": 25, "city": "Vijayawada"}

# Input: Key to check
key_to_check = input("Enter the key to check: ")

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"The value for the key '{key_to_check}' is: {my_dict[key_to_check]}")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
