def merge_sort(ARR, I, r):
    if I < r:
        # Choose a pivot element (e.g., the last element)
        pivot = ARR[r]
        i = I - 1

        for j in range(I, r):
            if ARR[j] < pivot:
                i += 1
                # Swap ARR[i] and ARR[j]
                ARR[i], ARR[j] = ARR[j], ARR[i]

        # Swap ARR[i + 1] and the pivot
        ARR[i + 1], ARR[r] = ARR[r], ARR[i + 1]

        # Recursively sort the sub-arrays before and after the pivot
        merge_sort(ARR, I, i)
        merge_sort(ARR, i + 2, r)

# Example usage:
ARR = [4, 2, 6, 1, 9, 3, 8]
I = 1
r = 5
merge_sort(ARR, I, r)
print(ARR)