#Create a program to find the factorial of a number using loop.

num = int(input("Enter a number - "))
factorial = 1 
if num < 0:
    print("factorial is not defined for negitive numbers")
elif num == 0:
    print("factorial of number 0 is", factorial)
else:
    for i in range(1,num+1):
        factorial *= i 
    print("factorial of num is ",factorial)