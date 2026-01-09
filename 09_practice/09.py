# 9. Write a program to find out whether a file 
# is identical & matches the content of another file.

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\this.txt") as f:
    c1 = f.read()
   
with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\ques9.txt") as f:
    c2 = f.read()

if(c1 == c2):
    print("Print ye these files are identical")

else:
    print("no thse files are not identical")
