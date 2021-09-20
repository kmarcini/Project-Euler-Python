###########################
# Project Euler Problem 21
# Factorial digit sum
#
# Code by Kevin Marciniak
###########################

def sumproperdivisors(num):
    sum = 0
    for x in range(1, int((num / 2)) + 1):
        if num % x == 0:
            sum += x

    return sum


amicableList = []

for x in range(0, 10000):
    temp = sumproperdivisors(x)
    if sumproperdivisors(temp) == x and sumproperdivisors(x) == temp and temp != x:
        if x not in amicableList and temp not in amicableList:
            amicableList.insert(len(amicableList), x)
            amicableList.insert(len(amicableList), temp)

totalSum = 0

for y in range(0, len(amicableList)):
    totalSum += amicableList[y]

print(totalSum)
