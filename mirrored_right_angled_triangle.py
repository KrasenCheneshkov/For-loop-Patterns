# Craft a Python script to print a mirrored right-angled triangle pattern.
# The user provides the number of rows.
rows = int(input())

for i in range(rows - 1, -1, -1):
    print(' ' * i + '*' * (rows - i))
