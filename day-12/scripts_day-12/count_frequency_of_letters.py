# Input: Word from the user
word = input("Enter a word: ")

# Initialize an empty dictionary to store letter frequencies
letter_frequency = {}

# Iterate through each letter in the word
for letter in word:
    # Update the frequency count in the dictionary
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

# Print the frequency of each letter
print("Letter frequencies:")
for letter, count in letter_frequency.items():
    print(f"{letter}: {count}")

