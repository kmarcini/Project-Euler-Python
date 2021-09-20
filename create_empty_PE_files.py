import requests
from bs4 import BeautifulSoup

baseURL = 'https://projecteuler.net/problem='
problemTitle = ''

# change the range as needed
for x in range(1, 766):
    tempURL = baseURL + str(x)

    reqs = requests.get(tempURL)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for title in soup.find_all('title'):
        problemTitle = (title.get_text())

    if x < 10:
        f = open("problem000" + str(x) + ".py", "w")
        f.write("###########################\n" +
                "#\n" +
                "# " + problemTitle + "\n" +
                "# " + tempURL + "\n" +
                "#\n" +
                "# Code by Kevin Marciniak\n" +
                "#\n" +
                "###########################\n")

    if x > 9 and x < 100:
        f = open("problem00" + str(x) + ".py", "w")
        f.write("###########################\n" +
                "#\n" +
                "# " + problemTitle + "\n" +
                "# " + tempURL + "\n" +
                "#\n" +
                "# Code by Kevin Marciniak\n" +
                "#\n" +
                "###########################\n")

    if x > 99 and x < 1000:
        f = open("problem0" + str(x) + ".py", "w")
        f.write("###########################\n" +
                "#\n" +
                "# " + problemTitle + "\n" +
                "# " + tempURL + "\n" +
                "#\n" +
                "# Code by Kevin Marciniak\n" +
                "#\n" +
                "###########################\n")

    if x > 999:
        f = open("problem" + str(x) + ".py", "w")
        f.write("###########################\n" +
                "#\n" +
                "# " + problemTitle + "\n" +
                "# " + tempURL + "\n" +
                "#\n" +
                "# Code by Kevin Marciniak\n" +
                "#\n" +
                "###########################\n")

    f.close()
