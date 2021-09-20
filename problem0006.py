###########################
#
# #6 Sum square difference - Project Euler
# https://projecteuler.net/problem=6
#
# Code by Kevin Marciniak
#
###########################

sum_of_squares = 0
square_of_sum = 0

# for i in range(1, 11):
for i in range(1, 101):
    sum_of_squares += i * i
    square_of_sum += i

square_of_sum *= square_of_sum

print(square_of_sum - sum_of_squares)
