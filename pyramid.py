# Create a Python script that prints a pyramid pattern based on the user-input number of rows.

rows = int(input())

for i in range(rows):
    print(" " * (rows - i) + "*" * (2 * i + 1))

