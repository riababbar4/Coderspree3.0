def find_num_index(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
arr = [1, 2, 3, 4, 5]
num = 3
result = find_num_index(arr, num)
print(result)  # This will print 2 since 3 is at index 2 in the array.