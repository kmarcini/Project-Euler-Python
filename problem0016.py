###########################
# Project Euler Problem 16
# Power digit sum
#
# Code by Kevin Marciniak
###########################

total = 0
# temp = 2**15
temp = 2**1000

for i in range(0, len(str(temp))):
    total += int(str(temp)[i])

print(total)
