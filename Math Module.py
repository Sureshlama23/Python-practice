import math
print("CEIL")
# Retun the ceiling of x,the smallest integer greater then or equal to x.
# If x is not a float , delegates to x.__ceil__(), which should return an integral value.
x=10.5
print(math.ceil(x))
output:11
x=13.1
print(math.ceil(x))
output:14
x=14
print(math.ceil(x))
output:14

print("MATH.FABS")
# Return the absulate value of x.
x=10
print(math.fabs(x))
output:10.0
x=-13.5
print(math.fabs(x))
output:13.5
x=12
print(math.fabs(x))
output:12

print("MATH.FACTORIAL")
# Return x factorial as an integer. Raises Value Error if x is not integral or is negative
X=4
print(math.factorial(4))
output:24
Example:4*3*2*1
x=7
print(math.factorial(x))
output:5040
Example:7*6*5*4*3*2*1

print("MATH.FLOOR")
# # Return the floor of x, the largest inger less than or equal to x.
# If x is not a float, delegates to x.__floor__(), which should return an integral value.

x=12.3
print(math.floor(x))
output:12
x=5.6
print(math.floor(x))
output:15

print("MATH.FSUM")
x=[10,20,30,50]
print(math.fsum(x))
output:110.0

print("MATH.SQRT")
print(math.sqrt(5))
output:2.23606797749979

print(math.sqrt(25))
output:5.0







