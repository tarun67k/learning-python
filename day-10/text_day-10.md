### Introduction to Lists and Tuples in Python

#### 1. **Lists**
- **Definition**: A list is a collection of items that is ordered and mutable (modifiable). It allows duplicate members.
- **Creation**: Lists are created using square brackets `[]`.

Example:
```python
my_list = [1, 2, 3, "apple", True]
```

- **Accessing elements**: You can access elements in a list by their index. Python uses **zero-based indexing**, meaning the first element is at index 0.
  
Example:
```python
print(my_list[0])  # Outputs: 1
print(my_list[3])  # Outputs: "apple"
```

- **Modifying elements**: Since lists are mutable, you can change the value of an element at a specific index.

Example:
```python
my_list[1] = 10
print(my_list)  # Outputs: [1, 10, 3, "apple", True]
```

- **Adding elements**: You can append elements to a list using `append()`.
  
Example:
```python
my_list.append("new item")
print(my_list)  # Outputs: [1, 10, 3, "apple", True, "new item"]
```

#### 2. **Tuples**
- **Definition**: A tuple is similar to a list but is immutable (cannot be changed after creation). It also allows duplicate elements.
- **Creation**: Tuples are created using parentheses `()`.

Example:
```python
my_tuple = (1, 2, 3, "banana", False)
```

- **Accessing elements**: Like lists, elements in a tuple can be accessed by their index.

Example:
```python
print(my_tuple[0])  # Outputs: 1
print(my_tuple[3])  # Outputs: "banana"
```

- **Immutability**: Since tuples are immutable, you cannot modify their elements after they are created.

Example:
```python
my_tuple[1] = 10  # This will raise an error
```

Here are some basic operations you can perform with lists and tuples in Python:

Basic List Operations
Creating a list:


my_list = [1, 2, 3, "apple", True]
Accessing elements:


print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True (access last element)
Slicing a list (getting a part of the list):


print(my_list[1:4])  # Output: [2, 3, "apple"] (from index 1 to 3)
print(my_list[:3])   # Output: [1, 2, 3] (from start to index 2)
Adding elements:

Append: Adds an element to the end of the list.

my_list.append("orange")
print(my_list)  # Output: [1, 2, 3, "apple", True, "orange"]

Insert: Adds an element at a specific index.

my_list.insert(2, "banana")
print(my_list)  # Output: [1, 2, "banana", 3, "apple", True]

Remove: Removes the first occurrence of a specific element.

my_list.remove("apple")
print(my_list)  # Output: [1, 2, 3, "banana", True]

Pop: Removes the element at a specific index (or the last element if no index is specified).

my_list.pop(3)
print(my_list)  # Output: [1, 2, 3, True]


print(len(my_list))  # Output: 4

Concatenation (joining two lists):

another_list = [5, 6, 7]
combined_list = my_list + another_list
print(combined_list)  # Output: [1, 2, 3, True, 5, 6, 7]

Basic Tuple Operations
Creating a tuple:

my_tuple = (1, 2, 3, "banana", False)

Accessing elements:

print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: False

Slicing a tuple:

print(my_tuple[1:4])  # Output: (2, 3, "banana")

Concatenation (joining two tuples):

another_tuple = (4, 5, 6)
combined_tuple = my_tuple + another_tuple
print(combined_tuple)  # Output: (1, 2, 3, "banana", False, 4, 5, 6)

Tuple length:

print(len(my_tuple))  # Output: 5

Checking if an item exists in a tuple:

print("banana" in my_tuple)  # Output: True
print(10 in my_tuple)  # Output: False


### Summary:
- **Lists** are mutable, created with `[]`, and elements can be modified.
- **Tuples** are immutable, created with `()`, and once created, their elements cannot be changed.



