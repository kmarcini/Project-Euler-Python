import requests
from bs4 import BeautifulSoup

baseURL = 'https://projecteuler.net/problem='
problemTitle = ''

for x in range(28, 767):
    tempURL = baseURL + str(x)

    reqs = requests.get(tempURL)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for title in soup.find_all('title'):
        problemTitle = (title.get_text())
    f = open("problem0" + str(x) + ".py", "w")
    f.write("###########################\n" +
            "# Project Euler Problem " + str(x) + "\n" +
            "# " + problemTitle + "\n" +
            "#\n" +
            "# Code by Kevin Marciniak\n" +
            "###########################\n")

    f.close()
