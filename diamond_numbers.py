# Write a Python program that prints a diamond shape pattern with numbers.
# The user provides the number of rows for the top half of the diamond.

rows = int(input())

for i in range(rows + 1):
    print(' ' * (rows - i), end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()
for i in range(rows - 1, -1, -1):
    print(' ' * (rows - i), end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()
