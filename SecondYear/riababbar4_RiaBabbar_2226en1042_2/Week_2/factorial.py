import math

def find_factorial_numbers(n):
    factorial_numbers = []
    i = 1
    while True:
        factorial = math.factorial(i)
        if factorial <= n:
            factorial_numbers.append(factorial)
            i += 1
        else:
            break
    return sorted(factorial_numbers)

# Example usage:
n = 100  # You can replace this with any positive integer.
result = find_factorial_numbers(n)
print(result)