###########################
# Project Euler Problem 14
# Longest Collatz sequence
#
# Code by Kevin Marciniak
###########################

limit = 1_000_000
longest_count = 0
longest_collatz = 0

for i in range(1, limit):
    temp = i
    count = 0

    while temp != 1:
        if temp % 2 == 0:
            temp /= 2
            count += 1
        else:
            temp = (3 * temp) + 1
            count += 1

    if count > longest_count:
        longest_collatz = i
        longest_count = count

print(longest_collatz)
