###########################
# Project Euler Problem 1
# Multiples of 3 and 5
#
# Code by Kevin Marciniak
###########################

i = 0
# limit = 10
limit = 1000
answer = 0

while i < limit:
    if i % 3 == 0:
        answer += i
    elif i % 5 == 0:
        answer += i
    i += 1

print(str(answer))
