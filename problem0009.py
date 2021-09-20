###########################
#
# #9 Special Pythagorean triplet - Project Euler
# https://projecteuler.net/problem=9
#
# Code by Kevin Marciniak
#
###########################

total = 1000
product = 0

for c in range(1, 1000):
    for b in range(1, c):
        for a in range(1, b):
            if (a + b + c) == 1000:
                if ((a * a) + (b * b)) == (c * c):
                    product = a * b * c

print(product)
