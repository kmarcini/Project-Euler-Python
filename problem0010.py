###########################
# Project Euler Problem 10
# Summation of primes
#
# Code by Kevin Marciniak
###########################

from advanced_math import *

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
