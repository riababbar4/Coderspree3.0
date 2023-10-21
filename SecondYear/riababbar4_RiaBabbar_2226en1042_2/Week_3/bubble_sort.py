def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize by checking if any swaps occur in a pass
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred in this pass, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)