# Design a Python code snippet to print a left-angled triangle pattern. The user should provide the number of rows.

rows = int(input())

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print('*', end='')
    print()
