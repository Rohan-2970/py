# RAM --> Volatile

# put r before the file path bec. it will then identify it as a raw string
f = open(r"C:\Users\HP\OneDrive\Desktop\py\09_Input+Output\file.txt")
data = f.read()
print(data)
f.close()
