###########################
#
# #7 10001st prime - Project Euler
# https://projecteuler.net/problem=7
#
# Code by Kevin Marciniak
#
###########################

from advanced_math import *

# limit = 6
limit = 10_001
prime_list = [2]
num = 3

while len(prime_list) < limit:
    if is_prime(num):
        prime_list.append(num)
        num += 2
    else:
        num += 2

print(prime_list[-1])
