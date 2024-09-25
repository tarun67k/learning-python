### Day 5: Loops – For and While

In Python, **loops** are used to execute a block of code repeatedly. Python provides two main types of loops: **`for` loops** and **`while` loops**.

---

### 1. **For Loop**

A `for` loop iterates over a sequence (such as a list, tuple, string, or range) and executes the block of code inside the loop for each element in the sequence.

**Syntax:**
```python
for variable in sequence:
    # code to be executed
```

#### Example 1: Looping through a list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

#### Example 2: Using `range()` to loop through numbers
```python
for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)
```
**Output:**
```
0
1
2
3
4
```

---

### 2. **While Loop**

A `while` loop repeatedly executes the block of code as long as the condition provided is `True`.

**Syntax:**
```python
while condition:
    # code to be executed
```

#### Example 1: Counting with a `while` loop
```python
i = 0
while i < 5:
    print(i)
    i += 1  # increment i to avoid an infinite loop
```
**Output:**
```
0
1
2
3
4
```

#### Example 2: Exit when a condition is met
```python
x = 10
while x > 0:
    print(f"x is {x}")
    x -= 2  # decrease x by 2 in each iteration
```
**Output:**
```
x is 10
x is 8
x is 6
x is 4
x is 2
```

---

### Differences Between `for` and `while` Loops:
    - **For Loop:** Best when you know the number of iterations (e.g., iterating over a sequence).
    - **While Loop:** Best when you loop until a condition is met, and the number of iterations is unknown.

