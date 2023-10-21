def rearrange_positive_negative(arr, N):
    # Initialize two pointers: one at the beginning and one at the end
    left = 0
    right = N - 1

    while left <= right:
        # If the left pointer points to a positive element, move it to the right
        if arr[left] > 0:
            left += 1
        # If the right pointer points to a negative element, move it to the left
        elif arr[right] < 0:
            right -= 1
        # If the left pointer points to a negative element and the right pointer points to a positive element, swap them
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Example usage:
N = 8
arr = [12, 11, -13, -5, 6, -7, 5, -3]
rearrange_positive_negative(arr, N)
print(arr)