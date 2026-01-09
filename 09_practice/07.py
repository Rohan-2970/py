# 7. Write a program to find out the line number
#  where python is present from ques 6.



with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\log.txt.html") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")