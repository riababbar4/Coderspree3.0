# Input the number of test cases
T = int(input())

for _ in range(T):
    # Read N and X for the current test case
    N, X = map(int, input().split())

    # Read the marks of all students
    marks = list(map(int, input().split()))

    # Sort the marks in descending order
    marks.sort(reverse=True)

    # Calculate the maximum passing mark
    max_passing_mark = marks[X - 1]

    # Print the result for this test case
    print(max_passing_mark)