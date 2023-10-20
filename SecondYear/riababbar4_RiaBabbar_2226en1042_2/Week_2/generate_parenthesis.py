def generate_parentheses(N):
    def generate(partial, left, right):
        if len(partial) == 2 * N:
            result.append(partial)
            return
        if left < N:
            generate(partial + "(", left + 1, right)
        if right < left:
            generate(partial + ")", left, right + 1)

    result = []
    generate("", 0, 0)
    return result

N = int(input("Enter the number of pairs: "))
combinations = generate_parentheses(N)
for combination in combinations:
    print(combination)