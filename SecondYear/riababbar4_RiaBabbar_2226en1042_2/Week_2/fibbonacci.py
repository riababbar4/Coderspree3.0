def generate_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_generator = generate_fibonacci(n)

for number in fibonacci_generator:
    print(number, end=' ')