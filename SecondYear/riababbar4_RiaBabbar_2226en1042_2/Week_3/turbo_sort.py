# Input the number of integers in the list
N = int(input())

# Initialize an empty list to store the integers
numbers = []

# Input the elements of the list
for _ in range(N):
    num = int(input())
    numbers.append(num)

# Sort the list in non-decreasing order
sorted_numbers = sorted(numbers)

# Output the sorted numbers
for num in sorted_numbers:
    print(num)