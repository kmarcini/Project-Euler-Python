###########################
#
# #2 Even Fibonacci numbers - Project Euler
# https://projecteuler.net/problem=2
#
# Code by Kevin Marciniak
#
###########################

prev = 1
next = 2

# limit = 100
limit = 4_000_000
answer = 0

print(prev)
print(next)

while next < limit:
    if next % 2 == 0:
        answer += next
    i = next
    next += prev
    prev = i

print(answer)
