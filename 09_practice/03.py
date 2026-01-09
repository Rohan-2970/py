# 3. Write a program to generate multiplication 
# tables from 2 to 20 and write it to the different 
# files. Place these files in a folder for a 13-year 
# old.
import os
# Create folder named "tables"

os.makedirs("tables", exist_ok=True)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}", "w") as f:
        f.write(table)


# this code will not work because no folder named 
# tables exist we need to create a folder useng os.markedirs()

for i in range(2, 21):
    generateTable(i)
    