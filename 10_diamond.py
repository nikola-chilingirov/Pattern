import math
n = int(input())
leftRight = math.floor((n - 1) / 2)
mid = (n - 2) * leftRight - 2
if mid >= 0:
    for row in range(0, n):
        print(f"{'-' * (leftRight - row)}**{'-' * (leftRight - row)}")

