'''This is code for get factor of a number in python'''

user_num = int(input('enter a number here: '))

for i in range(2,user_num+1):
    if (user_num%i ==0):
        print(i)