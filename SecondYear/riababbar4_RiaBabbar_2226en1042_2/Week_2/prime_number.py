def is_prime(n):
    if n <= 1:
        return False  # 1 and numbers less than 1 are not prime

    if n <= 3:
        return True  # 2 and 3 are prime

    if n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # If n is divisible by any number from 5 to the square root of n, it's not prime
        i += 6

    return True

# Example usage:
n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")