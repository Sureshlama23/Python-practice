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
