def reverse_bits(n):
    reversed_n = 0
    for _ in range(32):
        reversed_n = (reversed_n << 1) | (n & 1)
        n >>= 1
    return reversed_n

def calculate_ticket_price(n):
    reversed_n = reverse_bits(n)
    ticket_price = reversed_n
    return ticket_price

# Input the 32-bit unsigned integer 'n'
n = int(input("Enter a 32-bit unsigned integer: "))

# Calculate the ticket price
ticket_price = calculate_ticket_price(n)

print(f"Ticket Price: {ticket_price}")