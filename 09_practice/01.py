# 1.Write a program to read the text from a given 
# file 'poems.txt' and find out whether it contains 
# the word 'twinkle'.

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\poem.txt")as f:
    c= f.read()
    if("twinkle" in c):
     print("twinkle is prent in c")
    else:
       print("not present")