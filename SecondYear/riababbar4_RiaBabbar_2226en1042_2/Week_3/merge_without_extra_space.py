def merge_sorted_arrays(arr1, arr2, N, M):
    i = N - 1  # Index to traverse arr1 from the end
    j = 0      # Index to traverse arr2 from the beginning

    # Iterate through both arrays in reverse order
    while i >= 0 and j < M:
        # If the current element of arr1 is greater than the current element of arr2
        if arr1[i] > arr2[j]:
            # Swap the elements of arr1 and arr2
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        else:
            break

    # Sort both arrays (arr1 is already sorted, so we sort arr2 only)
    arr1.sort()
    arr2.sort()

# Example usage:
N = 4
M = 3
arr1 = [1, 3, 5, 7, 0, 0, 0]
arr2 = [2, 4, 6]
merge_sorted_arrays(arr1, arr2, N, M)
print("Merged arr1:", arr1[:N])
print("Merged arr2:", arr2)