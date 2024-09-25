### 1. **String Basics**
A string in Python is a sequence of characters enclosed within either single (`' '`) or double (`" "`) quotes.

Example:
```python
text = "Hello, World!"
```

### 2. **Concatenation**
String concatenation is the process of joining two or more strings together. In Python, you can concatenate strings using the `+` operator.

Example:
```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # Adds a space between "Hello" and "World"
print(result)  # Output: Hello World
```

### 3. **Basic String Methods**

- **`upper()`**: Converts all the characters in a string to uppercase.
  
  Example:
  ```python
  text = "hello"
  print(text.upper())  # Output: HELLO
  ```

- **`lower()`**: Converts all the characters in a string to lowercase.
  
  Example:
  ```python
  text = "HELLO"
  print(text.lower())  # Output: hello
  ```

- **`title()`**: Converts the first character of each word in a string to uppercase and the rest to lowercase.
  
  Example:
  ```python
  text = "hello world"
  print(text.title())  # Output: Hello World
  ```

### 4. **Combining Methods with Concatenation**
You can combine string methods with concatenation to format strings dynamically.

Example:
```python
first_name = "john"
last_name = "doe"
full_name = first_name.title() + " " + last_name.title()
print(full_name)  # Output: John Doe
```

Here are some basic string manipulations you can perform using Python:

    ### 1. **Remove Whitespaces**
    - **`strip()`**: Removes leading and trailing whitespaces.
    
    Example:
    ```python
    text = "  hello world  "
    clean_text = text.strip()
    print(clean_text)  # Output: "hello world"
    ```

    - **`lstrip()`**: Removes leading (left) whitespaces.
    
    Example:
    ```python
    text = "  hello"
    print(text.lstrip())  # Output: "hello"
    ```

    - **`rstrip()`**: Removes trailing (right) whitespaces.
    
    Example:
    ```python
    text = "world   "
    print(text.rstrip())  # Output: "world"
    ```

    ### 2. **String Length**
    - **`len()`**: Returns the number of characters in the string (including spaces).
    
    Example:
    ```python
    text = "Hello"
    print(len(text))  # Output: 5
    ```

    ### 3. **Replace Substrings**
    - **`replace(old, new)`**: Replaces occurrences of a substring with another substring.
    
    Example:
    ```python
    text = "I like apples"
    new_text = text.replace("apples", "bananas")
    print(new_text)  # Output: I like bananas
    ```

    ### 4. **Find a Substring**
    - **`find(substring)`**: Returns the index of the first occurrence of the substring. Returns `-1` if not found.
    
    Example:
    ```python
    text = "Hello World"
    index = text.find("World")
    print(index)  # Output: 6
    ```

    ### 5. **Substring Extraction (Slicing)**
    You can extract parts of a string using slicing.
    - **Syntax**: `string[start:end]`

    Example:
    ```python
    text = "Hello World"
    sub_text = text[0:5]  # Extract characters from index 0 to 4
    print(sub_text)  # Output: Hello
    ```

    ### 6. **Check Start or End of String**
    - **`startswith(substring)`**: Checks if the string starts with the specified substring.
    
    Example:
    ```python
    text = "Python programming"
    print(text.startswith("Python"))  # Output: True
    ```

    - **`endswith(substring)`**: Checks if the string ends with the specified substring.
    
    Example:
    ```python
    text = "Python programming"
    print(text.endswith("programming"))  # Output: True
    ```

    ### 7. **Split a String**
    - **`split(separator)`**: Splits a string into a list of substrings based on the separator.
    
    Example:
    ```python
    text = "apple,banana,cherry"
    fruits = text.split(",")  # Split by comma
    print(fruits)  # Output: ['apple', 'banana', 'cherry']
    ```

    ### 8. **Join a List into a String**
    - **`join(iterable)`**: Joins elements of a list into a single string with a specified separator.
    
    Example:
    ```python
    fruits = ['apple', 'banana', 'cherry']
    result = ", ".join(fruits)
    print(result)  # Output: apple, banana, cherry
    ```

