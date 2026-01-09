# 8. Write a program to make a copy of a text file 
# "this, txt"

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\this.txt") as f:
    c= f.read()

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\this_copy.txt","w") as f:
    f.write(c)