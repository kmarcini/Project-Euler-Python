###########################
# Reused math modules
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

