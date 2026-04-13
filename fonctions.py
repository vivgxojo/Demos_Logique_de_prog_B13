# Définir des fonctions
def saluer():
    print("Bonjour")

def saluer_quelqun(nom):
    print("Bonjour", nom)

def salutation_personnalise(nom, langue = ""): # paramètre optionnel avec valeur par défaut
    if langue == "français":
        print("Bonjour", nom)
    elif langue == "anglais":
        print("Hello", nom)
    elif langue == "espagnol":
        print("Hola", nom)
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
