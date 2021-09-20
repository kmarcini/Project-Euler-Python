###########################
#
# #5 Smallest multiple - Project Euler
# https://projecteuler.net/problem=5
#
# Code by Kevin Marciniak
#
###########################

# limit = 10
limit = 20
found = False
num = 0

while not found:
    num += 1
    found = True
    for i in range(1, limit):
        if not (num % i == 0):
            found = False
            break

print(num)
