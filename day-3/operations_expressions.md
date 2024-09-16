* operators and expressions

**Arithmetic operators** are used to perform mathematical operations between values. In Python, the most common arithmetic operators are:

    1. **Addition (`+`)**: Adds two values.
    ```python
    a = 5
    b = 3
    result = a + b  # result is 8
    ```

    2. **Subtraction (`-`)**: Subtracts the second value from the first.
    ```python
    a = 5
    b = 3
    result = a - b  # result is 2
    ```

    3. **Multiplication (`*`)**: Multiplies two values.
    ```python
    a = 5
    b = 3
    result = a * b  # result is 15
    ```

    4. **Division (`/`)**: Divides the first value by the second, returns a float.
    ```python
    a = 5
    b = 2
    result = a / b  # result is 2.5
    ```

    5. **Floor Division (`//`)**: Divides and rounds down to the nearest whole number.
    ```python
    a = 5
    b = 2
    result = a // b  # result is 2
    ```

    6. **Modulus (`%`)**: Returns the remainder of the division.
    ```python
    a = 5
    b = 2
    result = a % b  # result is 1
    ```

    7. **Exponentiation (`**`)**: Raises the first value to the power of the second.
    ```python
    a = 5
    b = 3
    result = a ** b  # result is 125
    ```

**Comparison operators** are used to compare two values. The result of these comparisons is either `True` or `False`.

Here are the common comparison operators in Python with examples:

    1. **Equal to (`==`)**: Checks if two values are equal.
    ```python
    a = 5
    b = 3
    result = a == b  # result is False
    result2 = a == 5  # result is True
    ```

    2. **Not equal to (`!=`)**: Checks if two values are not equal.
    ```python
    a = 5
    b = 3
    result = a != b  # result is True
    result2 = a != 5  # result is False
    ```

    3. **Greater than (`>`)**: Checks if the first value is greater than the second.
    ```python
    a = 5
    b = 3
    result = a > b  # result is True
    result2 = a > 6  # result is False
    ```

    4. **Less than (`<`)**: Checks if the first value is less than the second.
    ```python
    a = 5
    b = 3
    result = a < b  # result is False
    result2 = a < 6  # result is True
    ```

    5. **Greater than or equal to (`>=`)**: Checks if the first value is greater than or equal to the second.
    ```python
    a = 5
    b = 3
    result = a >= b  # result is True
    result2 = a >= 5  # result is True
    ```

    6. **Less than or equal to (`<=`)**: Checks if the first value is less than or equal to the second.
    ```python
    a = 5
    b = 3
    result = a <= b  # result is False
    result2 = a <= 5  # result is True
    ```

**Logical operators** are used to combine conditional statements and return `True` or `False` based on the logic of the conditions.

The three main logical operators in Python are:

    1. **AND (`and`)**: Returns `True` if both conditions are `True`.
    ```python
    a = 5
    b = 3
    c = 7
    
    result = (a > b) and (a < c)  # result is True (both conditions are True)
    result2 = (a > b) and (a > c)  # result is False (second condition is False)
    ```

    2. **OR (`or`)**: Returns `True` if at least one of the conditions is `True`.
    ```python
    a = 5
    b = 3
    c = 7
    
    result = (a > b) or (a > c)  # result is True (first condition is True)
    result2 = (a < b) or (a < c)  # result is True (second condition is True)
    ```

    3. **NOT (`not`)**: Reverses the result of the condition. If a condition is `True`, it returns `False`, and vice versa.
    ```python
    a = 5
    b = 3
    
    result = not (a > b)  # result is False (because a > b is True, and not reverses it)
    result2 = not (a < b)  # result is True (because a < b is False, and not reverses it)
    ```

    