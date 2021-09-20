###########################
#
# #19 Counting Sundays - Project Euler
# https://projecteuler.net/problem=19
#
# Code by Kevin Marciniak
#
###########################

numOfSundays = 0
currentDay = 3  # 1 Jan 1901 = Tuesday

for x in range(1901, 2000):
    if x % 4 == 0:
        for y in range(0, 366):
            currentDay += 1
            if currentDay == 7:
                currentDay = 0
                if y in (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 336) and currentDay == 0:
                    numOfSundays += 1
    else:
        for y in range(0, 365):
            currentDay += 1
            if currentDay == 7:
                currentDay = 0
                if y in (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335) and currentDay == 0:
                    numOfSundays += 1

print(numOfSundays)
