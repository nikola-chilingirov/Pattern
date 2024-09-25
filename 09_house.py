import math
n = int(input())
n_row = math.floor((n + 1) / 2)
for row in range(0, n_row):
    if n % 2 == 0:
        print(f"{'-' * (n_row - row - 1)}{'**' * (row + 1)}{'-' * (n_row - row - 1)}")
    else:
        print(f"{'-' * (n_row - row - 1)}*{('**' * row)}{'-' * (n_row - row - 1)}")
m_row = math.ceil((n + 1) / 2)
for m_row in range(1, m_row):
    print(f"|{'*' * (n - 2)}|")



#m_row = math.floor((n + 1) / 2)

    #print(f"{'_' * (n - m_row - 1)}*{'_' * (n - m_row)}")

