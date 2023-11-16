# # # swap solution 1
# # # x = 10
# # # y = 12
# # # temp = x
# # # print("The value of temp variable is,", temp)
# # # x = y
# # # print("the value of x is ",x)
# # #
# # # y = temp
# # # # print("the value of y is ",y)
# # #
# # # # solution 2
# # # x = 10
# # # y = 12
# # #
# # # x,y=y,x
# # # print("the vaule of x is", x)
# # # print("the value of y is", y)
# #
# #
# #
# # # random number choice
# # # import random
# # # x=random.randint(0,10)
# # # print(x)
# #
# #
# #
# # # # convert kilometers to miles
# # # # 1 Kilometers = 0.621371 miles
# # #
# # # km = float(input("enter your value in kms:- "))
# # # miles=(0.621371)*km
# # #
# # # print(km, "km in miles will be", miles, "miles")
# #
# # # celsius = int(input("enter temperature in celsius:-  "))
# # # fahrenheit =(celsius * (9/5))+32
# # # print("the converted value is:-" , fahrenheit,"fahrenheit")
# # # print(0b1011001100)
# # # 1024 512 256 128 64 32 16 8 4 2 1
# # print(bin(400))
# #
# # print(int(0b110010000))
# # print(0b100101)
# 
# print(0x41)
# print(bin(0x47))
# print(hex(0b1001011))
# 
# print(len("Welcome\nto\nSuresh"))

# # leatn about \\
# print("m\f")
# m
# print("mx\\f")
# m\f


# # even or odd numbers
# n=25
# if n %2==0:
#     print("Even Number")
# else:
#     print("odd number")

# leap year check
#
# year=int(input("enter a year:- "))
# if (year % 400==0) and (year % 100==0):
#               print(year,"is a Leap year")
#
# elif (year % 4==0) and(year % 100 !=0):
#     print(year, "is a Leap year")
#
# else:
#     print(year,"is not a leap year")


# solution 1
# using conditional statement
# num1 = int(input("enter your number:- "))
# num2 = int(input("enter your number:- "))
# num3 = int(input("enter your number:- "))
#
# if (num1 > num2) and (num1 > num3):
#     print(num1, "is a largest number")
#
# elif (num2 > num1) and (num2 > num3):
#     print(num2, "is the largest number")
#
# else:
#     print(num3, "is the largest number")



# Check Prime numbers
#
# num= int(input("enter your number here:-  "))
# if num == 1:
#     print(num, " is not a prime number")
# if num > 1:
#  for i in range(2,num):
#     if num%i ==0:
#         print(num, "is not prime number")
#         break
#     else:
#         print(num,"is prime number")
# lower = int(input("enter lower limit here:- "))
# upper = int(input("enter upper limit here:- "))
#
# for i in range(lower,upper+1):
#     if i > 1:
#         for a in range(2,i):
#             if i%a == 0:
#                 break
#             else:
#                 print(i)

# print("Ram  900".expandtabs(tabsize=50))
# print("shyam    800".expandtabs(tabsize=50))
# print("narayan krishna  700".expandtabs(tabsize=50))

# l=[]
#  for i in range(1,21):
#     l.append(i)
#     print(l)
# a=[]
# d=[m for m in range(1,21)]
# print(d)
# output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# l=[]
# d=[m for m in range(1,21) if m%2==0]
# print(d)
# # output [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# l=[1,2,6,10,30,20,5]
# l.sort()
# print(l)
# # output [1, 2, 5, 6, 10, 20, 30]
# print(l[-1::-1])
# # output


# factorial solution
# num=int(input("enter a number:- "))
# fac=1
# if num < 0:
#     print("factorial of 0 does not exit")
# if num == 0:
#     print("factorial of 0 is",1)
# if num > 0:
#  for i in range(1,num+1):
#     fac= fac * i
#     print("the factorialof the given number is",fac)

# import math
# num=int(input("enter a number:- "))
# fac=math.factorial(num)
# print(fac)

# Recursion method of factorial
# def fact(a):
#     if a==0:
#      return 1
#     else:
#        return((a)*fact(a-1))
# num=int(input("enter here number:- "))
# result=fact(num)
# print("the given number factorial is:-",result)

# l=[]
# for i in range(0,51):
# #     l.append(i)
# #     print(l)
#
# l=[m for m in range(0,26)]
# print(l)
# # output[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#
# l="welcome to suresh lama"
# print(l[0::])
# print(l[-1::-1])
# # welcome to suresh lama
# # amal hserus ot emoclew

