# 6. Write a program to mine a log file and find 
# out whether it contains 'python'.

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\log.txt.html") as f:
    c = f.read()

if("python" in c):
    print("Yes python is present")
else:
    print("No Python is not present")