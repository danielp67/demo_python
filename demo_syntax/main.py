# main.py
import calculator.calculator_module as test


test.print_welcome_message()



nom = "Dupont"
prenom = "Jean"
age = 30
age += 10
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print(f"Bonjour, je m'appelle {prenom} {nom} et j'ai {age+10} ans. Mon age est de type {type(age)}")
print((plateformes_sociales.index("Snapchat")))
print(plateformes_sociales[2])


nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}


taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2


print ("nom_de_campagne" in nouvelle_campagne)


avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")


fruit = "pomme"
match fruit:
    case "pommes":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")
        

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(10):
    print(f"{x} bouteilles de bières au mur !")


capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(f"Capacité actuelle : {capacite_actuelle}")

liste = [1, 2, 3, 4, 5]
    # Boucle for sur la liste
for element in liste:
    if element == 3:
# Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
# Dans tous les autres cas, on exécute le reste du code
    print(element)

# Fonctions
def afficher_message(nom, prenom):
    print( f"Bonjour, comment ça va {nom} {prenom}?")


afficher_message("Dupont", "Jean")



try:
    print(x)
except:
    print("Variable x n'existe pas")



import requests

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content)