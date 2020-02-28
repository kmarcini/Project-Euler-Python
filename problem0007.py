###########################
# Project Euler Problem 7
# 10001st prime
#
# Code by Kevin Marciniak
###########################

from math import *


def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        test = 3
        while test <= sqrt(num):
            if (num % test) == 0:
                return False
            test += 2
        else:
            return True


# limit = 6
limit = 10_001
prime_list = []
num = 2

while len(prime_list) < limit:
    if is_prime(num):
        prime_list.append(num)
        num += 1
    else:
        num += 1

print(prime_list[-1])
