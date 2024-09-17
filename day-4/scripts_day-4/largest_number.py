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

