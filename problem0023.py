###########################
#
# #23 Non-abundant sums - Project Euler
# https://projecteuler.net/problem=23
#
# Code by Kevin Marciniak
#
###########################

# def sumproperdivisors(num):
#     sumdivsors = 0
#     for x in range(1, int((num / 2)) + 1):
#         if num % x == 0:
#             sumdivsors += x
#
#     return sumdivsors
#
#
# def findabundantnum(num):
#     abundantlist = []
#     for x in range(1, int((num / 2)) + 1):
#         tempdiv = sumproperdivisors(x)
#         if tempdiv > x:
#             abundantlist.insert(len(abundantlist), x)
#
#     return abundantlist
#
#
# total = 0
# sumOfAbundant = False
#
# for x in range(0, 28123):
#     temp = findabundantnum(x)
#
#     for y in range(0, len(temp)):
#         for z in range(0, len(temp)):
#             if y + z == x:
#                 sumOfAbundant = True
#
#     if not sumOfAbundant:
#         total += x
#
#     sumOfAbundant = False
#
# print(total)
# takes too loooooooooooong!!!!!!

#####################################
#
# From: https://codereview.stackexchange.com/questions/39946/optimizing-solution-for-project-euler-problem-23-non-abundant-sums
#
#####################################
def getsumofdivs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n % i == 0:
            upper = n / i
            total += upper
            if upper != i:
                total += i
        i += 1
    return total


def isabundant(n): return getsumofdivs(n) > n


lAbundants = [x for x in range(12, 28123) if isabundant(x)]
dAbundants = {x: x for x in lAbundants}

sums = 1
for x in range(2, 28123):
    boo = True
    for k in lAbundants:
        if k < x:
            if (x - k) in dAbundants:
                boo = False
                break
        else:
            break
    if boo:
        sums += x

print(sums)
