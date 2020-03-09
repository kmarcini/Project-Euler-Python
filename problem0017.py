###########################
# Project Euler Problem 16
# Power digit sum
#
# Code by Kevin Marciniak
###########################


def num_to_word(num):
    if len(num) == 3:
        if num[1] == "0" and num[2] == "0":
            return num_to_word(num[0]) + "hundred"
        else:
            return num_to_word(num[0]) + "hundredand" + num_to_word(num[1:])

    if len(num) == 2:
        if num[0] == "9":
            return "ninety" + num_to_word(num[1])
        if num[0] == "8":
            return "eighty" + num_to_word(num[1])
        if num[0] == "7":
            return "seventy" + num_to_word(num[1])
        if num[0] == "6":
            return "sixty" + num_to_word(num[1])
        if num[0] == "5":
            return "fifty" + num_to_word(num[1])
        if num[0] == "4":
            return "forty" + num_to_word(num[1])
        if num[0] == "3":
            return "thirty" + num_to_word(num[1])
        if num[0] == "2":
            return "twenty" + num_to_word(num[1])
        if num[0] == "1":
            if num[1] == "9":
                return "nineteen"
            if num[1] == "8":
                return "eighteen"
            if num[1] == "7":
                return "seventeen"
            if num[1] == "6":
                return "sixteen"
            if num[1] == "5":
                return "fifteen"
            if num[1] == "4":
                return "fourteen"
            if num[1] == "3":
                return "thirteen"
            if num[1] == "2":
                return "twelve"
            if num[1] == "1":
                return "eleven"
            if num[1] == "0":
                return "ten"
        if num[0] == "0":
            return "" + num_to_word(num[1])

    if len(num) == 1:
        if num == "9":
            return "nine"
        if num == "8":
            return "eight"
        if num == "7":
            return "seven"
        if num == "6":
            return "six"
        if num == "5":
            return "five"
        if num == "4":
            return "four"
        if num == "3":
            return "three"
        if num == "2":
            return "two"
        if num == "1":
            return "one"
        if num == "0":
            return ""


# print(len(num_to_word(str(342))))  # equals 23 letters
# print(len(num_to_word(str(115))))  # equals 20 letters

temp = len("onethousand")

for i in range(1, 1000):
    temp += len(num_to_word(str(i)))

print(temp)
