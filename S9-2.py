"""
pseudocode
masque_valide = FAUX
REPETER
    DEMANDER octet1
    SI octet < 0 OU > 255:
        AFFICHE erreur
    SINON SI octet1 = 0, 128, 192, 224, 240, 248, 252, 254, 255
        ACCEPTER
    SINON
        AFFICHER erreur
MEME CHOSE POUR octet2, 3, 4
    ...
VÉRIFIER l'ordre des octets
masque = octet1 + "." + octet2 + "." + octet3 + "." + octet4
AFFICHER masque -> masque_valide
"""
masque_valide = False
while True:
    try:
        octet1 = int(input("Entre l'octet 1 : "))
        if octet1 < 0 or octet1 > 255:
            print("Erreur, l'octet doit être ente 0 et 255.")
        elif octet1 == 0 or octet1 == 128 or octet1 == 192 or octet1 ==  224 or octet1 ==  240 or octet1 ==  248 or octet1 == 252 or octet1 ==  254 or octet1 ==  255:
            break
        else:
            print("Erreur, l'octet + 1 est une puissance de 2.")
    except:
        print("Erreur, entrez un nombre entier.")

while True:
    try:
        octet2 = int(input("Entre l'octet 2 : "))
        if octet2 < 0 or octet2 > 255:
            print("Erreur, l'octet doit être ente 0 et 255.")
        elif octet2 in [0, 128, 192, 224, 240, 248, 252, 254, 255]: # si octet est dans la liste
            break
        else:
            print("Erreur, l'octet + 1 est une puissance de 2.")
    except:
        print("Erreur, entrez un nombre entier.")

while True:
    try:
        octet3 = int(input("Entre l'octet 3 : "))
        if octet3 < 0 or octet3 > 255:
            print("Erreur, l'octet doit être ente 0 et 255.")
        elif octet3 in [0, 128, 192, 224, 240, 248, 252, 254, 255]:
            break
        else:
            print("Erreur, l'octet + 1 est une puissance de 2.")
    except:
        print("Erreur, entrez un nombre entier.")

while True:
    try:
        octet4 = int(input("Entre l'octet 4 : "))
        if octet4 < 0 or octet4 > 255:
            print("Erreur, l'octet doit être ente 0 et 255.")
        elif octet4 in [0, 128, 192, 224, 240, 248, 252, 254, 255]:
            break
        else:
            print("Erreur, l'octet + 1 est une puissance de 2.")
    except:
        print("Erreur, entrez un nombre entier.")

if octet1 != 255:
    if octet2 == 0 and octet3 == 0 and octet4 == 0:
        masque_valide = True
else:
    if octet2 != 255:
        if octet3 == 0 and octet4 == 0:
            masque_valide = True
    else:
        if octet3 != 255:
            if octet4 == 0:
                masque_valide = True
        else:
            masque_valide = True
masque = str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4)
print(masque + " -> " + str(masque_valide))