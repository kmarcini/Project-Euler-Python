###########################
# Project Euler Problem 2
# Even Fibonacci numbers
#
# Code by Kevin Marciniak
###########################

prev = 1
next = 2

# limit = 100
limit = 4_000_000
answer = 0

print(str(prev))
print(str(next))

while next < limit:
    if next % 2 == 0:
        answer += next
    i = next
    next += prev
    prev = i

print(str(answer))
