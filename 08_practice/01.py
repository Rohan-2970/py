# Write a program using functions to find greatest 
# of three numbers.

a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"The greatest number is a: {a}")
    elif(b>c and b>c):
        print(f"The greatest number is b: {b}")
    elif(c>b and c>a):
        print(f"The greatest number is c: {c}")

print(greatest(a,b,c))

