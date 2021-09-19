###########################
# Project Euler Problem 25
# 1000-digit Fibonacci number
#
# Code by Kevin Marciniak
###########################

prevNum = 1
nextNum = 1

# limit = 3
limit = 1_000
answer = 1

while len(str(nextNum)) < limit:
	answer += 1
	i = nextNum
	nextNum += prevNum
	prevNum = i

print(answer + 1)
