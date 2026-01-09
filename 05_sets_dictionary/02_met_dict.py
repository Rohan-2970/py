# items will be printed 
a= {
    "rohan" : [809,43,454],
    "ghkh" : "hjrg",
    "eghh" : 897

    }
# print(a.items())
# -- items will be printed
print(a.keys())
# keys will be printed 
print(a.values())
len(a)
# values will be printed 
a.update({"rohan":879})
# to update the dictionary 
print(a)


# get method
print(a.get("rohan")) # both are same but  
print(a["rohan"])  

print(a.get("rohan5"))  #Prints None
print(a["rohan5"]) #Returns an error 

# chatgpt python dic. methods 
# pop method & pop item 