n = int(input())
for row in range(1, n + 1):
    print(f"{' ' * (n - row)}*{' *' * (row - 1)}")
for row1 in range(1, n):
    print(f"{' ' * row1}*{' *' * ((n - 1) - row1)}")