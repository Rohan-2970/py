f= open(r"C:\Users\HP\OneDrive\Desktop\py\09_Input+Output\file.txt")

# lines= f.readlines() 
#it will read the lines one by one all 

# print(lines, type(lines))
lines=f.readline()
while(lines != ""):
    print(lines)
    lines = f.readline()
f.close

