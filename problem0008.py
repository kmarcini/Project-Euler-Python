###########################
# Project Euler Problem 8
# Largest product in a series
#
# Code by Kevin Marciniak
###########################


def int_to_list(num, temp_list):
    for x in str(num):
        temp_list.append(int(x))
    return temp_list


# adjacent_digits = 4
adjacent_digits = 13
greatest_product = 0

total = []
big_num1 = 73167176531330624919225119674426574742355349194934
big_num2 = 96983520312774506326239578318016984801869478851843
big_num3 = 85861560789112949495459501737958331952853208805511
big_num4 = 12540698747158523863050715693290963295227443043557
big_num5 = 66896648950445244523161731856403098711121722383113
big_num6 = 62229893423380308135336276614282806444486645238749
big_num7 = 30358907296290491560440772390713810515859307960866
big_num8 = 70172427121883998797908792274921901699720888093776
big_num9 = 65727333001053367881220235421809751254540594752243
big_num10 = 52584907711670556013604839586446706324415722155397
big_num11 = 53697817977846174064955149290862569321978468622482
big_num12 = 83972241375657056057490261407972968652414535100474
big_num13 = 82166370484403199890008895243450658541227588666881
big_num14 = 16427171479924442928230863465674813919123162824586
big_num15 = 17866458359124566529476545682848912883142607690042
big_num16 = 2421902267105562632111110937054421750694165896040
big_num17 = 807198403850962455444362981230987879927244284909188
big_num18 = 8458015616609791913387549920052406368991256071760
big_num19 = 605886116467109405077541002256983155200055935729725
big_num20 = 71636269561882670428252483600823257530420752963450

# have to do this the hard way for now, may refactor this later
total = int_to_list(big_num1, total)
total = int_to_list(big_num2, total)
total = int_to_list(big_num3, total)
total = int_to_list(big_num4, total)
total = int_to_list(big_num5, total)
total = int_to_list(big_num6, total)
total = int_to_list(big_num7, total)
total = int_to_list(big_num8, total)
total = int_to_list(big_num9, total)
total = int_to_list(big_num10, total)
total = int_to_list(big_num11, total)
total = int_to_list(big_num12, total)
total = int_to_list(big_num13, total)
total = int_to_list(big_num14, total)
total = int_to_list(big_num15, total)
total = int_to_list(big_num16, total)
total = int_to_list(big_num17, total)
total = int_to_list(big_num18, total)
total = int_to_list(big_num19, total)
total = int_to_list(big_num20, total)

total_length = len(total) - (adjacent_digits - 1)

for i in range(1, total_length):
    temp_gp = total[i]
    for j in range(1, adjacent_digits):
        temp_gp *= total[i + j]
    if temp_gp > greatest_product:
        greatest_product = temp_gp

print(greatest_product)
