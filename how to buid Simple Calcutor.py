while true:
a = 0:
print('''
Simple Calculator 
+ADD
-SUBTRACT
*MULTIPLY
/DIVIDE''')
num1=float(input("Enter the value1:- "))
num2=float(input("Enter the value2:- "))
opr=input("Enter The Operator:- ")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1 - num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid opr...")
user_choice = input('To use calculator Type yes or No')
if user_choice == 'yes':
   continue
elif user_choice == 'no'
   a += 1
   if a == 1:
    break
else:
    print('please enter valid operation')
