### Defining Functions

In Python, you define a function using the `def` keyword followed by the function name and parentheses. Here’s a basic structure:

```python
def function_name(parameters):
    # Code block
    return value
```

### Example

```python
def greet(name):
    return f"Hello, {name}!"
```

In this example, `greet` is a function that takes one parameter, `name`, and returns a greeting string.

### Parameters

Parameters are variables listed inside the parentheses in a function definition. They are placeholders for the values you’ll pass into the function when you call it. 

**Example:**

```python
def add(a, b):
    return a + b
```

Here, `a` and `b` are parameters of the `add` function.

### Return Values

A function can return a value using the `return` statement. This value is sent back to the caller and can be used later in the program.

**Example:**

```python
result = add(3, 4)  # result will be 7
```

In this case, `add(3, 4)` returns `7`, which is assigned to the variable `result`.

### Calling Functions

To use a function, you call it by its name and pass the required arguments.

**Example:**

```python
print(greet("Alice"))  # Output: Hello, Alice!
```

### Default Parameters

You can also set default values for parameters, which makes some arguments optional.

**Example:**

```python
def greet(name="Guest"):
    return f"Hello, {name}!"
```

Here, if you call `greet()` without arguments, it will use "Guest" as the default value.

Let's create a few simple functions and see how to call them.

### 1. Function Without Parameters

**Function Definition:**

```python
def say_hello():
    print("Hello, world!")
```

**Calling the Function:**

```python
say_hello()
```

**Output:**

```
Hello, world!
```

### 2. Function With Parameters

**Function Definition:**

```python
def greet(name):
    print(f"Hello, {name}!")
```

**Calling the Function:**

```python
greet("Alice")
greet("Bob")
```

**Output:**

```
Hello, Alice!
Hello, Bob!
```

### 3. Function With Return Value

**Function Definition:**

```python
def add(a, b):
    return a + b
```

**Calling the Function:**

```python
result = add(5, 3)
print(result)
```

**Output:**

```
8
```

### 4. Function With Default Parameter

**Function Definition:**

```python
def greet(name="Guest"):
    return f"Hello, {name}!"
```

**Calling the Function:**

```python
print(greet())
print(greet("Charlie"))
```

**Output:**

```
Hello, Guest!
Hello, Charlie!
```

### 5. Function With Multiple Parameters and Return Value

**Function Definition:**

```python
def multiply(x, y):
    return x * y
```

**Calling the Function:**

```python
product = multiply(4, 5)
print(product)
```

**Output:**

```
20
```