# test = [10,20,40,30,70]
# test.sort()
# print(test)
# test[4] = 50
# print(test)
# test.pop(4)
# print(test)
# # test.append(60)
# # print(test)
#
#
# # loop function using
#
# # num = 7
# # for i in range(1,11):
# #     print(num,"x",i, "=", num*i)
#
# num2 = 7
# i =1
# while i <= 10:
#     print(num2, "x", i, "=", num2 * i)
#     i +=1

# Fibonancci  sequence:
#
# class Employee:
#     def __init__(self,name,age,address,mobile):
#         self.name = None
#         self.age = None
#         self.address = None
#         self.mobile = None
#     def show_details(self):
#         print("Employee name is:- ",self.name)
#         print("Employee age is:- ",self.age)
#         print("Employee address is:- ",self.address)
#         print("Employee number is:- ",self.mobile)
#
# setting_details = Employee("suresh",30,"bhaktapur",9818506375)
# setting_details.show_details()


# # Fibonacci Sequence
# a_num = 0
# b_num = 1
# num = int(input("Enter number here"))
#
# if num == 1:
#     print(a_num)
# else:
#     print(a_num)
#     print(b_num)
#     for i in range(1,num+1):
#         c =a_num + b_num
#         a_num = b_num
#         b_num = c
#         print(c)

#
# # Armstrong Number
# num = int(input("Enter number here: "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp%10
#     cube = digit**3
#     sum = sum + cube
#     temp //= 10
#
# if sum == num:
#     print("it is a armstrong number")
# else:
#     print("it is a not armstrong number")


# SIP Calculator


# class SipCalculater:
# 
#     def __init__(self):
#         self.monthly_investment = mont
#         self.annual_interest_rate = 0
#         self.investment_period = investment_period
#     def sip_calculation(self):
#         self.sip_amount = int(input("Enter here your monthly amount: "))
#         self.sip_year = int(input("Enter here your investing periods"))
#         for i in range(1,self.sip_year):


# class BikeRent:
#     def __init__(self,bike_stocks):
#         self.bike_stocks = bike_stocks
#
#     def show_stocks_bikes(self):
#         print("Total available bike for rent is: ",self.bike_stocks)
#         print("Bike rent Rs: 100 per each")
#
#     def bike_rent_quantity(self,quantity):
#         if quantity <= 0:
#             print("Enter order greater than zero")
#         elif quantity > self.bike_stocks:
#             print("Not available that amount order in stocks",)
#         else:
#             self.bike_stocks = self.bike_stocks - quantity
#             print("You bike order amount is", quantity * 100)
#             print("Total bike available for rent: ",self.bike_stocks)
# while True:
#  bikerent=BikeRent(100)
#  user_input = int(input('''
#         1. Check available bikes for rent
#         2. Take a bike
#         3. Exit
#            '''))
#  if user_input == 1:
#                  bikerent.show_stocks_bikes()
#  elif user_input == 2:
#                 quantity = int(input("How many you want bike for a rent: "))
#                 bikerent.bike_rent_quantity(quantity)
#  else:
#     break

#
#
# number = int(input("Enter number here: "))
#
# if number < 0:
#     print("enter positive or greater than zero")
# else:
#  sum = 0
# while number > 0:
#     sum += number
#     number -= 1
# print(sum)



# # Python program to display powers of 2 using anonymous function( lambda function)
#
# nterms = int(input("enter number of terms here: "))
#
# result = list (map(lambda x :2**x,range(nterms+1)))
# # print(result)
# for i in range(nterms+1):
#     print("the value of 2 raised to power", i,"is",result[i])

#
# # Python program to find number divisible by another number solution 1
# print("The number divisible by 13 are: ")
# for i in range(1,101):
#     if i % 13 == 0:
#      print(i)
#
# # solution 2 using lambda function and filter()
# #
# l = [39,48,26,98,33,67,87]
# result = list(filter(lambda x : x % 13 == 0,l))
# print("the number divisible by 13 are",result)

# num1 = int(input("Enter number here: "))
#
# print('even number'if num1 %2 == 0 else 'odd')

Name = int(input('Enter number here: '))

if Name >= 18:
    print("You can vote")
elif Name == 17:
    print('Wait for one more year')
else:
    print("You can't vote" )