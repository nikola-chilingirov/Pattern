import math
n = int(input())
print(f"{'*' * (2 * n)}{' ' * n}{'*' * (2 * n)}")
for i in range(1, n - 1):
    if i == math.floor((n - 1) / 2):
        print(f"*{'/' * ((2 * n) - 2)}*{'|' * n}*{'/' * ((2 * n) - 2)}*")
    else:
        print(f"*{'/' * ((2 * n) - 2)}*{' ' * n}*{'/' * ((2 * n) - 2)}*")
print(f"{'*' * (2 * n)}{' ' * n}{'*' * (2 * n)}")