###########################
# Project Euler Problem 12
# Highly divisible triangular number
#
# Code by Kevin Marciniak
###########################

from math import *


# code from StackOverflow, my solution was not efficient and was taking forever


def divisors(num):
	number_of_factors = 0
	for i in range(1, int(ceil(sqrt(num))) + 1):
		if num % i == 0:
			number_of_factors += 2
		if i * i == num:
			number_of_factors -= 1
	return number_of_factors


for n in range(1, 1_000_000):
	Tn = (n * (n + 1)) / 2
	if n % 2 == 0:
		count = divisors(n / 2) * divisors(n + 1)
	else:
		count = divisors(n) * divisors((n + 1) / 2)
	if count >= 500:
		print(int(Tn))
		break
