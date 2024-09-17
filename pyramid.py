# Write a Python program that prints a right-angled triangle using numbers. The user will provide the number of rows.

rows = int(input())

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
