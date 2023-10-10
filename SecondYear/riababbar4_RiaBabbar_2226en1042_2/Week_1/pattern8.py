def printTriangle(n):
    for i in range(1, n + 1):
        # Left side of the triangle
        for j in range(1, i + 1):
            print(j, end=" ")

        # Spaces in the middle
        for j in range(2 * n - 2 * i):
            print(" ", end=" ")

        # Right side of the triangle
        for j in range(i, 0, -1):
            print(j, end=" ")

        print()
