def is_armstrong_number(n):
    # Convert the integer to a string to calculate the number of digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # Initialize the sum of the digits raised to the power of the number of digits
    total = 0

    # Calculate the Armstrong number sum
    for digit in num_str:
        total += int(digit) ** num_digits

    # Check if the total is equal to the original number
    return total == n

# Example usage:
n = int(input("Enter an integer: "))
if is_armstrong_number(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")