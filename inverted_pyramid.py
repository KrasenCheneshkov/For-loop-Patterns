# Develop a Python script that prints an inverted pyramid pattern based on the number of rows provided by the user.

rows = int(input())

for i in range(rows - 1, - 1, -1):
    print(' ' * (rows - i) + '*' * (2 * i + 1))
