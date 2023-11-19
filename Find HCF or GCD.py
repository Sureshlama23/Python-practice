"""
find HCF OR GCD in python 
"""
def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if (x%i == 0) and (y%i ==0):
            hcf = i
    return(hcf)
print("ther hcf of the given two numbers is:",findHCF(12,30))


num = int(input('enter your number here:'))
num2 = int(input('enter your number here:'))
if num > num2:
    smaller = num2
else:
    smaller = num
for i in range(1,smaller+1):
    if (num%i == 0) and (num2%i ==0):
        hcf =i
print('ther hcf of the given two numbers:', hcf)