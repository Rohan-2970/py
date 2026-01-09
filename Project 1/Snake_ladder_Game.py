import random
'''
1 Snake
-1 Water
0 Gun

'''
# we have used random to generate random numbers 
computer= random.choice([-1,1,0])
youstr = input("Enter your Choice: ")
# We have declared value of snake water and gun over ere 
youDict={"Snake": 1,"Water": -1,"Gun":0}
you = youDict[youstr]
reversedict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}
print(f"Your choice {youstr} and Computers choice {reversedict[computer]}")

if(computer==-1 and you == 1):
    print("You Win!!")
elif(computer==-1 and you == -1):
    print("Tiee!!")
elif(computer==-1 and you == 0):
    print("You Lose!!")
elif(computer== 1 and you == 1):
    print("Tieee!!")
elif(computer== 1 and you == -1):
    print("You Lose!!")
elif(computer==-1 and you == 0):
    print("You Win!!")
elif(computer==0 and you == 1):
    print("You Win!!")
elif(computer==0 and you == -1):
    print("You Lose!!")
elif(computer==0 and you == 0):
    print("Tiee!!")
else:
    print("Something went wrong")

# In this area the whole cod e is 
# compresed to a shor version and comressed 
# if(computer == you):
    # print("It's a draw")
# else:
#   if((computer - you) == -1 or (computer - you) == 2 ):
# print("you lose")
# else:
# print("you win!!")