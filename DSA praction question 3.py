# 3. Create a list of all odd numbers between 1 and a max number. Max number is something you
#  need to take from a user using input() function

user_num = int(input("enter your number: "))
list = []
for i in range(1,user_num+1):
    if i%2 != 0:
        list.append(i)
print(list)