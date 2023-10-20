def power(x, n):
    result = 1.0
    if n < 0:
        x = 1 / x
        n = -n
    while n:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result