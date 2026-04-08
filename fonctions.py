# Définir des fonctions
def saluer():
    print("Bonjour")

def saluer_quelqun(nom):
    print("Bonjour", nom)

def salutation_personnalise(nom, langue = "francais"): # paramètre optionnel avec valeur par défaut
    if langue == "francais":
        print("Bonjour", nom)
    elif langue == "anglais":
        print("Hello", nom)
    else:
        print("Hi", nom)

def additionner(nb1, nb2):
    somme = nb1 + nb2
    return somme # retourner le résultat au programme principal

def addtionner_soustraire(nb1, nb2):
    """
    Additionner et soustraire deux nombres
    :param nb1: Le premier nombre
    :param nb2: Le deuxième nombre
    :return: la somme et la différence
    """
    somme = nb1 + nb2
    difference = nb1 - nb2
    return somme, difference # retourner plusieurs résultats au programme principal

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