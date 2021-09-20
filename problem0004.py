###########################
#
# #4 Largest palindrome product - Project Euler
# https://projecteuler.net/problem=4
#
# Code by Kevin Marciniak
#
###########################

# function which return reverse of a string
def reverse(s):
    return s[::-1]


def is_palindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if s == rev:
        return True
    return False


# limit = 100
limit = 1000
largest = 0

for i in range(1, limit):
    for j in range(1, limit):
        if is_palindrome(str(i * j)) and ((i * j) > largest):
            largest = i * j

print(largest)
