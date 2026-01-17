# You are given four integers x, y, z, and n. Generate all possible coordinates [i, j, k] such that 0 ≤ i ≤ x, 0 ≤ j ≤ y, and 0 ≤ k ≤ z, using list comprehension. Exclude the coordinates where the sum i + j + k is equal to n. Print the resulting list.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i,j,k]
    for i in range (x+1)
    for j in range (y+1)
    for k in range (z+1)
    if i+j+k != n]
print(result)

