#write a while loop that keeps asking the user for input until they type "exit".

x = True
while x:
    user = input("Enter input string - ")
    if user.lower() == "exit":
        print("exit")
        x = False