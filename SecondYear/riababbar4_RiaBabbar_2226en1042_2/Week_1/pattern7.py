def printDiamond(n):
    # Upper part of the diamond
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

# Example usage with N = 5
printDiamond(5)