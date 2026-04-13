from fonctions import *

# Programme principal : utiliser des fonctions
saluer()
saluer_quelqun("Ariane")
saluer_quelqun("Simon")
saluer_quelqun("Younes")
salutation_personnalise("Benjamin", "anglais")
salutation_personnalise("Charles") # utiliser la valeur par défaut pour le paramètre langue
print(additionner(5, 7)) # afficher le résultat (return) de la fonction
resultat = additionner(2, 6) # mettre le résultat (return) de la fonction dans une variable
print(resultat)
additionner(20, 100) # erreur : le résultat n'est jamais affiché
nombre1 = 40
nombre2 = 60
r = additionner(nombre1, nombre2)
print(r)
print(addtionner_soustraire(90, 30))
s, d = addtionner_soustraire(80, 50) # mettre les résultats de la fonction dans des variables
print("Somme :", s)
print("Différence :", d)