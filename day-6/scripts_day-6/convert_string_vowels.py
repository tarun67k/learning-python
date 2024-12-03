string = "Hello World"
vowels = "aeiouAEIOU"
result = ""
for char in string:
    if char in vowels:
        result += "*"
    else:
        result += char 
print(result)