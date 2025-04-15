import random

def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Original list: {numbers}')
shuffled_numbers = shuffle_list(numbers)
print(f'Shuffled list: {shuffled_numbers}')
