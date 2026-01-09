# 4. A file contains a word "Donkey" multiple times.
#  You need to write a program which replace this 
# word with ##### by updating the same file.


word = "Donkey"

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\file5.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open(r"C:\Users\HP\OneDrive\Desktop\py\09_practice\file5.txt", "w") as f:
    f.write(contentNew)