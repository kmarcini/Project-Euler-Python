###########################
#
# #1 Multiples of 3 or 5 - Project Euler
# https://projecteuler.net/problem=1
#
# Code by Kevin Marciniak
#
###########################

# limit = 10
limit = 1000
answer = 0

for x in range(0, limit):
    if x % 3 == 0:
        answer += x
    elif x % 5 == 0:
        answer += x

print(answer)
