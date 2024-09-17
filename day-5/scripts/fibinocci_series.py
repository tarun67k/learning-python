<<<<<<< HEAD
#Use a loop to print the Fibonacci sequence up to a certain number

limit = int(input("Enter a number - "))  # You can change this value

a = 0
b = 1
f = [a,b]
for i in range(limit):
    c = a+b 
    f.append(c)
    a = b 
    b = c 
print(f)
print(f[limit])
print(sum(f))

=======
#Use a loop to print the Fibonacci sequence up to a certain number

limit = int(input("Enter a number - ")) 
a = 0
b = 1
f = [a,b]
for i in range(limit):
    c = a+b 
    f.append(c)
    a = b 
    b = c 
print(f)
print(f[limit])
print(sum(f))

>>>>>>> af1e3dd7198a27f68fa793de051a5d3bed4c20d6
