###########################
#
# #22 Names scores - Project Euler
# https://projecteuler.net/problem=22
#
# Code by Kevin Marciniak
#
###########################

tempFile = open("p022_names.txt", "r")
nameList = [x.strip('"').lower() for x in tempFile.readline().split(',')]
nameList.sort()
tempFile.close()

# print(nameList)
nameScore = 0
totalNameScore = 0
for x in range(0, len(nameList)):
    currentName = list(nameList[x])
    print(currentName)
    for y in range(0, len(currentName)):
        if currentName[y] == 'a':
            nameScore += 1
        if currentName[y] == 'b':
            nameScore += 2
        if currentName[y] == 'c':
            nameScore += 3
        if currentName[y] == 'd':
            nameScore += 4
        if currentName[y] == 'e':
            nameScore += 5
        if currentName[y] == 'f':
            nameScore += 6
        if currentName[y] == 'g':
            nameScore += 7
        if currentName[y] == 'h':
            nameScore += 8
        if currentName[y] == 'i':
            nameScore += 9
        if currentName[y] == 'j':
            nameScore += 10
        if currentName[y] == 'k':
            nameScore += 11
        if currentName[y] == 'l':
            nameScore += 12
        if currentName[y] == 'm':
            nameScore += 13
        if currentName[y] == 'n':
            nameScore += 14
        if currentName[y] == 'o':
            nameScore += 15
        if currentName[y] == 'p':
            nameScore += 16
        if currentName[y] == 'q':
            nameScore += 17
        if currentName[y] == 'r':
            nameScore += 18
        if currentName[y] == 's':
            nameScore += 19
        if currentName[y] == 't':
            nameScore += 20
        if currentName[y] == 'u':
            nameScore += 21
        if currentName[y] == 'v':
            nameScore += 22
        if currentName[y] == 'w':
            nameScore += 23
        if currentName[y] == 'x':
            nameScore += 24
        if currentName[y] == 'y':
            nameScore += 25
        if currentName[y] == 'z':
            nameScore += 26

        totalNameScore += ((x + 1) * nameScore)
        nameScore = 0

print(totalNameScore)
