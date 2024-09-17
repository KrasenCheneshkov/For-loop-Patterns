#Write a Python script that displays a diamond pattern based on the number of rows (height) specified by the user.

height = int(input())

if height % 2 == 0:
    height -= 1
#The program is adjusted to work with even numbers, where it takes the previous highest odd number to create the pattern. 

for i in range(1, height + 1, 2):
    print(' ' * ((height - i) // 2) + '*' * i)
for i in range(height - 2, 0, -2):
    print(' ' * ((height - i) // 2) + '*' * i)
