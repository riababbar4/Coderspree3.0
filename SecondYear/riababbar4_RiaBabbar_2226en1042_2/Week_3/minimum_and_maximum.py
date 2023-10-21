# Input the size of the array
N = int(input())

# Input the array elements
A = list(map(int, input().split()))

# Initialize variables to store the maximum and minimum
max_element = A[0]
min_element = A[0]

# Iterate through the array to find the maximum and minimum elements
for num in A:
    if num > max_element:
        max_element = num
    if num < min_element:
        min_element = num

# Print the maximum and minimum elements
print("Maximum element:", max_element)
print("Minimum element:", min_element)