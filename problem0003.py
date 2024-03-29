###########################
#
# #3 Largest prime factor - Project Euler
# https://projecteuler.net/problem=3
#
# Code by Kevin Marciniak
#
###########################

from advanced_math import *


def prime_factor(num1, num2):
    for i in range(num1, num2):
        if is_prime(i):
            if num2 % i == 0:
                return i


def times_list(array):
    answer = 1
    for i in range(0, len(array)):
        answer *= array[i]
    return answer


# final_tested: int = 13195
final_tested = 600851475143
tested: int = final_tested
possiblePrimeFact = 2
prime_fact_list = []

while times_list(prime_fact_list) < final_tested:
    prime_fact_list.append(prime_factor(possiblePrimeFact, tested))
    if prime_fact_list[-1] == None:
        prime_fact_list.pop()
        prime_fact_list.append(tested)
    else:
        possiblePrimeFact = prime_fact_list[-1]
        tested = int(tested / possiblePrimeFact)

print(prime_fact_list[-1])
