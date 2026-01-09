# a=12
# b= 34
# c=345
# average=(a+b+c)/2
# print(average)

# agar yehi avg bahut baar nikalna ho toh functn ka 
# use karo
# ye peice of logic k se karo 

#  Function Defination 
def avg():
    a=int(input("Enter a Number: "))
    b=int(input("Enter a Number: "))
    c=int(input("Enter a Number: "))
    average = (a+b+c)/3
    print(average)
 
    # here we have declared a function but we didn't do function calling 
avg()  # Function call
print("Thank You")

# A function is a group of statements performing a specific task.

# When a program gets bigger in size and its complexity grows, it gets 
# difficult for a program to keep track on which piece of code is doing what!

# A function can be reused by the programmer in a given program any number of

# EXAMPLE AND SYNTAX OF A FUNCTION

# The syntax of a function looks as follows:

# def func1():

# print("hello")

# This function can be called any number of times, anywhere in the program.

# FUNCTION CALL
# Whenever we want to call a function, we put the name of the function followed by parentheses as follows:

# func1() 
# This is called function call.