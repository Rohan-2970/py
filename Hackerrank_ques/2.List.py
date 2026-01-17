# You are given the scores of participants in a University Sports Day.
# The first line contains an integer n, which represents the number of scores.
# The second line contains n space-separated integers, representing the scores.

# Your task is to find and print the runner-up score, which means the second highest score.
# If the highest score appears more than once, it should be considered only once.

# Input

# An integer n (number of scores)

# A list of n integers (scores)

# Output

# Print the runner-up (second highest) score

# Example

# Input

# 5
# 2 3 6 6 5


# Output

# 5


# Explanation
# The highest score is 6. After removing it, the next highest score is 5, which is the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique = list(set(arr))
    unique.remove(max(unique))
print(max(unique))