# comparison = relational operators 
# ==,>=,<=
# Logical operators 
# and,or,not
# both agree then agreee , anyone agree agree , agree convert to not agree vis a vis 
a=int(input("Enter your age : "))

if(a%2==0):
    print("NO ENTERED IS EVEN ")
if(a>18):
    print("You are above the age of consent: ")

elif(a==0):
    print("the age enterd is equal to 0 which is not possible ")

elif(a<0):
    print("The age entered is invalid ") 

else:
    print("You are below the age of consent: ")
    
# this is a __ if elif else ladder 
print("end of the program ")