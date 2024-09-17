#Develop a Python script that generates a right-angled triangle pattern. 
#The script should prompt the user to specify the number of rows. Here's a sample output for a user input of 5:
# *
# **
# ***
# ****
# *****

rows = int(input())

for i in range(1, rows + 1):
    for j in range(1, i +1):
        print('*', end='')
    print()
