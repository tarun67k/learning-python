* CONTROL FLOW : 
    Control flow refers to the order in which the statements or instructions in a program are executed. In Python, control flow is determined by conditional statements, loops, and other control structures that direct the flow of execution based on certain conditions or repetitions.

Here are the main control flow mechanisms in Python:

1. Conditional Statements (if-else)
    Conditional statements allow a program to execute certain blocks of code only if specific conditions are met.

    if: Executes a block of code if the condition is True.
    elif: (else if) Adds another condition if the previous one is False.
    else: Executes a block of code if all the previous conditions are False.

Example:

    x = 10

    if x > 15:
        print("x is greater than 15")
    elif x > 5:
        print("x is greater than 5 but less than or equal to 15")
    else:
        print("x is 5 or less")