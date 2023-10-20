def generate_sequence(n):
    if n < 1:
        return []
    else:
        # Recursively generate the sequence and append the current number
        return generate_sequence(n - 1) + [n]

# Example usage:
n = int(input("Enter a number: "))
sequence = generate_sequence(n)
print(sequence)