#Write a program to categorize a number into different ranges(eg: 1-10, 11-20)
num = int(input("Enter a number - "))
if num >= 1 and num <= 10:
    print("First Line")
elif num >= 11 and num <= 20:
    print("Second Line")
else:
    print("Over limit")