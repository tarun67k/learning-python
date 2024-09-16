#Write a program that checks if a number is positive or negative.
n = int(input("Enter a number - "))
if n > 0:
    print("It is a positive number")
elif n < 0:
    print("It is a negative number")
else:
    print("None")

#Create a program to check if a user is eligible to vote based on age(>= 18)
age = int(input("Enter age - "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

#Check if a number is even or odd.
number = int(input("Enter a number - "))
if number % 2 == 0:
    print("Number is even")
elif number % 2 == 1:
    print("Number is odd")
else:
    print("Invalid")

#Write a program to categorize a number into different ranges(eg: 1-10, 11-20)
num = int(input("Enter a number - "))
if num >= 1 and num <= 10:
    print("First Line")
elif num >= 11 and num <= 20:
    print("Second Line")
else:
    print("Over limit")

#Create a program to find the largest of three numbers entered by the user
a = int(input("Enter first number - "))
b = int(input("Enter second number - "))
c = int(input("enter third number - "))
largest = a 
if a > b :
    largest = a 
else:
    if b > a and b > c:
        largest = b 
    else:
        largest = c 

print(largest)


