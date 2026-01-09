# Write a program to access the first and last 
# element in a list.


def remove_duplicate(list):
    result=[] # creates ann empty list result
    seen = set()  
    # This seen set is used to keep track of 
    # elements that have already been encountered as 
    # the program iterates over the original list.
    for item in list:
        if item not in seen :
            result.append(item)
            seen.add(item)
    return result
orinal_list=[2,2,2,2,4,6,7,8,8,54,21,35,]
no_duplicates = remove_duplicate(orinal_list)
print("Original list:",orinal_list)
print("List after removing duplicates:",no_duplicates)