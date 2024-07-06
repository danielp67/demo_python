import requests

from bs4 import BeautifulSoup

import csv



url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []

for desc in descriptions_bs:
    descriptions.append(desc.string)
    print(descriptions)

fichier = open("hello.txt", "a")
fichier.write("ceci est un message de test 2 !!!")
fichier.close()

with open("hello.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)
    

with open('data.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)