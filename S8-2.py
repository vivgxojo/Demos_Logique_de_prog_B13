"""
pseudocode
RÉPÉTER
    ESSAYER
        DEMANDER id
        SI id < 1 OU > 4094
            AFFICHER erreur
        SINON
            ACCEPTER
DEMANDER nom
RÉPÉTER
    ESSAYER
        DEMANDER priorite
        SI priorite < 0 OU > 61440 OU PAS MULTIPLE DE 4096
            AFFICHER erreur
        SINON
            ACCEPTER
AFFICHER id, nom, priorite
"""
while True:
    try:
        id = int(input("Entre le ID du VLAN "))
        if id < 1 or id > 4094:
            print("Erreur, l'ID doit être entre 1 et 4094.")
        else:
            break
    except:
        print("Erreur, entrez un nombre entier.")
nom = input("Entre le nom du VLAN ")
while True:
    try:
        priorite = int(input("Entre la priorité STP "))
        if priorite < 0 or priorite > 61440 or priorite % 4096 != 0:
            print("Erreur, la priorité doit être un multiple de 4096 entre 0 et 61440.")
        else:
            break
    except:
        print("Erreur, entrez un nombre entier.")
print("Résumé du VLAN : ")
print("ID:", id)
print("Nom:", nom)
print("Priorité: ", priorite)