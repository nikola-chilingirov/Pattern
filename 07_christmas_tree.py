n = int(input())
for i in range(0, n + 1):
    print(f"{' ' * (n - i)}{'*' * i} | {'*' * i}{' ' * (n - 1)}")
