###########################
#
# #20 Factorial digit sum - Project Euler
# https://projecteuler.net/problem=20
#
# Code by Kevin Marciniak
#
###########################

from advanced_math import *

factToString = str(factorial(100))
sumOfDigits = 0

print(factToString)

for x in range(0, len(factToString)):
    sumOfDigits += int(factToString[x])

print(sumOfDigits)
