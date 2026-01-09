a=int(input("Enter a number: "))
i=1
while (i<11):
    print(f"{a}X{i}={a*i}")
    i+=1

# 1. i += 1
# This is the correct and most common way to increment
#  a value.

# 2. i + 1
# This is just an expression — it adds 1 to i, but 
# it does not store the result back in i.

# 3. i = +1
# This is not an increment at all.
# You're just assigning +1 (which is the same as 1) to i.