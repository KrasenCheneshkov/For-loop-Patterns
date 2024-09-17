# Craft a Python program that produces a square pattern with a hollow center. The program should take the size of the square as input from the user. Here's an example output for a user input of 5:
rows = int(input())

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or i == rows:
            print('*', end='')
        else:
            if j == 1 or j == rows:
                print('*', end='')
            else:
                print(' ', end='')
    print()

