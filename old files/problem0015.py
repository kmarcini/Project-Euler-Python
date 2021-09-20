###########################
# Project Euler Problem 15
# Lattice paths
#
# Code by Kevin Marciniak
###########################
# code from: https://stackoverflow.com/questions/2200236/project-euler-15

from math import factorial

n = 20
print(int(factorial(2 * n) / (factorial(n) * factorial(n))))

###########################
# old code, takes forever
###########################

# def traverse_lattice(down_remaining, right_remaining):
# total = 0
# temp_down = 0
# temp_right = 0

# if down_remaining > 0:
# temp_down = traverse_lattice((down_remaining - 1), right_remaining)

# if right_remaining > 0:
# temp_right = traverse_lattice(down_remaining, (right_remaining - 1))

# if down_remaining == 0 and right_remaining == 0:
# return 1

# total = temp_down + temp_right
# return total


# paths = traverse_lattice(2, 2)
# paths = traverse_lattice(20, 20)

# print(paths)
