def count_divisor_digits(n):
    count = 0
    original_n = n

    while n > 0:
        digit = n % 10
        if digit != 0 and original_n % digit == 0:
            count += 1
        n //= 10

    return count

# Input a number
n = int(input("Enter a number: "))

result = count_divisor_digits(n)
print(f"The number of digits that evenly divide {n} is: {result}")