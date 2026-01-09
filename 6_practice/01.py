# Write a program to find the greatest of four 
# numbers entered by the user.

a=int(input("Enter number a: "))
a1=int(input("Enter number a1: "))
a2=int(input("Enter number a2: "))
a3=int(input("Enter number a3: "))
a4=int(input("Enter number a4: "))
if(a>a1 and a>a2 and a>a3 and a>a4):
    print("Greatest number is a: ",a)
elif(a1>a and a1>a2 and a1>a3 and a1>a4):
        print("Greatest number is a1: ",a1)
elif(a2>a and a2>a1 and a2>a3 and a2>a4):
            print("Greatest number is a2: ",a2)

