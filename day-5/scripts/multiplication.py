#write a program to print the multiplecation table of a number entered by the user.

n = int(input("Enter a number - "))
for i in range(1,11):
    x = n * i
    print(str(n) + " * " + str(i) + " = " + str(x))