###########################
# Project Euler Problem 10
# Summation of primes
#
# Code by Kevin Marciniak
###########################

from math import *


def is_prime(prime_test):
    if prime_test <= 1:
        return False

    if prime_test == 2 or prime_test == 3:
        return True
    if prime_test % 2 == 0:
        return False
    if prime_test % 3 == 0:
        return False

    i = 5
    sqrt_prime_test = sqrt(prime_test)
    while i <= sqrt_prime_test:
        if (prime_test % i) == 0 or (prime_test % (i + 2)) == 0:
            return False
        i += 6

    return True


# limit = 10
limit = 2_000_000
prime_list = [2]
num = 3

while num < limit:
    if is_prime(num):
        prime_list.append(num)
        num += 2
    else:
        num += 2

sum = 0

for i in range(0, len(prime_list)):
    sum += prime_list[i]

print(sum)
